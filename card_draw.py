# Intentionally flawed Python program

# importing modules
import itertools
import random

def card_name(value):
    """Return the string name for a card value."""
    names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
    return names.get(value, str(value))

def main():
    SUITS = ['Spade', 'Heart', 'Diamond', 'Club']
    VALUES = range(1, 14)
    CARDS_TO_DRAW = 5

    # Create and shuffle the deck
    deck = list(itertools.product(VALUES, SUITS))
    random.shuffle(deck)

    # Draw cards
    print("You got:")
    for i in range(min(CARDS_TO_DRAW, len(deck))):
        print(f"{card_name(deck[i][0])} of {deck[i][1]}")

if __name__ == "__main__":
    main()
