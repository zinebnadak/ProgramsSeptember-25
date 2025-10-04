#used for TwentyOne 2.0 or other card games


import random

def new():
    """Creates a new, shuffled deck of 52 cards as (suit, rank) tuples."""
    play = []
    for i in range(1, 5):       # 4 suits
        for j in range(1, 14):  # 13 ranks
            play.append((i, j))
    random.shuffle(play)
    return play

def give(play):
    """Give (pop) the top card from the deck."""
    if len(play) > 0:
        return play.pop()
    else:
        return None

suit = ("♣", "♦", "♥", "♠")
rank = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

def show(card, last="\n"):
    """Print a card in readable format."""
    s, r = card
    print(suit[s - 1], rank[r - 1], end=last)


