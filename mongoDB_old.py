from pprint import pprint
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId, Binary
from gridfs import GridFS
from dotenv import load_dotenv, find_dotenv
import os
import pandas as pd

load_dotenv(find_dotenv())
connections = {'local': None, 'remote': None}


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
    return result.inserted_id
    # print(f'data: {data}')


def read_documents(collection, query={}):
    cursor = collection.find(query)
    for document in cursor:
        print(document)


def update_document(collection, query, new_data):
    result = collection.update_one(query, {'$set': new_data})
    print(f"Matched {result.matched_count} document(s) and modified {
          result.modified_count} document(s)")


def delete_document(collection, query):
    result = collection.delete_one(query)
    print(f"Deleted {result.deleted_count} document(s)")


def fetch_record(collection, query):
    cursor = collection.find_one(query)
    return cursor


def get_maxId_songs():
    with open("songsMaxid.txt", 'r') as file:
        data = file.read()
        return data


def set_maxId_songs(id):
    with open("songsMaxid.txt", 'w') as file:
        file.write(str(id))
    print(f'Max id set to {id}')


def check_if_exists(collection, query):
    cursor = collection.find_one(query)
    if cursor:
        print(f'document already exists with same data for the data : _id={cursor['_id']}, id = {
              cursor['id']}, SongName = {cursor["Song Name"]}, artist = {cursor['artists']} ')
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
        x = row['Song_Name']
        features = row[2:15]
        # print(features)
        folder, songData = x.split('/')
        artist, song = songData.split(" - ", 1)
        data = {"Song Name": song, "artists": [
            artist], "lyrics": row['lyrics']}
        exists = check_if_exists(collection=collections[0], query=data)
        uploaded_file = ''
        try:
            if not exists:
                with open(dir+x, "rb") as file:
                    file_data = file.read()
                    uploaded_file = fs.put(
                        file_data, filename=row['Song_Name'])
                
                # For adding data of the extracted features to the other collection -> pending
                features['Song Name'] = song
                features['artists'] = artist
                # print(features)
                id_features = create_document(collection=collections[1], data=features)

                id = int(get_maxId_songs()) + 1
                data_to_insert = {"Song Name": song, "artists": [
                    artist], "lyrics": row['lyrics'], 'features_id':id_features, 'file': uploaded_file, "id": id, 'genre': folder, "emotion": ''}
                create_document(collection=collections[0], data=data_to_insert)
                set_maxId_songs(id)




            else:
                data = {"Song Name": song, "artists": [artist]}
                record = fetch_record(collection=collections[0], query=data)
                if record['lyrics'] == '' and row['lyrics'] != '':
                    data['lyrics'] = row['lyrics']
                if record[types] == '' and folder != '':
                    data['lyrics'] = row['lyrics']
        except Exception as e:
            print(e)
            lst.append(x)

    pprint(lst)


if __name__ == "__main__":
    os.system('clear')

    # Get connection
    client, db = get_connection(level='local', db_name='music')
    collection1 = db['songs']
    collection2 = db['song_features']

    load_songs_csv(csv_path='Songs/genres/all_features_947.csv',
                   types='genres', db=db, collections=[collection1, collection2])

    # Update entry
    # update_query = {'_id': ObjectId('65efeafe5a6afb9cf404edbc')}
    # new_data = {"city": "Mumbai"}
    # update_document(update_query, new_data)

    # Read documents
    # read_documents()

    # Delete a document
    # delete_query = {"name": "John Doe"}
    # delete_document(delete_query)

    # Read documents
    # myquery = { "city": {"$gt": "N"} }
    # read_documents(myquery)
