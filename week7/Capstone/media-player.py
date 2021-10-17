import random
# This module implements pseudo-random number generators for various distributions


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist

    def __str__(self):
        return self.title + " by " + self.artist

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))

    def __en__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))

    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))


class Playlist:
    def __init__(self):
        self._tracks = []

    def push(self, track):
        self._tracks.append(track)

    def pop(self):
        try:
            return self._tracks.pop()
        except IndexError:
            print("Song Removed")

    def __len__(self):
        return len(self._tracks)

    def __repr__(self):
        return f"Playlist({self._tracks})"

queue = Playlist()
track1 = Song("Love & Hate", "Michael Kiwanuka")
track2 = Song("Fake Plastic Trees", "Radiohead")
track3 = Song("Feel It All Around", "Washed Out")
track4 = Song("Take Me Home, Country Roads", "John Denver")
track5 = Song("It Was A Good Day", "Ice Cube")
queue.push(track1)
queue.push(track2)
queue.push(track3)
queue.push(track4)
queue.push(track5)

def menu():
    print(20 * "-", "MENU", 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")


while True:
    menu()
    choice = int(input())

    if choice == 1:
        # prompts user for song title, artist name & add song to playlist
        print("New song added to playlist")
    elif choice == 2:
        # prompts user for song title & remove song from playlist
        print("Song removed from playlist")
    elif choice == 3:
        # play playlist from beginning & displays song title that is playing
        print("Playing...")
    elif choice == 4:
        # skips to next song on playlist & displays current song
        print("Skipping...")
    elif choice == 5:
        # go back to previous song on playlist & displays current song
        print("Replaying...")
    elif choice == 6:
        # randomly shuffles song, plays first song & displays name of song
        print("Shuffling...")
    elif choice == 7:
        # display song title and artist currently playing
        print("Currently playing: ", end=" ")
    elif choice == 8:
        # Shows the current title list order
        print("\nSong list:\n")
    elif choice == 0:
        print("Goodbye.")
        break
