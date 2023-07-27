from dbsqlite_connection import *
from functions import *

# FETCH LIST OF SONGS IN DATABASE
song_list = []
cursor.execute(f"SELECT * FROM {SONG_TABLE}")
for row in cursor.fetchall():
    name, album, rank = row
    song_list.append(name)

# FETCH LIST OF ALBUMS IN DB
album_list = []
cursor.execute(f"SELECT * FROM {ALBUM_TABLE}")
for row in cursor.fetchall():
    name, n_tracks, total, average = row
    album_list.append(name)

songs_ranked = {}
ranks_used = []
"""for song in song_list:
    rank = input(f"Enter the rank of the song {song} ")
    rank_checked = checkrank(rank, song, song_list, ranks_used)
    songs_ranked[rank_checked] = song
    ranks_used.append(rank_checked)
    show_ranked_song(songs_ranked)

for rank, song in songs_ranked.items():  # UPDATE SONGS RANKS
    data1 = (rank, song)
    sql_songs = f"UPDATE {SONG_TABLE} SET rank=(?) WHERE name=(?)"
    cursor.execute(sql_songs, data1)"""
connection.commit()


for album in album_list:  # Updatates total in album
    cursor.execute(f"SELECT * FROM {SONG_TABLE} WHERE album='{album}'")
    for row in cursor.fetchall():
        name, album, rank = row
        cursor.execute(
            f"UPDATE {ALBUM_TABLE} SET total = (total + {rank}) WHERE name='{album}'"
        )
connection.commit()

cursor.execute(f"SELECT * FROM {ALBUM_TABLE}")
for row in cursor.fetchall():
    name, n_tracks, total, average = row
    avarage = total / n_tracks
cursor.close()
connection.close()
