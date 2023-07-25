"Module with functions that are used internally"


def openfile(filename):
    """Opens a file and returns a list of lines formatted"""
    with open(filename, "r") as songs_file:
        song_list = songs_file.readlines()
    song_list_formatted = []  # format song list
    for song in song_list:
        song_list_formatted.append(song.strip().title())
    return song_list_formatted
