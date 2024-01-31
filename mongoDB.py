import pymongo
import sys
from urllib.parse import quote_plus

username = quote_plus('admin')
password = quote_plus('admin')

try:
    uri = "mongodb+srv://{username}:{password}@music.tsc9co1.mongodb.net/user?retryWrites=true&w=majority"
    client = pymongo.MongoClient(uri)
    client.close()


    # Rest of your script
except RuntimeError as e:
    print(f"Caught an exception: {e}")
