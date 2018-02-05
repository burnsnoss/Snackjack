import Deck
import Dealer
import Table


if __name__ == '__main__':
	# Set stuff up, initialize dealer, table, and deck
	dealer = Dealer.Dealer()
	dealer.welcome()
	table = Table.Table()
	deck = Deck.Deck()
	deck.shuffle()

	# Keeps track of number of hands played
	num_hands = 0
	# Keeps track of initial deal or not
	initial_deal = True

	# Start playing!
	dealer.letsBegin()
	while True:
		if initial_deal:
			# Increment number of hands played
			num_hands += 1
			# Ask for bets
			dealer.betsPlease(table)
			# Deal the hands
			dealer.dealHands(deck, table)
			# Check dealer's hand, offer insurance, end the hand
			dealer.printHand()
			table.printHands()

			initial_deal = False
		else:
			# play each player's hand
			# check for b-jacks?
			for player in table.getPlayers():
				dealer.playHand(player, deck)
				dealer.printHand()
				table.printHands()

			dealer.showCards()

			# Payout, take cards
			dealer.payout(table)
			dealer.sweepCards(table)

			initial_deal = True

		if num_hands % 2 == 0 and num_hands > 0:
			# i
			break

		





	