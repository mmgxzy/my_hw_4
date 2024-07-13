import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        
    def create_table(self):
        with self.connection:
            self.cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL, 
                    username TEXT,
                    age INT
                )    
            """)
            
    def add_user(self, user_id, username, age):
        with self.connection:
            self.cursor.execute("INSERT INTO users (user_id, username, age) VALUES (?, ?, ?)", (user_id, username, age))

    def get_user(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()

    def close(self):
        self.connection.close()
