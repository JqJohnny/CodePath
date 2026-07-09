class SongNode:
    def __init__(self, song, next=None):
        self.song = song
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()
        
# top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

bad_romance = SongNode("Bad Romance")
party_rock_anthem = SongNode("Party Rock Anthem", bad_romance)
top_hits_2010s = SongNode("Uptown Funk", party_rock_anthem)

print_linked_list(top_hits_2010s)