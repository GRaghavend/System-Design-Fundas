import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS letters (
    Letter_ID INTEGER PRIMARY KEY,
    Letters TEXT )
    """
)

cursor.execute(
    """
    INSERT INTO letters (Letters)
    VALUES ('A')
    """
)

conn.commit()
conn.close()

print("Database created and letter inserted successfully.")

