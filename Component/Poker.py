from enum import Enum

# 牌面和对应的数值
class CardFace(Enum):
	CF_NONE	= 0
	CF_A 	= 1
	CF_2 	= 2
	CF_3 	= 3
	CF_4 	= 4 
	CF_5 	= 5
	CF_6 	= 6 
	CF_7 	= 7 
	CF_8 	= 8 
	CF_9 	= 9
	CF_10 	= 0 
	CF_J 	= 0 
	CF_Q 	= 0  
	CF_K 	= 0

# 花色
class CardSuit(Enum):
	CS_NONE 	= 0
	CS_HEARTS 	= 1 # 红桃
	CS_SPADES 	= 2 # 黑桃
	CS_DIAMONDS	= 3 # 方块	
	CS_CLUBS 	= 4 # 梅花

# 一张扑克牌
class Poker:
	def __init__(self):
		self.face = CardFace.CF_NONE
		self.suit = CardSuit.CS_NONE
