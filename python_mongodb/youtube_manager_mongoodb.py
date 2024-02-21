from pymongo import MongoClient
from urllib.parse import quote_plus

# Escape username and password
username = "youtubepy"
password = "ADgj703@#"
escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

# Construct the connection URI with escaped username and password
uri = f"mongodb+srv://{escaped_username}:{escaped_password}@cluster0.oq8kfpe.mongodb.net/"

# Connect to the MongoDB cluster
client = MongoClient(uri)

# Access the "ytmanager" database and the "videos" collection
db = client["ytmanager"]
video_collection = db['videos']

print(video_collection)
