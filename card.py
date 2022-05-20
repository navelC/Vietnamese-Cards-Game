class Card:
	def __init__(self, num, suit):
		self.num = num
		self.suit = suit
	def __eq__(self, other):
		if (isinstance(other, Card)):
			return self.num == other.num and self.suit == other.suit
		return False
	def show(self):
		return str(self.num)+"-"+str(self.suit)
	def convertSuit(self):
		s = self.suit
		if s == 1: return "s"
		if s==2: return "c"
		if s==3: return "d"
		return "h"
		
	def convertNum(self):
		n = self.num
		if n == 15: return "2"
		if n==14: return "1"
		return n
	def convert(self):
		return str(self.convertNum())+str(self.convertSuit())
	