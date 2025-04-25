from Component.Poker import *
from Component.Banker import *
from Component.Player import *

# 百家乐游戏
class Baccarat:
	def __init__(self):
		self.pokers_num = 8 # 生成几副牌
		self.poker_pool = []
		for i in range(8):
			pass

class BaccaratGameMode:
	def __init__(self):
		pass
	
	# 输入闲家，庄家，判断游戏结果
	def get_game_result(player: Player, banker: Banker):
		pass