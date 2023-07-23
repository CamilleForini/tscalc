"""This module adds songs from a file txt to a db"""
from mysql_connection import connection


# Opens txt files with song list
with open("teste_list.txt", "r") as songs_file:
    song_list = songs_file.readlines()

song_list_formatted = []
for song in song_list:
    song_list_formatted.append(song.strip().title())

# MYSQL CONNECTION
myconnection = connection()

# ADDS SONG NAME TO DB
with myconnection:
    with myconnection.cursor() as cursor:
        for song in song_list_formatted:
            sql = f"INSERT INTO ts_songs (name) VALUE ('{song}')"
            cursor.execute(sql)
            myconnection.commit()
