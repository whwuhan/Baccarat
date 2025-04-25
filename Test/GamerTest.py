import sys 
sys.path.append("..") 

from Component.Player import *
from Component.Banker import *
from Component.Poker import *

import unittest


class GamerTest(unittest.TestCase):
	def test_gamer(self):
		banker = Banker()
		player = Player()
		banker.hole_cards.append(Poker.create_random_poker())
		player.hole_cards.append(Poker.create_random_poker())
		print(banker.__dict__)
		print(player.__dict__)

if __name__ == "__main__":
	unittest.main()