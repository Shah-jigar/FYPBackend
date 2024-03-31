import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId, Binary
from gridfs import GridFS
from dotenv import load_dotenv, find_dotenv
import pandas as pd
import librosa
from librosa import feature
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib

from pprint import pprint

load_dotenv(find_dotenv())
connections = {'local': None, 'remote': None}

# For getting Feature Vector
fn_list_i = [
    librosa.onset.onset_strength,              # it is spectral_flux
    # chromagram from a waveform or power spectrogram
    feature.chroma_stft,
    feature.chroma_cqt,
    feature.chroma_cens,
    feature.melspectrogram,
    feature.mfcc,
    feature.spectral_centroid,
    feature.spectral_bandwidth,
    feature.spectral_contrast,
    feature.spectral_rolloff,
    feature.tonnetz
]

fn_list_ii = [
    feature.zero_crossing_rate
]


def get_feature_vector(y, sr):
    feat_vect_i = [np.mean(funct(y=y, sr=sr)) for funct in fn_list_i]
    feat_vect_ii = [np.mean(funct(y=y)) for funct in fn_list_ii]
    feature_vector = feat_vect_i + feat_vect_ii
    return feature_vector


def get_connection(level, db_name):

    if level == 'local':
        url = os.getenv('MONGODB_LOCAL_URL')
    elif level == 'remote':
        url = str(os.getenv('MONGODB_REMOTE_URI'))
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        url = url.replace("<username>", username)
        url = url.replace("<password>", password)
    else:
        raise Exception("Please provide a proper method for connection")

    if connections[level] is None:
        # Create a new client and connect to the server
        client = MongoClient(url, server_api=ServerApi('1'))
        connections[level] = client
    else:
        client = connections[level]
    db = client[db_name]
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return client, db


def close_connection(client):
    client.close()


def create_document(collection, data):
    result = collection.insert_one(data)
    print(f"Document inserted with ID: {result.inserted_id}")
    # print(f'data: {data}')
    return result.inserted_id


def read_documents(collection, query={}):
    cursor = collection.find(query)
    for document in cursor:
        print(document)


def update_document(collection, query, new_data):
    print(new_data)
    pprint(query)
    result = collection.update_one(query, {'$set': new_data})
    print(f"Matched {result.matched_count} document(s) and modified {
          result.modified_count} document(s)")


def delete_document(collection, query):
    result = collection.delete_one(query)
    print(f"Deleted {result.deleted_count} document(s)")


def fetch_record(collection, query):
    cursor = collection.find_one(query)
    # print(cursor['_id'])
    return cursor


def check_if_exists(collection, query):
    cursor = collection.find_one(query)
    if cursor:
        print(f"document already exists with same data for the data : _id={
              cursor['_id']}, SongName = {cursor["Song Name"]}, artist = {cursor['artist']}, genre = {cursor['genre']}, emotion = {cursor['emotion']} ")
        return cursor
    else:
        return None


def load_songs_csv(csv_path, types, db, collections,):
    fs = GridFS(db)
    current_dir = os.getcwd()
    dir = os.path.join(current_dir, "Songs", types, "")
    dir = dir.replace('\\', '/')
    print(dir)
    if types == 'genres':
        types = 'genre'
    elif types == 'emotions':
        types = 'emotion'
    else:
        raise Exception(
            f"Enter proper type for the loading function. Possible Values include emotions and genres only but '"+types+"' was provided")
    df = pd.read_csv(csv_path)
    lst = []
    for index, row in df.iterrows():
        print(index)
        x = row['Song_Name']
        features = row[2:15]
        # print(features)
        folder, songData = x.split('/')
        artist, song = songData.split(" - ", 1)
        song = song.split(".")[0]
        data = {"Song Name": song, "artist": artist}
        exists = check_if_exists(collection=collections[0], query=data)

        uploaded_file = ''
        try:
            if not exists:
                with open(dir+x, "rb") as file:
                    file_data = file.read()
                    uploaded_file = fs.put(
                        file_data, filename=row['Song_Name'])
                data_to_insert0 = {"Song Name": song, "artist": artist}
                data_to_insert0.update(features)
                features_id = create_document(
                    collection=collections[1], data=data_to_insert0)
                data_to_insert = {"Song Name": song, "artist": artist,
                                  "lyrics": row['lyrics'], 'file': uploaded_file, 'features_id': features_id, 'genre': '', "emotion": ''}
                data_to_insert[types] = folder
                create_document(collection=collections[0], data=data_to_insert)
            else:
                data = {"Song Name": song, "artist": artist}
                record = fetch_record(collection=collections[0], query=data)
                if record['lyrics'] == '' and row['lyrics'] != '':
                    data['lyrics'] = row['lyrics']
                if record[types] == '' and folder != '':
                    data[types] = folder
                update_document(
                    collection=collections[0], query={"_id": record['_id']}, new_data=data)
        except:
            lst.append(x)
    print("printing list of songs that could not be added to db or gave some error during insertion")
    pprint(lst)


