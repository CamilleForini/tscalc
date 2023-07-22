"""This module adds songs from a file txt to a db"""
from mysql_connection import connection


# Opens txt files with song list
with open("ts_songs.txt", "r") as ts_songs_file:
    ts_song_list = ts_songs_file.readlines()

ts_song_list_formatted = []
for song in ts_song_list:
    ts_song_list_formatted.append(song.strip().title())

# MYSQL CONNECTION
myconnection = connection()

# ADDS SONG NAME TO DB
with myconnection:
    with myconnection.cursor() as cursor:
        for song in ts_song_list_formatted:
            sql = f"INSERT INTO ts_songs (name) VALUE ('{song}')"
            cursor.execute(sql)
            myconnection.commit()
