def load_data():
    pass

def list_all_videos(videos):
    pass

def add_videos(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager | Choose an option")
        print("1. List all YouTube videos ")
        print("2. Add a YouTube video ")
        print("3. Update a YouTube video details ")
        print("4. Delete a YouTube video ")
        print("5. Exit the app ")
        choice = input("Enter Your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()
