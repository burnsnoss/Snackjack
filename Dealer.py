import time

class Dealer:
	''' Dealer - Keeps track of the deck and the game '''
	turn = 0
	rounds = 0
	hand = []
	cardTotal = 0


	def __init__(self):
		pass


	def welcome(self):
		print '\n --- W E L C O M E   T O   S N A C K J A C K ---\n'
		time.sleep(1)
		print ' DEALER:'
		print '\t"Hello! I am your dealer."'
		print '\t"Let\'s get some info first."'


	def letsBegin(self):
		print ''
		print ' DEALER:'
		print '\t"Let\'s begin!"'
		print ''
		return


	def deal(self, deck, player, num_cards = 1):
		for i in range(num_cards):
			player.receiveCard(deck.popCard())
		return


	def dealHands(self, deck, table):
		# Deals two cards to everyone
		print ' DEALER:'
		print '\t"Dealing hands..."'
		print ''

		for i in range(2):
			for j in range(table.getNumPlayers()):
				player = table.getPlayer(j)
				self.deal(deck, player)
			self.deal(deck, self)
		self.turn = 0
		self.rounds += 1
		return


	def receiveCard(self, card):
		self.hand.append(card)
		return


	def playHand(self, player, deck):
		# Print and notify player of his/her turn
		print ' DEALER:'
		print '\t"It is ' + player.getName() + '\'s turn!"'
		while True:
			user_input = raw_input('\t"Hit, stay, double, or split?" --> ')
			if self.checkUserInput(user_input, True):
				break
			print 'Please enter hit, stay, double, split, help, or quit.'

		if user_input == 'hit':
			self.deal(deck, player)
			# check for bust?
		elif user_input == 'stay':
			return 
		elif user_input == 'double':
			pass
		elif user_input == 'split':
			pass
		elif user_input == 'help':
			pass
		elif user_input == 'quit':
			exit()

		self.printHand()
		player.printHand()

		while True:
			while True:
				user_input = raw_input('\t"Hit or stay?" --> ')
				if self.checkUserInput(user_input):
					break
				print 'Please enter hit, stay, help, or quit.'

			if user_input == 'hit':
				self.deal(deck, player)
				# check for bust?
			elif user_input == 'stay':
				return
			elif user_input == 'help':
				pass
			elif user_input == 'quit':
				exit()

			self.printHand()
			player.printHand()


	def sweepCards(self, table):
		self.setHand([])
		for player in table.getPlayers():
			player.setHand([])
		return


	def checkUserInput(self, ui, all_opts = False):
		ui = ui.lower()
		if all_opts:
			return ui == 'hit' or ui == 'stay' or ui == 'split' or ui == 'double' or ui == 'quit' or ui == 'help'
		else:
			return ui == 'hit' or ui == 'stay' or ui == 'quit' or ui == 'help'


	def setHand(self, new_hand):
		self.hand = new_hand
		self.totalHand()
		return


	def getHand(self):
		return self.hand


	def showCards(self):
		print ' DEALER:'
		print '\t"Now, I will reveal my hand."'
		print ''
		self.printHand(False)
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


	def betsPlease(self, table):
		pass
		# for player in table.getPlayers():



	def payout(self, table):
		pass


	def printHand(self, hidden = True):
		print ' DEALER:'
		first_card = True
		for card in self.getHand():
			if first_card and hidden:
				print '\tHIDDEN CARD'
				first_card = False
			else:
				card.printCard()
		if not hidden:
			print '\tTotal: ' + str(self.totalHand())
		print ''
		return
