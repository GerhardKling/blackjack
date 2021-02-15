"""Main file to execute"""
import random

from card import Card
from deck import Deck



"""Initialize game"""
card1 = Card("7", "Hearts")
card2 = Card("King", "Hearts")
card3 = Card("Ace", "Hearts")

print(card1.rank + " " + card1.suit) 

print(card1)

print(card1.value)

print(card2.value)

print(card3.value)

#Test overwrite property
card3.rank = "1"
print(card3.value)

#Check deck
deck1 = Deck()

print(deck1.cards)

deck1.add_cards(Card)

print(deck1.cards)

print(len(deck1))

#Reshuffle deck
random.shuffle(deck1.cards)
print(deck1.cards)