"""
Tests Card class
"""
import unittest
from card import Card

class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")
        
    def test_has_suit(self):
        card = Card(rank = "10", suit = "Clubs")
        self.assertEqual(card.suit, "Clubs")        
       
    def test_has_technical_representation(self):
        card = Card(rank = "7", suit = "Spades")
        self.assertEqual(repr(card), "7 of Spades")

    def test_has_value(self):
        card1 = Card(rank = "6", suit = "Clubs")
        card2 = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card1.value, 6)
        self.assertEqual(card2.value, 10)
        
#The following is not needed if run using command line        
if __name__ == "__main__":
    unittest.main()