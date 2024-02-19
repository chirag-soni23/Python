import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS video (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
)
''')
def list_videos():
       pass

def add_video():
       pass
def main():
       while True:
              print("\n Youtube manager app with DB")
              print("1. List videos")
              print("2. Add videos")
              print("3. Update videos")
              print("4. Delete videos")
              print("5. Exit app")
              choice = input("Enter Your Choice: ")

              if choice == '1':
                     list_videos()
              elif choice == '2':
                    name = input("Enter the video name: ")
                    time = input("Enter the video time: ")
                    add_video(name,time)
              elif choice == '3':
                    input("Enter video ID to update: ")
                    name = input("Enter the video name: ")
                    time = input("Enter the video time: ")
                    add_video(name,time)
       

if __name__ == "__main__":
       main()