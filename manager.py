import sqlite3

# Connect to the database (creates it if not exists)
conn = sqlite3.connect("test.db")
print("DB created successfully")

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Create table (fixed the SQL syntax)
cur.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

# Function to list all videos
def list_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)

# Function to add a new video
def add_video(name, time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

# Function to update a video by ID
def video_update(video_id, new_name, new_time):
    cur.execute("UPDATE videos SET name=?, time=? WHERE id=?", (new_name, new_time, video_id))
    conn.commit()

# Function to delete a video by ID
def delete_video(video_id):
    cur.execute("DELETE FROM videos WHERE id=?", (video_id,))
    conn.commit()

# Main app loop
def main():
    while True:
        print("\nYouTube Manager App with DB")
        print("1. List videos")
        print("2. Add video")
        print("3. Delete video")
        print("4. Update video")
        print("5. Exit app")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == "4":
            video_id = input("Enter video ID to update: ")
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")
            video_update(video_id, name, time)
        elif choice == "5":
            print("Exiting app...")
            break
        else:
            print("Wrong choice, please try again.")

    conn.close()

# Entry point
if __name__ == "__main__":
    main()
