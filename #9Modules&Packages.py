#dont matter if you use same file name as long as file in dif folder

#1 Write a module you can use for playing the game: "Rock","papper", "scissors".
#The module will have two functions:
# The first will randomly return one of the above values every time you replay
# The second function will have two texts as parameters.
# These texts will contain one of the three values that the first function returns.
# This function will determine who won or if it got equal

#You're not writing a full game loop here — just the logic that can be used inside a game.


import random
play = ["rock", "paper", "scissors"]  #no need to split list

def random_play():                    #Every time it's called, return "rock", "paper", or "scissors" randomly
    return random.choice(play)        #random choice from play

player_1 = random_play()                #call function, assign to variable to use later
player_2 = random_play()


def winner (player_1, player_2):
    if player_1 == player_2:
        return "Its a tie!"

    possible_wins = {       #define a dictionary of possible matches
        "rock":"scissors",
        "rock":"paper",
        "scissors":"paper",
    }

    if possible_wins[player_1]== player_2:      #ex. wins_against["rock"] == "scissors" ,if player 1 is the first of the pairs defines in dic , player 1 is winner
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

#Test
print("Player 1 chose:", player_1)      #print(random_play()) would prints the result but does not assign it to player_1. print() returns None
print("Player 2 chose:", player_2)
print(winner(player_1, player_2))


#2 The game is played by receiving one card at a time, and the player decides whether to take additional cards or not.
# The goal is to get the total card value as close to 21 as possible without going over.
# Aces are counted as either 1 or 14.
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
    return random.choice(deck)


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
        return str(rank)  # to combine a number (2-10) and a string


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
    player_points = []
    computer_points = []


    while True:  # Loop that lets  player play until  stop or bust, and calculate score
        card = get_card()  # get the card
        rank, suit = card  # card is a tuple (rank, suit), extract these before using them.
        player_points.append(get_card_value(rank))  # get the points
        print(f"You drew: {card_name(rank)} {suit} and have {sum(player_points)} points")  # Show sum of player points

        if sum(player_points) > 21:  # if player get  over 21 lose
            print("You busted!")
            break

        answer = input("One more card? (y/n): ")
        if answer != "y":
            break

    if sum(player_points) <= 21:  # if player stays under 21 computer gets another turn
        print("\nComputers turn:")
        while sum(computer_points) < 17:
            card = get_card()
            rank, suit = card
            computer_points.append(get_card_value(rank))
            print(f"Computer drew: {card_name(rank)} {suit} and has {sum(computer_points)} points")

    # determine winner
    if sum(computer_points) > 21:  # if computer gets over 21 player wins
        print("Computer busted! You win! 🎉")
    elif sum(computer_points) > sum(player_points):     # checks this "elif" if computer score less than 21, and computer has higher score than player (still under 21)
        print("Computer wins!")
    elif sum(computer_points) == sum(player_points):
        print("Computer wins! (Tie)")
    else:
        print("You won!")

    # --- Ask to play again ---
    another_round = input("\nPlay again? (y/n): ")
    if another_round.lower() != "y":
        break

print("Thanks for playing! 👋")