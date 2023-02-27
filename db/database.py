import pymongo
import os
#url = "mongodb+srv://chauhan:chauhanji1@cluster0.kflv2hk.mongodb.net/?retryWrites=true&w=majority"
url = os.getenv("MONGO_URL")
client = pymongo.MongoClient(url)
database = client["Amarjeet"]
collection=database["chauhan"]

def showdata():
    l=[]
    f=collection.find()
    for i in f:
        i["_id"]=str(i["_id"])
        l.append(i)
    return l

#loginvalidation###################
def validationdata(data):
    collection.find_one(data)
    return True

#singup #######################
def adddata(data1):
    data1 = dict(data1)
    f=collection.insert_one(data1)
    return "Successfully Added data"