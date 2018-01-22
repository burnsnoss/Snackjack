import Player

class Table:
	''' Table - Like a container for players. Keeps track of minimum bet also '''
	players = []
	bet = 0


	def __init__(self):
		# Ask for the minimum bet
		while True: 
			min_bet = raw_input('\nWhat is the minimum bet? --> ')
			if self.checkMinBet(min_bet):
				break
			print 'Please enter a multiple of 5.'
		self.bet = int(min_bet)

		# Ask for the number of players at the table
		while True:
			num_players = raw_input('\nHow many players at the table? --> ')
			if num_players.isdigit() and int(num_players) > 0 and int(num_players) < 8:
				break
			print 'Please enter a number from 1 to 7.'

		# Create players array
		for i in range(int(num_players)):
			player = Player.Player(i, self.bet)
			self.players.append(player)


	def checkMinBet(self, min_bet):
		# Handy check function for minimum bet user inputs
		return min_bet.isdigit() and int(min_bet) >= 5 and int(min_bet) % 5 == 0


	def printTable(self):
		# Prints players array
		print 'Table:'
		for p in self.players:
			p.printPlayer()
		return


	def getPlayer(self, idx):
		return self.players[idx]


	def getPlayers(self):
		return self.players


	def getNumPlayers(self):
		return len(self.players)


	def printHands(self):
		for player in self.players:
			player.printHand()
			print ''
		return


		