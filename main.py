from dbsqlite_connection import *
from functions import *

# FETCH LIST OF SONGS IN DATABASE
song_list = ["August", "Seven", "Clean", "ME", "Foolish One"]
"""cursor.execute(f"SELECT * FROM {SONG_TABLE}")
for row in cursor.fetchall():
    name, album, rank = row
    song_list.append(name)"""


songs_ranked = {}
ranks_used = []
for song in song_list:
    rank = input(f"Enter the rank of the song {song} ")
    rank_checked = checkrank(rank, song, song_list, ranks_used)
    songs_ranked[rank_checked] = song
    ranks_used.append(rank_checked)

for rank, song in songs_ranked.items():
    print(rank, "-", song)
cursor.close()
connection.close()
