"""
Determines Player class
"""

class Player():
	def __init__(self, name):
		self.name = name
		self.hand = []
		self.score = 0

	def __repr__(self):
		return f"{self.name} has score {self.score}"