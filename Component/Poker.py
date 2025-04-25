from enum import Enum
import random

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
	CF_10 	= 10
	CF_J 	= 11
	CF_Q 	= 12
	CF_K 	= 13
	CF_NUM  = 14

# 花色
class CardSuit(Enum):
	CS_NONE 	= 0
	CS_HEARTS 	= 1 # 红桃
	CS_SPADES 	= 2 # 黑桃
	CS_DIAMONDS	= 3 # 方块
	CS_CLUBS 	= 4 # 梅花
	CS_NUM 		= 5

# 扑克牌
class Poker:
	# def __init__(self):
	# 	self.face = CardFace.CF_NONE
	# 	self.suit = CardSuit.CS_NONE
	# 	self.cal_value()

	def __init__(self, card_face: CardFace, card_suit: CardSuit):
		self.face = card_face
		self.suit = card_suit
		self.__cal_value()

	#　通过牌面计算百家乐中的值
	def __cal_value(self):
		if self.face == CardFace.CF_NONE:
			raise ValueError("Poker must have a valid card face.")
		elif self.face == CardFace.CF_A:
			self.value = 1
			return
		elif self.face == CardFace.CF_2:
			self.value = 2
			return
		elif self.face == CardFace.CF_3:
			self.value = 3
			return
		elif self.face == CardFace.CF_4:
			self.value = 4
			return
		elif self.face == CardFace.CF_5:
			self.value = 5
			return
		elif self.face == CardFace.CF_6:
			self.value = 6
			return
		elif self.face == CardFace.CF_7:
			self.value = 7
			return
		elif self.face == CardFace.CF_8:
			self.value = 8
			return
		elif self.face == CardFace.CF_9:
			self.value = 9
			return
		elif self.face == CardFace.CF_10:
			self.value = 0
			return
		elif self.face == CardFace.CF_J:
			self.value = 0
			return
		elif self.face == CardFace.CF_Q:
			self.value = 0
			return
		elif self.face == CardFace.CF_K:
			self.value = 0
			return
		else:
			raise ValueError("Invalid card face.")

	# 返回百家乐中表示的值
	def get_value(self):
		return self.value

	# 生成一副扑克牌，没有大小王
	def create_pokers():
		pokers = []
		for i in range(1, CardFace.CF_NUM.value):
			for j in range(1, CardSuit.CS_NUM.value):
				pokers.append(Poker(CardFace(i), CardSuit(j)))
		return pokers

	# 生成一张扑克 牌面 + 花色
	def create_poker(card_face: CardFace, card_suit: CardSuit):
		p = Poker(card_face, card_suit)
		return p
	
	# 随机生成一张扑克
	def create_random_poker():
		face = random.randint(1, 13)
		suit = random.randint(1, 4)
		poker = Poker(CardFace(face), CardSuit(suit))
		return poker

