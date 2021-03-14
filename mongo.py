import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDatabase"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected ")
        return conn
    except pymongo.errors.ConnectionFailure as e :
        print("could not connncet to MongoDB: %S")%e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]
new_doc = {"first":"takudzwa","last":"chauruka","dob":"01/06/1998","gender":"m","hair_colour":"black","occupation":"engineer","nationality":"zimbabwean"}
coll.insert(new_doc)
documents = coll.find()

for doc in documents:
    print (doc)
