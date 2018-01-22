class Card:
	''' Card - class with name, suit, and value attributes that represents a playing card. '''

	def __init__(self, new_name, new_suit):
		if not self.cardCheck(new_name):
			print 'Error: Invalid card name'
			exit()
		if not self.suitCheck(new_suit):
			print 'Error: Invalid suit'
			exit()
		self.name = new_name
		self.suit = new_suit
		self.value = self.getValue()


	def getValue(self, ace_one = False):
		if self.name == 'A' and ace_one:
			return 1
		elif self.name == 'A' and not ace_one:
			return 11
		elif self.name.isdigit():
			return int(self.name)
		else:
			return 10


	def cardCheck(self, card):
		card_names = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
		if card not in card_names:
			return False
		return True


	def suitCheck(self, suit):
		suit_names = ['Spades','Hearts','Clubs','Diamonds']
		if suit not in suit_names:
			return False
		return True


	def printCard(self):
		print '\t' + self.name + ' ' + self.suit
		return