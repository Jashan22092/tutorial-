import pymongo
uri = "mongodb+srv://root:pass123@cluster0.hpla9eh.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
db = client['gw2023pds1']
collections = db.list_collection_names()
#print(collections)
for collection in collections:
    print(collection)

documents = db['customer'].find()
for document in documents:
    print(document)