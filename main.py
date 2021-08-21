class Track:

    def __init__(self, song, artiste):
        self.name = song
        self.artiste = artiste
        self.timesplayed = 0

    def get_artiste(self):
        return self.artiste

    def get_name(self):
        return self.name

    def play(self):
        self.timesplayed += 1
        return self

    def __str__(self):
        music_track = "{} {} {}".format(self.name, self.artiste, self.timesplayed)
        return music_track


class DLLNode:
    def __init__(self, previous_node=None, music_track=None, next_node=None):
        self.prev = previous_node
        self.music_track = music_track
        self.next = next_node

class Pytoonz:

    def __init__(self):
        self.list_size = 0
        self.head = DLLNode(None, None, None)
        self.tail = DLLNode(self.head, None, None)
        self.list_pointer = None
        self.head.next = self.tail

    def __str__(self):
        item = self.head.next
        playlist = "Playlist: \n"
        if self.list_size == 0:
            playlist += str(None)
            return playlist
        else:
            j = 0
            while j < self.list_size:
                if item == self.list_pointer:
                    playlist += "-->"
                playlist += str(item.music_track) + "\n"
                item = item.next
                j += 1
            return playlist

    def length(self):
        return self.list_size

    def get_current(self):
        if self.list_size == 0:
            return None
        else:
            return self.list_pointer.track

    def add_track(self, track):
        new_track = DLLNode(None, track, None)
        self.list_pointer = self.head.next
        if self.head.next is self.tail:
            new_track.prev = self.head
            new_track.next = self.tail
            self.head.next = new_track
            self.tail.prev = new_track
        else:
            current_track = self.head
            while current_track.next is not self.tail:
                current_track = current_track.next
            current_track.next = new_track
            new_track.prev = current_track
            new_track.next = self.tail
        self.list_size += 1

    def add_after(self, track, track_before):
        current = self.head
        new_track = DLLNode(None, track, None)
        while current:
            if current.next is self.tail and current.music_track == track_before:
                self.add_track(track)
            elif current.music_track is track_before:
                after_node = current.next
                current.next = new_track
                new_track.next = after_node
                new_track.prev = current
                after_node.prev = new_track
            current = current.next

    def next_track(self):
        if self.list_pointer.next is self.tail:
            self.list_pointer = self.head.next
        else:
            self.list_pointer = self.list_pointer.next

    def prev_track(self):
        if self.list_pointer.prev is self.head:
            self.list_pointer = self.tail.prev
        else:
            self.list_pointer = self.list_pointer.prev

    def reset(self):
        if self.list_pointer is not self.head.next:
            self.list_pointer = self.head.next

    def play(self):
        play = "Playing: "
        if self.list_size > 0:
            if self.list_pointer is not self.head or self.tail:
                return play + str(Track.play(self.list_pointer.track))
        else:
            print("There is no songs in your playlist to play")

    def remove_current(self):
        if self.list_size == 1:
            self.head.next = self.tail
            self.tail.prev = self.head
            self.list_size = 0
        elif self.list_size > 1:
            if self.list_pointer.next is not self.tail:
                before_node = self.list_pointer.prev
                after_node = self.list_pointer.next
                before_node.next = after_node
                after_node.prev = before_node
                self.list_size -= 1
        elif self.list_pointer.next is self.tail:
            before_node = self.list_pointer.prev
            before_node.next = self.tail
            self.tail.prev = before_node
            self.list_size -= 1
        else:
            return None
        self.pointer = self.list_pointer.next



def main():
    DLL_Test= Pytoonz()

    track1 = Track("Dreams", "Fleetwood Mac")
    track2 = Track("Billie Jean", "Michael Jackson")
    track3 = Track("Don't Stop Believin", "Journey")
    track4 = Track("Every Breath You Take", "The Police")
    track5 = Track("Bohiemian Rapspody", "Queen")

    Track.play(track1)
    Track.play(track1)
    Track.play(track1)
    Track.play(track2)
    Track.play(track2)
    Track.play(track3)
    Track.play(track3)
    Track.play(track4)
    Track.play(track5)

    DLL_Test.add_track(track1)
    DLL_Test.add_track(track2)
    DLL_Test.add_track(track3)
    DLL_Test.add_track(track4)
    DLL_Test.add_track(track5)

    print(DLL_Test)

    DLL_Test.prev_track()
    print(DLL_Test)

    DLL_Test.next_track()
    print(DLL_Test)
    DLL_Test.next_track()
    print(DLL_Test)
    DLL_Test.prev_track()
    print(DLL_Test)



if __name__ == '__main__':
    main()
