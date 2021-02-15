"""
Tests Player class
"""
import unittest
from player import Player

class PlayerTest(unittest.TestCase):
    def test_has_name(self):
        player = Player('Tom')
        self.assertEqual(player.name, 'Tom')
        
    def test_has_hand(self):
        player = Player('Tom')
        self.assertEqual(player.hand, [])
        
    def test_has_score(self):
        player = Player('Tom')
        self.assertEqual(player.score, 0)

    def test_has_representation(self):
        player = Player('Tom')
        self.assertEqual(repr(player), 'Tom has score 0')

#The following is not needed if run using command line        
if __name__ == "__main__":
    unittest.main()