class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level info
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artists_count()

    # Increment total song count
    def add_song_to_count(self):
        Song.count += 1

    # Add genre if unique
    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    # Add artist if unique
    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    # Update count per genre
    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    # Update count per artist
    def add_to_artists_count(self):
        if self.artist in Song.artists_count:
            Song.artists_count[self.artist] += 1
        else:
            Song.artists_count[self.artist] = 1

    # Display info for a single song
    def display_info(self):
        print(f"Song: {self.name}, Artist: {self.artist}, Genre: {self.genre}")

    # Display library-wide info
    @classmethod
    def display_library_info(cls):
        print(f"Total Songs: {cls.count}")
        print(f"Artists: {cls.artists}")
        print(f"Genres: {cls.genres}")
        print(f"Songs per Genre: {cls.genre_count}")
        print(f"Songs per Artist: {cls.artists_count}")