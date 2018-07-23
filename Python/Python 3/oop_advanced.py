# #
# oop_advanced.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 23/07/2018
#
# #

# Inheritance
# Class method - viewed but not used
# Abstract method - see abc {import abc}
# Dunder methods
# Iterable
# Duck typing
# MRO - viewed but not used
# Multiple inheritance - viewed but not used
# Mixins - seen but not used

# Python Data Model
# Initialization : __init__
# Representation : __str__, __repr__
# Containers     : __contains__, __iter__, __len__, __getitem__
# Numericals     : __add__, __sub__, __mul__, __mod__

#from abc import ABC # Abstract Base Classes

class Program:

	def __init__(self, name, year):
		self._name = name.title()
		self.year = year
		self._likes = 0

	@property
	def likes(self):
		return self._likes

	def like(self):
		self._likes += 1

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	def __str__(self):
		return f'Name: {self.name} - Year: {self.year} - Likes: {self.likes}'

	def __repr__(self):
		return f'Program(name=\'{self.name}\', year={self.year}, likes={self.likes})'


class Movie(Program):

	def __init__(self, name, year, duration):
		super().__init__(name, year)
		self.duration = duration

	def __str__(self):
		return f'Name: {self.name} - Year: {self.year} - Likes: {self.likes} - Duration: {self.duration}'

	def __repr__(self):
		return f'Movie(name=\'{self.name}\', year={self.year}, likes={self.likes}, duration={self.duration})'

class Series(Program):

	def __init__(self, name, year, seasons, episodes):
		super().__init__(name, year)
		self.seasons = seasons
		self.episodes = episodes

	def __str__(self):
		return f'Name: {self.name} - Year: {self.year} - Likes: {self.likes} - Seasons: {self.seasons} - Episodes: {self.episodes}'

	def __repr__(self):
		return f'Series(name=\'{self.name}\', year={self.year}, likes={self.likes}, seasons={self.seasons}, episodes={self.episodes})'


class Playlist():

	def __init__(self, name, programs):
		self.name = name.title()
		self._programs = programs

	def __repr__(self):
		return f'Playlist(name=\'{self.name}\', {repr(self._programs)})'

	def __getitem__(self, item):
		return self._programs[item]

	def __len__(self):
		return len(self._programs)
	
	@property
	def playlist(self):
		return self._programs


def main():

	avengers = Movie('avengers infinity war', 2018, 160)
	atlanta = Series('atlanta', 2018, 2, 16)
	game_of_thrones = Series("game of thrones", 2011, 7, 68)
	simpsons = Movie('simpsons the movie', 2007, 90)

	avengers.like()
	atlanta.like()
	atlanta.like()
	game_of_thrones.like()
	game_of_thrones.like()
	game_of_thrones.like()

	weekend = Playlist('Weekend playlist', [avengers, atlanta, game_of_thrones, simpsons])

	print("\nPlaylist size: {}\n".format(len(weekend)))

	for program in weekend:
		print(program)

	print("\n\nRepresentations: \n")

	for program in weekend:
		print(repr(program))

	print(f'\n\nIs infinity war in the list? {avengers in weekend}')

	print('\n\nPlaylist representation:')
	print(f'\n{repr(weekend)}')


if __name__ == '__main__':
	main()