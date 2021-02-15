"""Determines Display class"""
from player import Player
from game import Game
from card import Card
from deck import Deck

class Display():
	def __init__(self):
		print("""
		>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
		>>>>>>>>>>>>>>>>>>> Welcome to Blackjack <<<<<<<<<<<<<
		>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
		>>>>Looks like 1982>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
		""")

	def add_players(self):
		"""Asks for number of players, their names, and returns a list of players"""
		number = input("Enter number of players: ")

		#Check whether integer was entered
		while not number.isdigit():
			print('Please enter an integer')
			number = input("Enter number of players: ")

		#Convert string to integer
		number = int(number)

		if number > 4:
			print('Sorry, the maximum number of players is 4')
			number = 4

		#Ask for players' names and initialize players
		#Organize players in list
		list_players = []

		for idx in range(number):
			name = input(f"Player {idx + 1} please enter your name: ")
			list_players.append(Player(name))
		
		#Add the BANK as the last player
		list_players.append(Player('The BANK'))

		return list_players

	def play_game(self, list_players):
		#Add players to game
		game = Game()
		#Add players
		for player in list_players:
			game.add_player(player)  

		#Call instance method
		game.first_round(Deck, Card)     

		#Show hand for each player
		for player in game.players:
			print(f"\n{player.name} has a {player.hand[0]} and a {player.hand[1]}\n the score is {player.score}\n")

		#Ask for next card
		#The BANK will not be asked for extra cards
		number = len(game.players) - 1
		player_want_cards = number #Default setting at start

		#Game stops if nobody wants more cards
		while player_want_cards > 0:
			for player in game.players[0 : number]:
				#Check whether input is valid
				valid = 1
				while valid == 1:
					#Check whether player is bust
					if player.score > 21:
						answer = 'n'					
					else:
						answer = input(f"{player.name} do you want one more card [y/n]: ")
					if answer == 'y':
						game.next_card(player)
						valid = 0
						print(f"{player.name} received a {player.hand[-1]}.\n Your score is {player.score}")
					if answer == 'n':
						player_want_cards -= 1
						valid = 0
					else:
						valid = 1

		#The BANK takes cards
		while game.players[-1].score < 18:
			game.next_card(game.players[-1])

		#Who wins agains the BANK?
		for player in game.players[0 : number]:
			if player.score > 21:
				print(f"{player.name} is BUST with score {player.score}.")
			elif game.players[-1].score > 21:
				print(f"{player.name} wins with score {player.score}.\n {game.players[-1].name} is BUST with score {game.players[-1].score}.")
			elif player.score > game.players[-1].score:
				print(f"{player.name} wins with score {player.score}.\n {game.players[-1].name} has score {game.players[-1].score}.")
			else:
				print(f"{player.name} has lost with score {player.score}.\n {game.players[-1].name} has score {game.players[-1].score}.")


				


