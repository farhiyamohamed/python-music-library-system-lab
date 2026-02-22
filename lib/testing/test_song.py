from lib.song import Song

# Create song objects
song1 = Song("Halo", "Beyonce", "Pop")
song2 = Song("Single Ladies", "Beyonce", "Pop")
song3 = Song("Numb", "Linkin Park", "Rock")
song4 = Song("In the End", "Linkin Park", "Rock")
song5 = Song("Lose Yourself", "Eminem", "Rap")

# Display individual songs
song1.display_info()
song3.display_info()

# Display overall library info
Song.display_library_info()
