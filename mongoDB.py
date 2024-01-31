from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId



username = "admin"
password = "admin"
uri = f"mongodb+srv://{username}:{password}@music.tsc9co1.mongodb.net/user?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['test']
collection = db['data']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def create_document(data):
    result = collection.insert_one(data)
    print(f"Document inserted with ID: {result.inserted_id}")

# Read (Query) Document
def read_documents(query={}):
    cursor = collection.find(query)
    for document in cursor:
        print(document)    
        
# Update Document
def update_document(query, new_data):
    result = collection.update_one(query, {'$set': new_data})
    print(f"Matched {result.matched_count} document(s) and modified {result.modified_count} document(s)")

# Delete Document
def delete_document(query):
    result = collection.delete_one(query)
    print(f"Deleted {result.deleted_count} document(s)")

if __name__ == "__main__":

    # insert entry
    # data_to_insert = {"name": "John Doe", "age": 30, "city": "New York"}
    # create_document(data_to_insert)


    # Update entry 
    update_query = {'_id': ObjectId('65ba1bc68b0a532f6aaade12')}
    new_data = {"city": "Mumbai"}
    update_document(update_query, new_data)

    # Read documents
    # read_documents()

    # Delete a document
    # delete_query = {"name": "John Doe"}
    # delete_document(delete_query)

    # Read documents
    # myquery = { "city": {"$gt": "N"} }
    # read_documents(myquery)








    ...