import random
import Card

# This class is structured to have 2 lists: currentOrder and cardList. currentOrder is a list of numbers, 0-51. These
# are the indices of the card in the cardList. currentOrder is randomized as the shuffle, and then the indices are
# removed and referenced against the cardList. cardList is never re-ordered.
class Deck:
    def __init__(self):
        self.currentOrder = list(range(0,52))

        # This creates and populates the card list
        self.cardList = []
        for e in self.currentOrder:
            tmp = Card.Card(e+1)
            self.cardList.append(tmp)

    def shuffle(self):
        random.shuffle(self.currentOrder)

    # dealX removes x cards from the front of the list. This fully removes those entries, preventing a double draw.
    # Return a Card Object
    def dealX(self, x):
        out = []
        for e in range (0,x):
            temp = self.currentOrder.pop(0)
            out.append(self.cardList[temp-1])
            temp = None
        return out

    # dealOne removes 1 card from the front of the list. This fully removes than entry, preventing a double draw.
    # Return a Card Object
    def dealOne(self):
        return self.cardList[self.currentOrder.pop(0)]

# This main function was used for testing to validated functions
if __name__ == "__main__":
    test = Deck()
    print(test.currentOrder)

    print(test.dealOne())