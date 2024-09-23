# models/concert.py

import sqlite3

class Concert:
    def __init__(self, id):
        self.id = id

    def band(self):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT * FROM bands
        JOIN concerts ON bands.name = concerts.band_name
        WHERE concerts.id = ?
        ''', (self.id,))
        result = cursor.fetchone()
        connection.close()
        return result

    def venue(self):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT * FROM venues
        JOIN concerts ON venues.title = concerts.venue_title
        WHERE concerts.id = ?
        ''', (self.id,))
        result = cursor.fetchone()
        connection.close()
        return result

    def hometown_show(self):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT bands.hometown, venues.city FROM bands
        JOIN concerts ON bands.name = concerts.band_name
        JOIN venues ON concerts.venue_title = venues.title
        WHERE concerts.id = ?
        ''', (self.id,))
        hometown, city = cursor.fetchone()
        connection.close()
        return hometown == city

    def introduction(self):
        band = self.band()
        venue = self.venue()
        return f"Hello {venue[1]}!!!!! We are {band[0]} and we're from {band[1]}"
