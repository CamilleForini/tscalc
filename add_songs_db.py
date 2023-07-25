"""This module adds songs from a file txt to a db"""
from dbsqlite_connection import connection, cursor
from functions import *

TABLE_NAME1 = "TS_Songs"
TABLE_NAME2 = "TS_Albuns"


debut_list = openfile("album/debut.txt")
fearless_list = openfile("album/fearless.txt")
speak_now_list = openfile("album/speak_now.txt")
red_list = openfile("album/red.txt")
nineth89_list = openfile("album/1989.txt")
reputation_list = openfile("album/reputation.txt")
lover_list = openfile("album/lover.txt")
folklore_list = openfile("album/folklore.txt")
evermore_list = openfile("album/evermore.txt")
midnights_list = openfile("album/midnights.txt")

albuns = {
    "debut": debut_list,
    "fearless": fearless_list,
    "speak_now": speak_now_list,
    "red": red_list,
    "1989": nineth89_list,
    "reputation": reputation_list,
    "lover": lover_list,
    "folklore": folklore_list,
    "evermore": evermore_list,
    "midnights": midnights_list,
}

for album, album_list in albuns.items():
    for song in album_list:  # ADD SONGS TO TABLE
        data1 = (song, album.title())
        sql1 = f"INSERT INTO {TABLE_NAME1} (name, album) VALUES (?,?)"
        cursor.execute(sql1, data1)
    data2 = (album.title(), len(album_list))
    sql2 = f"INSERT INTO {TABLE_NAME2} (name, n_tracks) VALUES (?,?)"
    cursor.execute(sql2, data2)  # ADD ALBUM TO TABLE

connection.commit()

cursor.close()
connection.close()
