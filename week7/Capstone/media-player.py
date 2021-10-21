from queue import Queue
import random

class Song():
    def __init__(self,title,artist):
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
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))

class Playlist:
    def __init__(self, currentSongIndex=0, currentlyPlaying=False):
        self.items = []
        self.setCurrentSongIndex(currentSongIndex)
        self.setCurrentlyPlaying(currentlyPlaying)

    def setCurrentSongIndex(self, index):
        self.currentSongIndex = index

    def setCurrentlyPlaying(self, currentlyPlaying):
        self.currentlyPlayingOne = currentlyPlaying

    def addSong(self, song):
        if self.size() > 0:
            self.items.insert(self.size() + 1, song)
        else:
            self.items.insert(0, song)

    def size(self):
        return len(self.items)

    def play(self, song_index):
        self.currentSongIndex = song_index
        
        self.setCurrentlyPlaying(True)
        
        print("\nPlaying....")

        print(self.items[self.currentSongIndex])

    def displayPlaylist(self):
        num = 1

        print("\nSong List:\n")

        for item in self.items:
            print(str(num) + '. ' + str(item))
            num += 1

    def current(self):
        if self.currentlyPlayingOne:
            print("\nCurrently Playing:")

            print(self.items[self.currentSongIndex])
        else:
            print('\nNothing is Playing!')

    def next(self):
        if self.currentlyPlayingOne:
            playlistLength = len(self.items) - 1

            if self.currentSongIndex == playlistLength:
                next_song = 0
            else:
                next_song = self.currentSongIndex + 1

            print("\nSkipping....")

            self.play(next_song)
        else:
            print('\nNothing is Playing!')

    def prev(self):
        if self.currentlyPlayingOne:
            playlistLength = len(self.items) - 1
            
            if self.currentSongIndex == 0:
                prev_song = playlistLength
            else:
                prev_song = self.currentSongIndex - 1

            print("\nReplaying....")
            
            self.play(prev_song)
        else:
            print('\nNothing is Playing!')

    def delete(self, title):
        song_index = 0

        for item in self.items:
            if item.title == title:
                break   
            song_index += 1

        self.items.pop(song_index)
        
    def shuffle(self):
        listLength = self.size()
        
        for i in range(listLength):
            # pop off the first element and append it to the end of the list
            firstNumber = self.items.pop(0)
            self.items.append(firstNumber)
            
            # generate a random number based on the size of the list
            randomNumber = random.randint(0, listLength - 1)

            # pop off that random element and append to the end of the list
            listElement = self.items.pop(randomNumber)
            self.items.append(listElement)

# Main Menu 
def menu():
    print('\n')
    print(20 * "-" , "MENU" , 20 * "-")
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
    print('\n')
    
mediaPlayer = Playlist()

# main list
mediaPlayer.addSong(Song("Love & Hate", "Michael Kiwanuka"))
mediaPlayer.addSong(Song("Fake Plastic Trees", "Radiohead"))
mediaPlayer.addSong(Song("Sweet Home Alabama", "Lynyard Skynard"))
mediaPlayer.addSong(Song("Take Me Home, Country Roads", "John Denver"))
mediaPlayer.addSong(Song("Feel It All Around", "Washed Out"))
mediaPlayer.addSong(Song("It Was A Good Day", "Ice Cube"))


# Media Player
while True:
    menu()
    choice = int(input())

    if choice == 1:
        artist = input('Enter an Artist: ')
        title = input('Enter a Title: ')
        # Prompts user to input Songs Title and Artist Name

        song = Song(title=title, artist=artist)
        mediaPlayer.addSong(song)
        # Adds song to playlist
        
        print("New Song: " + song.title + " Added to Playlist")
        
    elif choice == 2:
        title = input('Enter the Song Title to be Removed: ')
        # Ask user to enter for Song Title 
        mediaPlayer.delete(title)
        # Removes the user song input from playlist
        print("Song: " + title + " Removed from Playlist")

    elif choice == 3:
        mediaPlayer.play(0)
        # Displays song name that's playing
        
    elif choice == 4:
        mediaPlayer.next()
        # Skips to the next song
        
    elif choice == 5:
        mediaPlayer.prev()
        # Back to previous song

    elif choice == 6:
        mediaPlayer.shuffle()
        print("Shuffling....")
        mediaPlayer.displayPlaylist()
        mediaPlayer.play(0)
        # Shuffles the playlist and play the first song

    elif choice == 7:
        mediaPlayer.current()
        #  Song name & artist of the currently song

    elif choice == 8:
        mediaPlayer.displayPlaylist()
        # Displays list order

    elif choice == 0:

        print("Goodbye.")
        break