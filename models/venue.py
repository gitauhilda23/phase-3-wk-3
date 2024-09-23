# models/venue.py

import sqlite3
from models.band import Band  # Ensure to import the Band class

class Venue:
    def __init__(self, title):
        self.title = title

    def concerts(self):
        connection = sqlite3.connect('concerts.db')
        try:
            cursor = connection.cursor()
            cursor.execute('''
            SELECT * FROM concerts WHERE venue_title = ?
            ''', (self.title,))
            results = cursor.fetchall()
        finally:
            connection.close()
        return results

    def bands(self):
        connection = sqlite3.connect('concerts.db')
        try:
            cursor = connection.cursor()
            cursor.execute('''
            SELECT DISTINCT bands.* FROM bands
            JOIN concerts ON bands.name = concerts.band_name
            WHERE concerts.venue_title = ?
            ''', (self.title,))
            results = cursor.fetchall()
        finally:
            connection.close()
        
        # Convert results to Band instances
        return [Band(name=row[0]) for row in results]

