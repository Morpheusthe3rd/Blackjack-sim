import Deck
import Card
import Uberdeck
import Player
import sys

class Table:

    def __init__(self, playerCount, deckCount):
        self.uberDeck = Uberdeck.Uberdeck(deckCount) # Blackjack is typically played with 6 decks
        self.playerCount = playerCount
        self.playerList = []
        self.playerList.append(Player.Player()) # The last position on the player list will be the dealer
        self.winners = [[None, None]]*(self.playerCount+1)

        self.winnerFinal = []
        # print("winners.len = " + len(self.winners).__str__())
        for e in range(0,playerCount):
            self.playerList.append(Player.Player())

        # print(self.playerList)

    def printHands(self):
        print("---OPEN")
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
        print("---CLOSED")
        loopCounter = 1
        for e in self.playerList:
            if loopCounter <= self.playerCount:
                print("Player " + str(loopCounter) + " hand: " + str(e.hand) + " Value: " + e.handValue.__str__())
                loopCounter += 1
            else:
                print("Dealer hand: " + str(e.hand[0]) + " [] ")
        print("---")

    def clearHands(self):
        print("Round over. Press 'Enter' to collect hands and re-deal.")
        input()
        for e in self.playerList:
            e.hand = []
        self.winnerFinal = []
        self.winners = [[None, None]]*(self.playerCount+1)

    def checkWinners(self):
        # This statement checks winners
        print()  # Newline
        cycleCount = 1
        for e in self.playerList:
            if cycleCount <= self.playerCount:
                # Select highest hand value < 22
                if e.handValue[1] <= 21:
                    try:
                        print("Player " + cycleCount.__str__() + " total: " + e.handValue[1].__str__())
                        self.winners[cycleCount - 1] = [e.handValue[1], "Player " + cycleCount.__str__()]
                    except(IndexError):
                        print("\n===DIAGNOSTIC ERROR Lines 61-62===\n")
                        print("Index out of bounds: cycleCount = " + str(cycleCount) + " Acceptable range: [0," +
                              len(self.winners).__str__() +"]")
                elif e.handValue[0] <= 21:
                    try:
                        print("Player " + cycleCount.__str__() + " total: " + e.handValue[0].__str__())
                        self.winners[cycleCount - 1] = [e.handValue[0], "Player " + cycleCount.__str__()]
                    except(IndexError):
                        print("\n===DIAGNOSTIC ERROR Lines 69-70===\n")
                        print("Index out of bounds: cycleCount = " + str(cycleCount) + " Acceptable range: [0," +
                              len(self.winners).__str__() +"]")
                else:
                    print("Player " + cycleCount.__str__() + " busted!")
            else:
                if e.handValue[1] <= 21:
                    try:
                        print("Dealer total: " + e.handValue[1].__str__())
                        self.winners[cycleCount - 1] = [e.handValue[1], "Dealer"]
                    except(IndexError):
                        print("\n===DIAGNOSTIC ERROR Lines 80-81===\n")
                        print("Index out of bounds: cycleCount = " + str(cycleCount) + " Acceptable range: [0," +
                              len(self.winners).__str__() + "]")
                elif e.handValue[0] <= 21:
                    try:
                        print("Dealer total: " + e.handValue[0].__str__())
                        self.winners[cycleCount - 1] = [e.handValue[0], "Dealer"]
                    except(IndexError):
                        print("\n===DIAGNOSTIC ERROR Lines 88-89===\n")
                        print("Index out of bounds: cycleCount = " + str(cycleCount) + " Acceptable range: [0," +
                              len(self.winners).__str__() + "]")
                else:
                    print("Dealer busted!")
            cycleCount += 1

        # print(self.winners)
        highestTotal = 0
        NoneType = type(None)

        for i in self.winners:
            newTestValue = i[0]
            if type(newTestValue) == NoneType:
                pass
            else:
                if newTestValue == highestTotal:
                    # handle a tie
                    self.winnerFinal.append(i)
                    highestTotal = newTestValue
                elif newTestValue > highestTotal:
                    self.winnerFinal = []
                    self.winnerFinal.append(i)
                    highestTotal = newTestValue
                else:
                    pass
        # print("Winner list: " + self.winnerFinal.__str__())
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

    def play(self):
        winners = []
        # Deal Cards
            # Deal 1 face up to all
        for e in self.playerList:
            e.hand.append(self.uberDeck.dealOne())
            e.calculateHandValue()
            # Deal 1 face up to players, face down to dealer
        # self.printHands()
        for e in self.playerList:
            e.hand.append(self.uberDeck.dealOne())
            e.calculateHandValue()
        self.printHandsClosed()

        # Check for Natural 21s
        cycleCount = 1
        for e in self.playerList:
            if e.handValue[0] == 21 or e.handValue[1] == 21:
                # Flag winner
                winners.append(cycleCount)
                break
            cycleCount += 1

        # self.printHands()

        if winners != []:

            self.printHands()

            if cycleCount <= self.playerCount+1:
                print("Congradulations Player: " + winners.__str__())
            else:
                print("The Dealer won!")
            self.clearHands()
            return winners

        # Cycle through player turns
        turnOrder = 1
        for e in self.playerList:
            # This statement determines if a "player" is acting, rather than the dealer.
            if turnOrder <= self.playerCount:
                playerinput = ''
                while playerinput.lower() != "stand":
                    if playerinput.lower() == "quit" or playerinput.lower() == "q":
                        print("Quitting game")
                        raise EnvironmentError("Game over")
                    elif e.handValue[0] > 21: # This statement checks if the current player has gone over 21.
                        print("You've gone too far this time!")
                        break

                    playerinput = input("Would you like to stand or hit? >> ")
                    if playerinput.lower() == "hit":
                        tmp = self.uberDeck.dealOne()
                        input("You drew: " + tmp.__str__())
                        e.hand.append(tmp)
                        e.calculateHandValue()
                    self.printHandsClosed()

                print("Player " + turnOrder.__str__() + " is finished.")
                turnOrder += 1
            # This statement handles the Dealers play
            else:
                self.printHands()
                # This first loop will handle the generic case, drawing for the dealer if the highest total
                while e.handValue[1] < 17:
                    tmp = self.uberDeck.dealOne()
                    input("Dealer drew: " + tmp.__str__())
                    e.hand.append(tmp)
                    e.calculateHandValue()
                # This second case handles Aces. If an Ace pushes the total over 21, this takes over.
                if e.handValue[0] < 17 and e.handValue[1] > 21:
                    while e.handValue[0] < 17:
                        tmp = self.uberDeck.dealOne()
                        input("Dealer drew: " + tmp.__str__())
                        e.hand.append(tmp)
                        e.calculateHandValue()

                print("Dealer is finished")

        self.checkWinners()
        self.clearHands()

if __name__ == "__main__":

    sys.argv
    while 1:
        test = Table(int(sys.argv[1]), 6)
        test.uberDeck.fullShuffle()
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

