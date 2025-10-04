
#The game TwentyOne!
# The game is played by receiving one card at a time, and the player decides whether to take additional cards or not.
# The goal is to get the total card value as close to 21 as possible without going over.
# Aces are counted as either 1 or 14.
# card faces already represent their value 2-10
# Jacks (11), Queens (12) and Kings (13) are all worth 10 points
# If a player exceeds 21, they lose. In this example, a game is simulated between a human player and the computer.
# One card is dealt at a time, and after each round, if the player or the computer ends up with more than 21 points, they are considered to have lost.
# If both the player and the computer have less than 21 points, the one with the higher score wins.
# The computer always wins in case of a tie.

print("Welcome to Twenty-one!")

# deck of cards
suits = ["♥", "♦", "♣", "♠"]  # ['Hearts', 'Diamonds', 'Spades', 'Clubs']
deck = []  # Ranks 2 to 10, Jack (11), Queen (12), King (13), and Ace (1) (we'll include Ace as 1, and later treat it as 1 or 14 in scoring)

# 4 suits X 13 ranks (eg. Ace to King)
for suit in suits:
    for rank in range(1, 14):
        deck.append((rank, suit))  # Each card is a (rank, suit) tuple, tot. 52 cards

import random
def get_card():  # function for drawing a card
    return random.choice(deck)      #returns a tuple (rank, suit)


# Displaying card names (exceptions for Ace, Jacks, Queen and Kings)
def card_name(rank):
    if rank == 1:
        return "A"
    elif rank == 11:
        return "J"
    elif rank == 12:
        return "Q"
    elif rank == 13:
        return "K"
    else:
        return str(rank)  # convert number to string ,to combine a number (2-10) and a string


# Function to assign card’s value
def get_card_value(rank):  # cards 1-14, to count points later
    if rank == 1:
        return random.choice([1, 14])  # Ace is picked randomly , 1 or 14
    elif rank >= 11:
        return 10
    else:
        return rank  # Cards 2–10 return their face value


while True:  # Main game loop to allow multiple rounds
    # start points counter/hands for each round
    player_points = []      #can´t use sum directly on a list
    computer_points = []

    while True:  # Loop that lets player play until stop or bust, and calculate score
        card = get_card()  # get the card, (and first card wo asking)
        rank, suit = card  # unpack! card is a tuple (rank, suit), extract these before using them.
        player_points.append(get_card_value(rank))  # get the points
        print(f"You drew: {card_name(rank)} {suit} and have {sum(player_points)} points")  # Show sum of player points

        if sum(player_points) > 21:  # if player gets over 21, lose
            print("You busted!")
            break

        answer = input("One more card? (y/n): ")        #if not jump here let user choose to cotinue
        if answer != "y":
            break

    if sum(player_points) <= 21:  # start a new if-loop, bcs previous over 21 was not true and player want another card. Now as long as player stays under 21 computer also gets cards
        print("\nComputer's turn:")
        card = get_card()
        rank, suit = card
        computer_points.append(get_card_value(rank))
        print(f"Computer drew: {card_name(rank)} {suit} and has {sum(computer_points)} points")

    # determine winner
    if sum(player_points) > 21:  # if player busts, computer wins
        print("Computer wins!")
    elif sum(computer_points) > 21:  # if computer busts, player wins
        print("Computer busted! You win! 🎉")
    elif sum(computer_points) > sum(player_points):  # both ar now under 21, the ones with higher winns
        print("Computer wins!")
    elif sum(computer_points) == sum(player_points):  # tie goes to computer
        print("Computer wins! (Tie)")
    else:
        print("You won!")

    # --- Ask to play again ---
    another_round = input("\nPlay again? (y/n): ")
    if another_round.lower() != "y":        #converts a string to lowercase, takes both capital and lower cas letters
        break

print("Thanks for playing! 👋")
