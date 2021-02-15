"""
Tests Deck class
"""
import unittest
from deck import Deck
from card import Card

class DeckTest(unittest.TestCase):
    def test_has_no_cards(self):
        deck = Deck()
        self.assertEqual(deck.cards, [])

    def test_adding_cards(self):
        deck = Deck()
        deck.add_cards(Card)
        card1 = Card('2', 'Clubs')
        card2 = Card('Ace', 'Spades')
        self.assertEqual(deck.cards[0].rank, card1.rank)
        self.assertEqual(deck.cards[-1].rank, card2.rank)        

    def test_len_function(self):
        deck = Deck()
        deck.add_cards(Card) 
        self.assertEqual(len(deck), 52)       

        
#The following is not needed if run using command line        
if __name__ == "__main__":
    unittest.main()