import pymongo
from tabulate import tabulate

class MongoDBHelper:

    def __init__(self,collection='customer'):
        uri = "mongodb+srv://root:pass123@cluster0.hpla9eh.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(uri)
        self.db = client['gw2023pds1']
        self.collection=self.db[collection]
        print("MongoDB Connected")

    def insert(self , document):
        result = self.collection.insert_one(document)
        print("Document Inserted" , result)
        return result

    def delete(self, query):
        result = self.collection.delete_one(query)
        print("Document Deleted", result)


    def fetch(self, query=""):
            documents = list(self.collection.find(query))
            return list(documents)

        #for document in documents:
        #   print(document)


    def update(self, document, query):
        update_query = {'$set': document}
        result = self.collection.update_one(query, update_query)
        print("Updated Document:", result.modified_count)
