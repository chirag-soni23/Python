from pymongo import MongoClient
client = MongoClient("mongodb+srv://youtubepy:ADgj703@#@cluster0.oq8kfpe.mongodb.net/")
# Not a good idea to include id and password in code files
db = client["ytmanager"]
video_collection = db['videos']

print(video_collection)

