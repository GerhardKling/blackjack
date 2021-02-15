"""
Tests Game class
"""
import unittest
from game import Game
from player import Player
from deck import Deck
from card import Card

class PlayerTest(unittest.TestCase):
    def test_has_players(self):
        game = Game()
        self.assertEqual(game.players, [])

    def test_adds_player(self):
        player = Player('Tom')
        game = Game()
        #Call instance method
        game.add_player(player)
        self.assertEqual(game.players, [player])

    def test_gives_cards_to_players(self):
        player1 = Player('Tom')
        player2 = Player('Sue')
        game = Game()
        #Add players
        game.add_player(player1)  
        game.add_player(player2)
        #Call instance method
        game.first_round(Deck, Card)  
        #Test whether each player has two cards
        self.assertEqual(len(player1.hand), 2)
        self.assertEqual(len(player2.hand), 2)  

    def test_scores_added(self):     
        player1 = Player('Tom')
        player2 = Player('Sue')
        game = Game()
        #Add players
        game.add_player(player1)  
        game.add_player(player2)
        #Call instance method
        game.first_round(Deck, Card) 
        self.assertEqual(player1.score, game.scores[0])
        self.assertEqual(player2.score, game.scores[1])

    def test_deck_updated_after_first_round(self):
        player1 = Player('Tom')
        player2 = Player('Sue')
        game = Game()
        #Add players
        game.add_player(player1)  
        game.add_player(player2)
        #Call instance method
        game.first_round(Deck, Card) 
        self.assertEqual(len(game.deck), 48)

#The following is not needed if run using command line        
if __name__ == "__main__":
    unittest.main()