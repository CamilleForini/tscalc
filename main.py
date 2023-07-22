from mysql_connection import connection

myconnection = connection()
TABLE_NAME = "ts_songs"

song_list = []
with myconnection:
    with myconnection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")

        for row in cursor.fetchall():
            name, album, rank = row
            song_list.append(name)

        for song in song_list:
            new_rank = int(input(f"Digite o rank para a musica {song} "))
            cursor.execute(
                f"UPDATE {TABLE_NAME} SET song_rank='{new_rank}' WHERE name='{song}'"
            )
            myconnection.commit()
