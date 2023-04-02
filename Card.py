class Card:
	#The Card class contains all information on any particular card.
	def __init__(self, code):
		self.code = code
		#This extensive switch statement will simplify all card creation elsewhere, at the
		#expense of complexity here.
		#This can be reformatted into a if elif without much difficulty
		if self.code == 1:
			self.face = "Ace"
			self.value = [1, 11]
			self.suit = "Hearts"
		elif self.code == 2:
			self.face = "2"
			self.value = [2]
			self.suit = "Hearts"
		elif self.code == 3:
			self.face = "3"
			self.value = [3]
			self.suit = "Hearts"
		elif self.code == 4:
				self.face = "4"
				self.value = [4]
				self.suit = "Hearts"
		elif self.code == 5:
				self.face = "5"
				self.value = [5]
				self.suit = "Hearts"
		elif self.code == 6:
				self.face = "6"
				self.value = [6]
				self.suit = "Hearts"
		elif self.code == 7:
				self.face = "7"
				self.value = [7]
				self.suit = "Hearts"
		elif self.code == 8:
				self.face = "8"
				self.value = [8]
				self.suit = "Hearts"
		elif self.code == 9:
				self.face = "9"
				self.value = [9]
				self.suit = "Hearts"
		elif self.code == 10:
				self.face = "10"
				self.value = [10]
				self.suit = "Hearts"
		elif self.code == 11:
				self.face = "Jack"
				self.value = [10]
				self.suit = "Hearts"
		elif self.code == 12:
				self.face = "Queen"
				self.value = [10]
				self.suit = "Hearts"
		elif self.code == 13:
				self.face = "King"
				self.value = [10]
				self.suit = "Hearts"
		elif self.code == 14:
				self.face = "Ace"
				self.value = [1, 11]
				self.suit = "Diamonds"
		elif self.code == 15:
				self.face = "2"
				self.value = [2]
				self.suit = "Diamonds"
		elif self.code == 16:
				self.face = "3"
				self.value = [3]
				self.suit = "Diamonds"
		elif self.code == 17:
				self.face = "4"
				self.value = [4]
				self.suit = "Diamonds"
		elif self.code == 18:
				self.face = "5"
				self.value = [5]
				self.suit = "Diamonds"
		elif self.code == 19:
				self.face = "6"
				self.value = [6]
				self.suit = "Diamonds"
		elif self.code == 20:
				self.face = "7"
				self.value = [7]
				self.suit = "Diamonds"
		elif self.code == 21:
				self.face = "8"
				self.value = [8]
				self.suit = "Diamonds"
		elif self.code == 22:
				self.face = "9"
				self.value = [9]
				self.suit = "Diamonds"
		elif self.code == 23:
				self.face = "10"
				self.value = [10]
				self.suit = "Diamonds"
		elif self.code == 24:
				self.face = "Jack"
				self.value = [10]
				self.suit = "Diamonds"
		elif self.code == 25:
				self.face = "Queen"
				self.value = [10]
				self.suit = "Diamonds"
		elif self.code == 26:
				self.face = "King"
				self.value = [10]
				self.suit = "Diamonds"
		elif self.code == 27:
				self.face = "Ace"
				self.value = [1, 11]
				self.suit = "Clubs"
		elif self.code == 28:
				self.face = "2"
				self.value = [2]
				self.suit = "Clubs"
		elif self.code == 29:
				self.face = "3"
				self.value = [3]
				self.suit = "Clubs"
		elif self.code == 30:
				self.face = "4"
				self.value = [4]
				self.suit = "Clubs"
		elif self.code == 31:
				self.face = "5"
				self.value = [5]
				self.suit = "Clubs"
		elif self.code == 32:
				self.face = "6"
				self.value = [6]
				self.suit = "Clubs"
		elif self.code == 33:
				self.face = "7"
				self.value = [7]
				self.suit = "Clubs"
		elif self.code == 34:
				self.face = "8"
				self.value = [8]
				self.suit = "Clubs"
		elif self.code == 35:
				self.face = "9"
				self.value = [9]
				self.suit = "Clubs"
		elif self.code == 36:
				self.face = "10"
				self.value = [10]
				self.suit = "Clubs"
		elif self.code == 37:
				self.face = "Jack"
				self.value = [10]
				self.suit = "Clubs"
		elif self.code == 38:
				self.face = "Queen"
				self.value = [10]
				self.suit = "Clubs"
		elif self.code == 39:
				self.face = "King"
				self.value = [10]
				self.suit = "Clubs"
		elif self.code == 40:
				self.face = "Ace"
				self.value = [1, 11]
				self.suit = "Spades"
		elif self.code == 41:
				self.face = "2"
				self.value = [2]
				self.suit = "Spades"
		elif self.code == 42:
				self.face = "3"
				self.value = [3]
				self.suit = "Spades"
		elif self.code == 43:
				self.face = "4"
				self.value = [4]
				self.suit = "Spades"
		elif self.code == 44:
				self.face = "5"
				self.value = [5]
				self.suit = "Spades"
		elif self.code == 45:
				self.face = "6"
				self.value = [6]
				self.suit = "Spades"
		elif self.code == 46:
				self.face = "7"
				self.value = [7]
				self.suit = "Spades"
		elif self.code == 47:
				self.face = "8"
				self.value = [8]
				self.suit = "Spades"
		elif self.code == 48:
				self.face = "9"
				self.value = [9]
				self.suit = "Spades"
		elif self.code == 49:
				self.face = "10"
				self.value = [10]
				self.suit = "Spades"
		elif self.code == 50:
				self.face = "Jack"
				self.value = [10]
				self.suit = "Spades"
		elif self.code == 51:
				self.face = "Queen"
				self.value = [10]
				self.suit = "Spades"
		elif self.code == 52:
				self.face = "King"
				self.value = [10]
				self.suit = "Spades"
		else:
			raise ValueError("Card ID is beyond acceptable values (0:52 inclusive)")
			pass
	def __str__(self):
		return self.face + " of " + self.suit

	def __repr__(self):
		return self.face + " of " + self.suit



if __name__ == "__main__":
	test = Card(1)
	print(test)