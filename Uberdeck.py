import Deck
import Card
import random
import math

# This class reuses the principle from Deck.py. The uberDeck element is a list of lists of integers. The referenceDeck
# holds all card objects, and is not modified.
class Uberdeck:

    def __init__(self, deckCount):
        self.deckCount = deckCount
        self.referenceDeck = Deck.Deck()
        self.uberDeck = []

        deckNum = 1                         # Counts the number of decks generated
        cycleCount = 0                      # Counts the number of cards generated

        # This loop iterates once for each card in the uberDeck
        for e in range(52*self.deckCount):
            # This statement checks if the loop has complete 1 standard deck, and modifies the counters appropriately.
            if cycleCount > 52:
                deckNum += 1
                cycleCount = 1
            # this encodes the overall card number, the deck number, and the card number in that deck.
            self.uberDeck.append([e+1, deckNum, cycleCount])
            cycleCount += 1

        # The cut point is represented as a plastic card in real games. This creates a count between 20% and 40% of the
        # total uberdeck, and which point the whole thing will need to be reshuffled.
        self.cutPoint = random.randint(math.ceil((52*self.deckCount)*0.20), math.ceil((52*self.deckCount)*0.40))
        print("The deck will be reshuffled when " + str(self.cutPoint) + " cards remain.")

    # Shuffled the uberDeck
    def fullShuffle(self):
        random.shuffle(self.uberDeck)

    # dealX removes x cards from the front of the list. This fully removes those entries, preventing a double draw.
    # Return a Card Object
    def dealX(self, x):
        out = []
        for e in range(0, x):
            temp = self.uberDeck.pop(0)
            out.append(self.referenceDeck.cardList[temp[2]-1])
            temp = None
        return out

    # dealOne removes 1 card from the front of the list. This fully removes than entry, preventing a double draw.
    # Return a Card Object
    def dealOne(self):
        index = self.uberDeck.pop(0)[2]
        tmp = self.referenceDeck.cardList[index-1]
        return tmp

# This main function was used for testing to validated functions
if __name__ == "__main__":
    test = Uberdeck(6)
    #print(test.uberDeck)
    #test.fullShuffle()
    #print(test.uberDeck)
    '''
    tmp = test.dealX(3)
    for e in tmp:
        print(e)
    '''
    print(test.uberDeck)
    deckSize = len(test.uberDeck)
    while deckSize > test.cutPoint:
        tmp = test.dealX(1)
        print(tmp[0])
        # print(test.uberDeck)
        deckSize = len(test.uberDeck)



