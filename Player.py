class Player:
	'''
		Player - keeps track of each players hand and bank
			attributes: hand, split_hand, bank, name, position
	'''

	def __init__(self, i, min_bet):
		# Set position at table
		self.position = i + 1

		# Say hello
		print '\nHello, Player' + str(self.position) + '!'

		# Ask for the player's name
		while True:
			new_name = raw_input('What is your name? --> ')
			# Check to make sure it's not too long
			if len(new_name) <= 18:
				break
			print 'That name is too long.'
		self.name = new_name

		# Ask how much money the player's got
		while True:
			new_bank = raw_input('How much money do you have? --> ')
			# Check that its not bad input
			if self.checkNewBank(new_bank, min_bet):
				break
			print 'Bank must be at least the minimum bet.'
		self.bank = new_bank

		self.hand = []
		self.split_hand = []
		self.cardTotal = 0


	def checkNewBank(self, new_bank, min_bet):
		# Handy check function for checking user input for bank
		return new_bank.isdigit() and int(new_bank) > 0 and int(new_bank) >= min_bet


	def printPlayer(self):
		# Prints player's name and bank
		print 'Player' + str(self.position) + ': ' + self.name + '\tBank: ' + str(self.bank)


	def receiveCard(self, card):
		self.hand.append(card)
		self.totalHand()
		return


	def totalHand(self):
		# Initialize card total to zero
		self.cardTotal = 0

		# First iterate through cards, skipping aces
		for card in self.getHand():
			if card.getName() == 'A':
				continue
			else:
				self.cardTotal += card.getValue()

		# Then iterate through cards and add in aces
		for card in self.getHand():
			if card.getName() == 'A' and self.cardTotal > 10:
				self.cardTotal += card.getValue(True)
			elif card.getName() == 'A':
				self.cardTotal += card.getValue()

		return self.cardTotal


	def getName(self):
		return self.name


	def getHand(self):
		return self.hand


	def setHand(self, new_hand):
		self.hand = new_hand
		return


	def printHand(self):
		print ' ' + self.name + ':'
		for card in self.hand:
			card.printCard()
		print '\tTotal: ' + str(self.totalHand())
		return



