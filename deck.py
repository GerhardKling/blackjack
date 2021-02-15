"""Defines the Deck class"""
#ERROR line 13: cards need to be stored as their representation to get a list
#Discovered as indexing failed

class Deck():
	def __init__(self):
		self.cards = []

	def add_cards(self, Card):
		SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
		RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
		for suit in SUITS:
			for rank in RANKS:
				card = Card(rank, suit)
				self.cards.append(card)

	def __len__(self):
		return len(self.cards)