"Module with functions that are used internally"


def openfile(filename):
    """Opens a file and returns a list of lines formatted"""
    with open(filename, "r") as songs_file:
        song_list = songs_file.readlines()
    song_list_formatted = []  # format song list
    for song in song_list:
        song_list_formatted.append(song.strip().title())
    return song_list_formatted


def checkrank(rank, song, song_list, ranks_used):
    """Checks the rank of a given song and returns a valid rank"""
    rank = rank
    while True:
        if rank.isdigit():
            rank_int = int(rank)
        else:
            print("Invalid rank, please enter only numbers")
            rank = input(f"Please enter a rank to rank this song {song} ")
            continue

        if rank_int > len(song_list):
            print(f"Rank out of range, expecting value between 1 and {len(song_list)}")
            rank = input(f"Please enter a rank to rank this song {song} ")
            continue
        elif rank_int in ranks_used:
            print("Rank already used")
            rank = input(f"Please enter a rank to rank this song {song} ")
            continue
        else:
            break
    return rank_int


def show_ranked_song(songs_ranked):
    """Shows ranks songs in crescent order"""
    ranked_songs_formatted = []

    for rank, song in songs_ranked.items():
        ranked_songs_formatted.append(f"{rank}º - {song}")

    for song_ranked in sorted(ranked_songs_formatted):
        print(song_ranked)
