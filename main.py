from dbsqlite_connection import *
from functions import *
from classes import *


song_list_obj = []  # LIST OF SONGS OBJECTS
# FETCH LIST OF SONGS IN DATABASE
cursor.execute(f"SELECT * FROM {SONG_TABLE}")
for row in cursor.fetchall():
    name, album, rank = row
    song = Song(name, album)
    song_list_obj.append(song)


albums_list_obj = []  # LIST OF ALBUMS OBJECTS
# FETCH LIST OF ALBUMS IN DB
cursor.execute(f"SELECT * FROM {ALBUM_TABLE}")
for row in cursor.fetchall():
    name, n_tracks, total, average = row
    album = Album(name, n_tracks)  # CREATES AN ALBUM OBJECT
    albums_list_obj.append(album)


songs_ranked = []
ranks_used = []
for song in song_list_obj:
    rank = input(f"Enter the rank of the song {song.get_name()} ")
    rank_checked = checkrank(rank, song, song_list_obj, ranks_used)
    song.set_rank(rank_checked)
    songs_ranked.append(song)
    ranks_used.append(rank_checked)
    show_ranked_song(songs_ranked)

for album in albums_list_obj:
    for song in songs_ranked:
        if song.get_album() == album.get_name():
            album.update_soma(song.rank)
        else:
            continue

show_ranked_albums(albums_list_obj)


for song in songs_ranked:  # UPDATE SONGS RANKS
    data1 = (song.rank, song.name)
    sql_songs = f"UPDATE {SONG_TABLE} SET rank=(?) WHERE name=(?)"
    cursor.execute(sql_songs, data1)
connection.commit()


for album in albums_list_obj:
    data = (album.get_soma(), album.get_media())
    sql = f"UPDATE {ALBUM_TABLE} SET total = (?), avarage = (?) WHERE name='{album.get_name()}'"
    cursor.execute(sql, data)


connection.commit()

cursor.close()
connection.close()
