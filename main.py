import Deck
import Dealer
import Table
import Turn

if __name__ == '__main__':
	# Set stuff up
	dealer = Dealer.Dealer()
	dealer.welcome()
	table = Table.Table()
	deck = Deck.Deck()
	deck.shuffle()

	initial_deal = True
	
	dealer.letsBegin()

	# Start playing!
	while True:
		if initial_deal:
			# Deal the hands
			dealer.dealHands(deck, table)
			initial_deal = False
			# Check dealer's hand, offer insurance, end the hand
			dealer.printHand()
			table.printHands()
		else:
			# play each player's hand
			# check for b-jacks?
			for player in table.getPlayers():
				dealer.playHand(player, deck)
				dealer.printHand()
				table.printHands()

		





	