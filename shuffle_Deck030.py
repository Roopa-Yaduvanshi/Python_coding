#Python Program to Shuffle Deck of Cards

import random

# define suits and ranks
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

# create deck
deck = []
for suit in suits:
    for rank in ranks:
        deck.append(f"{rank} of {suit}")   

# shuffle the deck
random.shuffle(deck)

print("\nShuffled deck:")
for card in deck:
    print(card)