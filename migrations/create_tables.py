# migrations/create_tables.py

import sqlite3

def create_tables():
    connection = sqlite3.connect('concerts.db')  # Connect to the database
    cursor = connection.cursor()

    # Create bands table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bands (
        name TEXT PRIMARY KEY,
        hometown TEXT
    )''')

    # Create venues table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS venues (
        title TEXT PRIMARY KEY,
        city TEXT
    )''')

    # Create concerts table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS concerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        band_name TEXT,
        venue_title TEXT,
        date TEXT,
        FOREIGN KEY(band_name) REFERENCES bands(name),
        FOREIGN KEY(venue_title) REFERENCES venues(title)
    )''')

    connection.commit()  # Commit changes
    connection.close()   # Close the connection

if __name__ == "__main__":
    create_tables()  # Run the function to create tables
