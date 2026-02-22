## Music Library System - Song Class

This project implements a `Song` class to manage a music library with the following features:

- Track total number of songs.
- Keep a list of unique artists and genres.
- Count how many songs belong to each artist and genre.
- Display individual song info and global library info.

### Example Usage

```python
from lib.song import Song

song1 = Song("Halo", "Beyonce", "Pop")
song2 = Song("Lose Yourself", "Eminem", "Rap")

Song.display_library_info()Total Songs: 2
Artists: ['Beyonce', 'Eminem']
Genres: ['Pop', 'Rap']
Songs per Genre: {'Pop': 1, 'Rap': 1}
Songs per Artist: {'Beyonce': 1, 'Eminem': 1}
---

## **Step 3: Take a Screenshot**

1. Run your test:


python3 -m lib.testing.test_song