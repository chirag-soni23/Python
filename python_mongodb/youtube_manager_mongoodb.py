from pymongo import MongoClient
from urllib.parse import quote_plus
from bson import ObjectId

# Escape username and password
username = "youtubepy"
password = "ADgj703@#"
escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

# Construct the connection URI with escaped username and password
uri = f"mongodb+srv://{escaped_username}:{escaped_password}@cluster0.oq8kfpe.mongodb.net/"

# Connect to the MongoDB cluster
client = MongoClient(uri, tlsAllowInvalidCertificates=True)

# Access the "ytmanager" database and the "videos" collection
db = client["ytmanager"]
video_collection = db['videos']

print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"Id: {video['_id']}, name: {video['name']}, time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, newName, newTime):
    video_collection.update_one({"_id": ObjectId(video_id)}, {'$set': {"name": newName, "time": newTime}})

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})

def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video id: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the video id: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
