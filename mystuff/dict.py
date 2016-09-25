class Song(object):
	def __init__(self,lyrics):
		self.lyrics=lyrics
	def sing_me_a_song (self):
		for line in self.lyrics:
			print(line)


happy_bady=Song(["Happy birthday to you","I don't want to get sued","So I'll stop right there"])
happy_bady.sing_me_a_song()