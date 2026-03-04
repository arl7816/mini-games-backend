import sqlite3
from src.config import settings

location = settings.DB_LOCATION

# python -m src.databasemanager.database_create
def main() -> None:
    
    con = sqlite3.connect(location)
    cur = con.cursor()


    try:
        cur.execute("""CREATE TABLE User(
                    email VARCHAR(30) PRIMARY KEY, 
                    username VARCHAR(30) UNIQUE NOT NULL, 
                    password VARCHAR(50) NOT NULL);""")
        print("Created User Table")
    except: 
        print("User Table already exists, skipping this")

    try:
        cur.execute("""
            CREATE TABLE GameSession (
                session_id INTEGER PRIMARY KEY AUTOINCREMENT,
                start_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
                user_email VARCHAR(30) NOT NULL, 
                game_type VARCHAR(10) NOT NULL, 
                name VARCHAR(20) NOT NULL, 
                difficulty INTEGER NOT NULL, 
                game_info JSON, 
                CONSTRAINT fk_user 
                    FOREIGN KEY (user_email) 
                    REFERENCES User (email) 
                    ON DELETE CASCADE,
                CONSTRAINT check_game_type 
                    CHECK (game_type IN ('TTT', 'RPS', 'COUNT')),
                CONSTRAINT check_difficulty 
                    CHECK (difficulty > 0)
            );
        """)
        print("Game Session Table Created")
    except:
        print("GameSession Table already exists")


    return

if __name__ == "__main__":
    main()