class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy Birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there."])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

jesses_girl = [
    "Jesse is a friend",
    "He's a good friend of mine"
]

jesses_girl_object = Song(jesses_girl)

print("\n")
happy_bday.sing_me_a_song()

print("\n")
bulls_on_parade.sing_me_a_song()

print("\n")
jesses_girl_object.sing_me_a_song()
print("\n")
