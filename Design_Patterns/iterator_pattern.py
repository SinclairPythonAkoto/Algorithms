# You are working on a music streaming app and want to implement a playlist feature. 
# The iterator pattern will allow us to create a Playlist class to play all the 
# Song objects.

class Song:
    def __init__(self, title, artist) -> None:
        self.title = title
        self.artist = artist
    

class Playlist:
    def __init__(self) -> None:
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    def __iter__(self):
        return PlaylistIterator(self)


class PlaylistIterator:
    def __init__(self, playlist) -> None:
        self.playlist = playlist
        self.current_index = 0

    def __next__(self):
        if self.current_index >= len(self.playlist.songs):
            raise StopIteration
        else:
            song = self.playlist.songs[self.current_index]
            self.current_index += 1
            return song


playlist: Playlist = Playlist()
playlist.add_song(Song('Calm Waters', 'Purple Cat'))
playlist.add_song(Song('Lost Paradise', 'Purple Cat'))
playlist.add_song(Song('Mellow Vibes', 'Zmeyev'))

for song in playlist:
    print(f'{song.title} by {song.artist}')



# Output
# Calm Waters by Purple Cat
# Lost Paradise by Purple Cat
# Mellow Vibes by Zmeyev