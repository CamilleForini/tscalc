from mysql_connection import connection

myconnection = connection()
TABLE_NAME = "ts_songs"

# FETCH LIST OF SONGS IN DATABASE
song_list = ["False god", "Cornelia Street", "Daylight"]
"""with myconnection:
    with myconnection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        for row in cursor.fetchall():
            name, album, rank = row
            song_list.append(name)"""

ranks_used = []
for song in song_list:
    rank = input(f"Enter the ranking of this song {song}: ")
    rank = int(rank)

    # checks if song rankin is in range
    if rank > len(song_list):
        print(f"Rank out of range, please rank song from 1 to {len(song_list)}")
        rank = int(input(f"Enter the ranking of this song {song}: "))
    if rank in ranks_used:  # checks if rank already used
        print("Rank already used")
        rank = int(input(f"Enter the ranking of this song {song}: "))
    else:
        ranks_used.append(rank)
