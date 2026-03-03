import sqlite3
from src.config import settings

location = settings.DB_LOCATION

# python -m src.databasemanager.database_create
def main() -> None:
    
    print("Creaing user table")

    con = sqlite3.connect(location)
    cur = con.cursor()


    try:
        cur.execute("CREATE TABLE User(email VARCHAR(30) PRIMARY KEY, username VARCHAR(30) NOT NULL, password VARCHAR(50) NOT NULL)")
    except: 
        print("User Table already exists, skipping this")


    return

if __name__ == "__main__":
    main()