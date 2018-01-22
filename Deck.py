import Card
import random

class Deck:
	''' Deck - a container for cards. The number of decks determines when to re-shuffle '''
	deck = []
	num_decks = 0

	def __init__(self):
		# Ask for number of decks to use
		while True:
			new_num = raw_input('\nHow many decks? --> ')
			if self.checkNumberOfDecks(new_num):
				break
			print 'Please enter a number from 2 to 100.'
		self.num_decks = int(new_num)

		# Generate this number of decks
		for i in range(int(new_num)):
			new_deck = self.generateNewDeck()
			for card in new_deck:
				self.deck.append(card)


	def checkNumberOfDecks(self, new_num):
		# Handy check for number of decks input by user
		return new_num.isdigit() and int(new_num) >= 2 and int(new_num) <= 100


	def generateNewDeck(self):
		# Makes a fresh deck, in order 2-A and spd-hrt-clb-dia
		card_names = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
		suit_names = ['Spades','Hearts','Clubs','Diamonds']
		deck = []
		for card in card_names:
			for suit in suit_names:
				deck.append(Card.Card(card, suit))
		return deck


	def shuffle(self):
		# Shuffles the entire deck by doing random switcheroonies
		for i in range(len(self.deck)):
			# Switch this card with a random card
			j = random.randint(0, len(self.deck)-1)
			tmp_card = self.deck[j]
			self.deck[j] = self.deck[i]
			self.deck[i] = tmp_card
			# Switch two random cards
			j = random.randint(0, len(self.deck)-1)
			k = random.randint(0, len(self.deck)-1)
			tmp_card = self.deck[k]
			self.deck[k] = self.deck[j]
			self.deck[j] = tmp_card
		return


	def reshuffle(self):
		# Shuffles in the middle of a game
		#  Resests the deck to freshly shuffled, no cards missing
		self.deck = []
		for i in range(self.num_decks):
			new_deck = self.generateNewDeck()
			for card in new_deck:
				self.deck.append(card)

		self.shuffle()


	def printDeck(self):
		# Prints each card + num left in deck
		for card in self.deck:
			card.printCard()
		print 'Number of cards:', len(self.deck)
		return


	def getNumDecks(self):
		return self.num_decks


	def getNumRemainingCards(self):
		return len(self.deck)


	def popCard(self):
		return self.deck.pop(0)

