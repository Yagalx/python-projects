class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
bday = '''
Happy Birthday to you
Happy Birthday to you 
Happy birthday Hooray'''
happy_bday = Song([bday])

bulls_on_parade = Song(['They rally around tha family',
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()



