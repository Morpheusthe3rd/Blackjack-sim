import random
import Card

class Deck:
    def __init__(self):

        self.currentOrder = list(range(0,52))
        self.cardList = []
        for e in self.currentOrder:
            #print(e+1)
            tmp = Card.Card(e+1)
            #print(tmp)
            self.cardList.append(tmp)

    def shuffle(self):
        random.shuffle(self.currentOrder)

    def dealX(self, x):
        out = []
        for e in range (0,x):
            #print("e value: ")
            #print(e)
            temp = self.currentOrder.pop(0)
            #print("Card selected: ")
            #print(temp)
            #print(len(self.cardList))
            out.append(self.cardList[temp-1])
            temp = None
        return out

    def dealOne(self):
        return self.cardList[self.currentOrder.pop(0)]

if __name__ == "__main__":
    test = Deck()
    print(test.currentOrder)

    print(test.dealOne())