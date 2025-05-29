# Intentionally flawed Python program

# importing modules
import itertools
import random

def card_name(value):
    names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
    return names.get(value, str(value))

# make a deck of cards
deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
    print(f"{card_name(deck[i][0])} of {deck[i][1]}")
