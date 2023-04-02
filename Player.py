import Card
import Deck
import Uberdeck

class Player:

    def __init__(self):
        self.hand = []
        self.handValue = [0, 0]
        self.aceCount = 0

    def calculateHandValue(self):
        self.handValue = [0, 0]
        for e in self.hand:
            if e.face == "Ace" and self.aceCount < 2:
                # print("Adding " + str(e.face) + " to " + self.handValue.__str__())
                self.aceCount += 1
                self.handValue[0] += e.value[0]
                self.handValue[1] += e.value[1]
                # print(self.handValue)
            else:
                # print("Adding " + str(e.face) + " to " + self.handValue.__str__())
                self.handValue[0] += e.value[0]
                self.handValue[1] += e.value[0]
                # print(self.handValue)

# This main function was used for testing to validated functions
if __name__ == "__main__":
    testPlayer = Player()
    testDeck = Deck.Deck()
    testDeck.shuffle()
    tmp = testDeck.dealOne()
    testPlayer.hand.append(tmp)
    for e in testPlayer.hand:
        print(e)
    testPlayer.calculateHandValue()
    print(testPlayer.handValue)
