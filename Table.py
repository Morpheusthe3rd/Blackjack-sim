import Deck
import Card
import Uberdeck
import Player
import sys

class Table:

    def __init__(self, playerCount, deckCount):
        self.uberDeck = Uberdeck.Uberdeck(deckCount) # Blackjack is typically played with 6 decks
        self.playerCount = playerCount               # Players are unlimited
        self.playerList = []                         #
        self.playerList.append(Player.Player())      # The last position on the player list will be the dealer
        self.winners = [[None, None]]*(self.playerCount+1) # This list is used for tracking victor calculations
        self.winnerFinal = []                              # This is where the winner is stored

        # populate the player list with Player objects
        for e in range(0,playerCount):
            self.playerList.append(Player.Player())

    # This function reveals all cards of all players, including the dealer
    def printHands(self):
        print("---")
        loopCounter = 1
        for e in self.playerList:
            if loopCounter <= self.playerCount:
                print("Player " + str(loopCounter) + " hand: " + str(e.hand) + " Value: " + e.handValue.__str__())
                loopCounter += 1
            else:
                print("Dealer hand: " + str(e.hand) + " Value: " + e.handValue.__str__())
        print("---")

    # This function will be used to hide the dealers second card until their turn
    def printHandsClosed(self):
        print("---")
        loopCounter = 1
        for e in self.playerList:
            if loopCounter <= self.playerCount:
                print("Player " + str(loopCounter) + " hand: " + str(e.hand) + " Value: " + e.handValue.__str__())
                loopCounter += 1
            else:
                print("Dealer hand: " + str(e.hand[0]) + " [] ")
        print("---")

    # This function runs at the end of each round to reset variables for the next
    def clearHands(self):
        print("Round over. Press 'Enter' to collect hands and re-deal.")
        input()
        for e in self.playerList:
            e.hand = []
        self.winnerFinal = []
        self.winners = [[None, None]]*(self.playerCount+1)

    # This function iterates through the players to calculate and display final scores.
    def checkWinners(self):

        print()  # Newline for CLI cleanliness
        cycleCount = 1 # This counts the number of cycles the loop goes through, and stands in for Player number.

        # This loop determines and prints everyone's playable score, or if they busted.
        for e in self.playerList:               # This operates on all players, including dealer

            if cycleCount <= self.playerCount:  # This checks that we are dealing with a player

                # This if-elif-else block checks the 2 hand values for <= 21. If neither are, this posts a bust message
                # It also populates the 'winners' list, with the player number and their hand value
                if e.handValue[1] <= 21:
                    print("Player " + cycleCount.__str__() + " total: " + e.handValue[1].__str__())
                    self.winners[cycleCount - 1] = [e.handValue[1], "Player " + cycleCount.__str__()]
                elif e.handValue[0] <= 21:
                    print("Player " + cycleCount.__str__() + " total: " + e.handValue[0].__str__())
                    self.winners[cycleCount - 1] = [e.handValue[0], "Player " + cycleCount.__str__()]
                else:
                    print("Player " + cycleCount.__str__() + " busted!")
            else:
                if e.handValue[1] <= 21:
                    print("Dealer total: " + e.handValue[1].__str__())
                    self.winners[cycleCount - 1] = [e.handValue[1], "Dealer"]
                elif e.handValue[0] <= 21:
                    print("Dealer total: " + e.handValue[0].__str__())
                    self.winners[cycleCount - 1] = [e.handValue[0], "Dealer"]
                else:
                    print("Dealer busted!")
            cycleCount += 1

        # This section calculates the winner, reducing the list to 1 (or 2 in case of a tie)

        highestTotal = 0        # tracking variable
        NoneType = type(None)   # comparison variable for detecting busted players (which are [None, None])

        for i in self.winners:
            newTestValue = i[0] # for comparison to highestTotal
            if type(newTestValue) == NoneType:      # Will pass if current player busted
                pass
            else:
                if newTestValue == highestTotal:    # This section handles a tie
                    self.winnerFinal.append(i)
                    highestTotal = newTestValue
                elif newTestValue > highestTotal:   # This determines if the new player did better than the last one
                    self.winnerFinal = []
                    self.winnerFinal.append(i)
                    highestTotal = newTestValue
                else:                               # This is the case that the previous player had a higher total
                    pass

        # The final print for the victor.
        if len(self.winnerFinal) == 0:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("All players Busted, no winners")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif len(self.winnerFinal) > 1:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Tie! " + self.winnerFinal.__str__())
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Winner: " + self.winnerFinal.__str__())
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # This function manages the initial deal of cards to begin the round
    def dealCards(self):
        # Deal Cards

        # Deal 1 face up to all
        for e in self.playerList:
            e.hand.append(self.uberDeck.dealOne())
            e.calculateHandValue()

        # Deal 1 face up to players, face down to dealer
        for e in self.playerList:
            e.hand.append(self.uberDeck.dealOne())
            e.calculateHandValue()
        self.printHandsClosed()

        # Check for Natural 21s. If any player (or dealer) starts with an Ace and Face, the round immediately ends.
        for e in self.playerList:
            if e.handValue[0] == 21 or e.handValue[1] == 21:
                self.checkWinners()
                self.clearHands()
                return

    # This is the main statement, and runs a round of the game.
    def play(self):
        winners = []
        self.dealCards()

        # Cycle through player turns
        turnOrder = 1
        for e in self.playerList:
            # This statement determines if a "player" is acting, rather than the dealer.
            if turnOrder <= self.playerCount:
                playerinput = ''                        # resets player input

                # This loop represents a single players turn. Player input is received in the middle of the loop, after
                # initial checks.
                while playerinput.lower() != "stand":

                    if playerinput.lower() == "quit" or playerinput.lower() == "q": # exit case
                        print("Quitting game")
                        raise EnvironmentError("Game over")
                    elif e.handValue[0] > 21:           # This statement checks if the current player has gone over 21.
                        print("You've gone too far this time! You're busted.") # Bust statement
                        break

                    playerinput = input("Would you like to stand or hit? >> ")  # Any input besides hit goes to the top
                                                                                # of the next loop.
                    if playerinput.lower() == "hit":
                        tmp = self.uberDeck.dealOne()           # Draws a card
                        input("You drew: " + tmp.__str__())     # Shows card, requires Enter to progress
                        e.hand.append(tmp)                      # Adds card to hand
                        e.calculateHandValue()                  # Recalculates hand value
                    self.printHandsClosed()                     # Prints current hand

                print("Player " + turnOrder.__str__() + " is finished.")
                turnOrder += 1

            # This statement handles the Dealers play. Dealer has automated rules.
            else:
                self.printHands()

                # This first loop will handle the generic case, drawing for the dealer if the highest total < 17
                while e.handValue[1] < 17:
                    tmp = self.uberDeck.dealOne()
                    # Dealer draws also require manual check, to improve readability
                    input("Dealer drew: " + tmp.__str__())
                    e.hand.append(tmp)
                    e.calculateHandValue()

                # This second case handles Aces. If an Ace pushes the total over 21, this takes over.
                if e.handValue[0] < 17 and e.handValue[1] > 21:
                    while e.handValue[0] < 17:
                        tmp = self.uberDeck.dealOne()
                        # Dealer draws also require manual check, to improve readability
                        input("Dealer drew: " + tmp.__str__())
                        e.hand.append(tmp)
                        e.calculateHandValue()

                print("Dealer is finished")

        self.checkWinners()
        self.clearHands()

if __name__ == "__main__":

    while 1:                                    # This loop will handle multiple games
        test = Table(int(sys.argv[1]), 6)       # This creates the Table
        test.uberDeck.fullShuffle()             # This shuffles the deck

        # This loop will run rounds of the game until the deck needs to be reshuffled.
        while len(test.uberDeck.uberDeck) > test.uberDeck.cutPoint:
            test.play()

        print("Deck needs to be reshuffled.")
        input = input("Play again?(y/n) >> ")

        if input == "n":
            print("Quitting game")
            raise EnvironmentError("Game over")
        else:
            del(test)
            pass

