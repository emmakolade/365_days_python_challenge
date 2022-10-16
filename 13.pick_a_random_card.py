import random

cards = ["Diamonds", "Spades", "Hearts", "Clubs"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace" ]

def Random_Card():
	card = random.choices(cards)
	rank = random.choices(ranks)
	return(f"the {rank} of {card}")

print(Random_Card())