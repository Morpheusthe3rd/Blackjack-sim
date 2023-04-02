import Deck
import Card
import random
import math

class Uberdeck:

    def __init__(self, deckCount):
        self.deckCount = deckCount
        self.referenceDeck = Deck.Deck()
        self.uberDeck = []

        deckNum = 1
        cycleCount = 0
        for e in range(52*self.deckCount):
            if cycleCount > 52:
                deckNum += 1
                cycleCount = 1
            self.uberDeck.append([e+1, deckNum, cycleCount])
            cycleCount += 1

        self.cutPoint = random.randint(math.ceil((52*self.deckCount)*0.20), math.ceil((52*self.deckCount)*0.40))
        # testing
        ## self.cutPoint = len(self.uberDeck) - 5
        print("The deck will be reshuffled at: ")
        print(self.cutPoint)

        # print(self.uberDeck)
    def fullShuffle(self):
        random.shuffle(self.uberDeck)

    def dealX(self, x):
        out = []
        #print(len(self.uberDeck))
        for e in range(0, x):
            temp = self.uberDeck.pop(0)
            #print(temp[2])
            #print(self.referenceDeck.cardList[temp[2]-1])
            out.append(self.referenceDeck.cardList[temp[2]-1])
            temp = None
        return out

    def dealOne(self):
        index = self.uberDeck.pop(0)[2]
        # print("Index for dealt card: " + index.__str__())
        tmp = self.referenceDeck.cardList[index-1]
        # print(tmp)
        return tmp


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



