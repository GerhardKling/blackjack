"""Determines Game class"""
import random

class Game():
	def __init__(self):
		self.players = []
		self.scores = []
		self.deck = []

	def add_player(self, player):
		"""Button to add one player at a time"""
		self.players.append(player)

	def first_round(self, Deck, Card):
		#Initialize deck
		deck = Deck()
		#Add cards to deck
		deck.add_cards(Card)
		#Reshuffle deck
		random.shuffle(deck.cards)

		#Check whether we have at least one player
		#Give first two cards to players
		if len(self.players) > 0:
			for _ in range(2):
				for player in self.players:
					#Gives the first card to player
					#Remove card from deck
					card = deck.cards.pop(0)
					player.hand.append(card)
					player.score += card.value
		else:
			print('Add players to start game')

		#Update deck on game instance as we need to use it for next round
		self.deck = deck.cards

		#Store scores in list
		for player in self.players:
			#Address special case: Player has two Aces
			if player.score == 22: 
				player.hand[0].rank = "Ace-1" #Take first Ace as "1"
				player.score = 12 #Set score to 12 = 11 + 1
			#Add player's score to game scores
			self.scores.append(player.score)

	def next_card(self, player):
		#Remove card from deck
		card = self.deck.pop(0)
		player.hand.append(card)
		player.score += card.value

		if player.score > 21:
			for card in player.hand:
				if card.rank == 'Ace':
					card.rank = 'Ace-1'
					player.score -= 10
					break




			



