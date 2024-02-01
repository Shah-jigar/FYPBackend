

import requests
import os

cur_path = os.path.dirname(__file__)


def fetch_lyrics(artist_name, song_name, path="lyrics"):
    try:
        # artist_name = "Arjun Kaungo"
        # song_name = "Ishq Samundar"
        param = song_name + " " + artist_name
        param = param.replace(' ', '+')
        res = requests.get(
            "https://www.jiosaavn.com/api.php?__call=autocomplete.get&_format=json&_marker=0&includeMetaTags=1&query={param}".format(param=param)).json()
        try:
            song_id = res['songs']['data'][0]['id']
            res = requests.get(
                "https://www.jiosaavn.com/api.php?__call=lyrics.getLyrics&ctx=web6dot0&api_version=4&_format=json&_marker=0%3F_marker%3D0&lyrics_id={id}".format(id=song_id)).json()
            lyrics = res['lyrics'].replace('<br>', "\n")
            print(lyrics)
            with open(path+"/"+artist_name+' - '+song_name+'.txt', 'w', encoding='utf-8') as file:
                # Write content to the file
                file.write(lyrics)
            return {"lyrics": lyrics}
        except:
            return {"Error": "Not found"}
    except Exception as e:
        return {"Error": e}


song_name = "Udd Jaa Kaale Kaava"
artist_name = "Udit Narayan, Alka Yagnik, Mithoon, Uttam Singh"

lyr = fetch_lyrics(artist_name, song_name, path = "lyrics")
# print(lyr)
