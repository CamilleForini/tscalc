class Album:
    def __init__(self, name, n_tracks):
        self.name = name
        self.soma = 0
        self.media = 0.0
        self.length = n_tracks

    def get_name(self):
        return self.name

    def update_soma(self, n):
        self.soma += n

    def get_media(self):
        self.media = self.soma / self.length
        return self.media

    def get_soma(self):
        return round(self.soma, 2)


class Song:
    def __init__(self, name, album):
        self.name = name
        self.album = album
        self.rank = 0

    def set_rank(self, rank):
        self.rank = rank

    def get_name(self):
        return self.name
