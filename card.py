"""Defines the Card class"""

class Card():
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __repr__(self):
		"""What Python echoes when referring to Card"""
		return f"{self.rank} of {self.suit}"

	@property
	def value(self):
		"""Soft value for Ace"""
		if self.rank == "Ace":
			value = 11
		else:
			try:
				value =  int(self.rank)
			except:
				value = 10
		return value
	