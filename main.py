"""
Main file to execute
Video for rules of blackjack: https://www.youtube.com/watch?v=qd5oc9hLrXg
"""
import random

from card import Card
from deck import Deck
from game import Game
from player import Player
from display import Display



"""Initialize game"""

#Start display
display = Display()

#Add players
list_players = display.add_players()

#Play game
display.play_game(list_players)