def create_dataset(collections):

    pipeline = [
        {
            "$lookup": {
                "from": 'song_features',
                "localField": "features_id",
                "foreignField": "_id",
                "as": "matched_data"
            }
        },
        {
            "$unwind": "$matched_data"
        },
        {
            "$project": {
                "_id": 1,
                "Song Name": 1,
                "artist": 1,
                "lyrics": 1,
                "onset_strength": "$matched_data.onset_strength",
                "chroma_stft": "$matched_data.chroma_stft",
                "chroma_cqt": "$matched_data.chroma_cqt",
                "chroma_cens": "$matched_data.chroma_cens",
                "melspectrogram": "$matched_data.melspectrogram",
                "mfcc": "$matched_data.mfcc",
                "spectral_centroid": "$matched_data.spectral_centroid",
                "spectral_bandwidth": "$matched_data.spectral_bandwidth",
                "spectral_contrast": "$matched_data.spectral_contrast",
                "spectral_rolloff": "$matched_data.spectral_rolloff",
                "tonnetz": "$matched_data.tonnetz",
                "zero_crossing_rate": "$matched_data.zero_crossing_rate",
                "genre": 1,
                "emotion": 1
            }
        }
    ]
    result = pd.DataFrame(db.songs.aggregate(pipeline))
    print(result)
    columns = result.columns.tolist()
    columns.remove("genre")
    columns.remove("emotion")
    columns.extend(["genre", "emotion"])
    result = result[columns]
    result.to_csv('dataset')


def load_model(type):
    loaded_model = joblib.load(
        f"C:/Projects/python/FYPBackend/models/best_Random Forest.joblib") or None
    return loaded_model


def insertSong(collections, path):
    current_dir = os.getcwd()
    path = path.replace('\\', '/')
    dir = os.path.join(current_dir, path)
    dir = dir.replace('\\', '/')

    print(path)
    print(dir)

    full = False
    if dir != path:
        path = dir
    y, sr = None, None
    print("Extracting featrues from file")
    # try:
    #     full=True
    #     y, sr = librosa.load(path, sr=None)
    # except:
    y, sr = librosa.load(dir, sr=None)
    feature_vector = get_feature_vector(y, sr)
    print(feature_vector)

    labels_emotion = {0: "Happy", 1: "Sad", 2: "Love", 3: "Energetic"}
    labels_genre = {0: "Hindi Rap", 1: "Ghazal", 2: "Gharwali",
                    3: "Bhajan", 4: "Hindi Romantic", 5: "Sufi"}

    model = load_model('genre') or None
    genre = labels_genre[tuple(model.predict([feature_vector]))[0]]

    model = load_model('genre') or None
    emotion = labels_emotion[tuple(model.predict([feature_vector]))[0]]

    # Left
    x = path.split('/')[-1]
    artist, song = x.split(" - ", 1)
    song = song.split(".")[0]
    data = {"Song Name": song, "artist": artist}
    print(data)
    data = data+feature
    data['genre'] = genre or ""
    data['emotion'] = emotion or ""

    create_document(collection=collections[0], data=data)

    # till here

    return genre, emotion


if __name__ == "__main__":
    os.system('clear')

    # Get connection
    client, db = get_connection(level='local', db_name='music')
    collection0 = db['songs']
    collection1 = db['song_features']

    # load_songs_csv(csv_path='Songs/genres/all_features_947.csv',
    #                types='genres', db=db, collections=[collection0, collection1])
    # load_songs_csv(csv_path='Songs/emotions/all_features_emotion_559.csv',
    #    types='emotions', db=db, collections=[collection0, collection1])

    insertSong(collections=[collection0, collection1],
               path='download/Tanishk Bagchi - Teri Baaton Mein Aisa Uljha Jiya.opus')
    # create_dataset(collections=[collection0, collection1])
