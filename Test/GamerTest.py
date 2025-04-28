import sys
import os
import unittest

'''
__file__:  F:\git_repository\Baccarat\Test\GamerTest.py  脚本的位置
os.path.join(os.path.dirname(__file__), ".." 上层文件夹的绝对路径
'''
# 将上层目录的绝对路径添加到path，方便测试模块引入
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Component.Player import *
from Component.Banker import *
from Component.Poker import *



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