# models/band.py

import sqlite3
from models.concert import Concert

class Band:
    def __init__(self, name):
        self.name = name

    def concerts(self):
        connection = sqlite3.connect('concerts.db')
        try:
            cursor = connection.cursor()
            cursor.execute('''
            SELECT * FROM concerts WHERE band_name = ?
            ''', (self.name,))
            results = cursor.fetchall()
        finally:
            connection.close()
        return results

    def venues(self):
        connection = sqlite3.connect('concerts.db')
        try:
            cursor = connection.cursor()
            cursor.execute('''
            SELECT DISTINCT venues.* FROM venues
            JOIN concerts ON venues.title = concerts.venue_title
            WHERE concerts.band_name = ?
            ''', (self.name,))
            results = cursor.fetchall()
        finally:
            connection.close()
        return results

    def play_in_venue(self, venue_title, date):
        connection = sqlite3.connect('concerts.db')
        try:
            cursor = connection.cursor()
            cursor.execute('''
            INSERT INTO concerts (band_name, venue_title, date) VALUES (?, ?, ?)
            ''', (self.name, venue_title, date))
            connection.commit()
        finally:
            connection.close()

    def all_introductions(self):
        intros = []
        for concert in self.concerts():
            concert_instance = Concert(concert[0])  # Use the concert ID
            intros.append(concert_instance.introduction())
        return intros

    @staticmethod
    def most_performances():
        connection = sqlite3.connect('concerts.db')
        try:
            cursor = connection.cursor()
            cursor.execute('''
            SELECT band_name, COUNT(*) as performance_count FROM concerts
            GROUP BY band_name
            ORDER BY performance_count DESC
            LIMIT 1
            ''')
            result = cursor.fetchone()
        finally:
            connection.close()
        return result
