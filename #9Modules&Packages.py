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

#form to play agains computer now! :)


#2 The game is played by receiving one card at a time, and the player decides whether to take additional cards or not.
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


#3 Construct a module, area that contains functions for how to calculate
# areas of, rectangles, circles and triangles

import math
def area_rectangle(lenght, width):
    area = lenght * width
    return area

def area_circle(radius):
    area = math.pi * radius ** 2           #the variable name "area" inside each function can be the same, because each function has its own separate local scope
    return area

def area_triangle (base, height):
    area = (base*height)/2
    return area

while True:
    shape = input("What kind of geometric shape would you like to know area of? ractangle/circle/triangle?: ").lower()

    try:
        if shape == "rectangle":
            lenght = float(input("Enter lenght in cm: "))
            width = float(input("Enter width in cm: "))
            print (f"Area of a rectangle with lenght {lenght}cm and width {width}cm is {area_rectangle(lenght, width):.2f} cm^2")

        elif shape == "circle":
            radius = float(input("Enter radius in cm: "))
            print (f"Area of a circle with radius {radius} cm is {area_circle(radius):.2f} cm^2")

        elif shape == "triangle":
            base = float(input("Enter base in cm: "))
            height = float(input("Enter height in cm: "))
            print (f"Area of a triangle with base {base}cm and height {height}cm is {area_triangle(base, height):.2f}cm^2 ")

        else:
            print("ERROR: Sorry, I don't recognize that shape. Please enter rectangle, circle, or triangle.")

    except ValueError:
        print("ERROR: Please enter valid numbers.")
        continue

        another_area = input("Calculate another shape? y/n: ").lower()
        if another_area == "n":
            break



# 4.Extend the module "CardGame" with a function comp. that can be used when comparing playing cards.
#Comparison Rules:
# Compare suits first using Bridge order:
# Clubs < Diamonds < Hearts < Spades
# (You already have suits as numbers 1–4, so this works directly.)
# If suits are equal, compare ranks.
# Ace (E) should be treated as the highest card (i.e. rank 1 → count it as 14 during comparison).

# Then test your function by writing a program that repeatedly, until the cards run out, draws the top two cards from a shuffled deck.
# The program should compare the two cards and state which one is considered the highest.



import random

def new():          #creates a new, shuffeled play of 52 cards represented as tuples (suit, rank).
    play =[]
    for i in range (1,5):       #4 suits
        for j in range (1,14):  #13 ranks
            play.append((i,j))  #add each card as tuple (suit, rank) in the empty list
    random.shuffle(play)        #shuffle the deck of cards
    return play

def give(play):     #give the top card in play of cards
    if len(play) > 0:       #if there are still cards in deck
        return play.pop()   #return play and remove last item from list and returns it eg. shows it simultaniouly
    else:
        return None     # Return None if the deck is empty

suit = ("♣️", "♦️", "♥️", "♠️")
rank =("E","2","3","4","5","6","7","8","9","10","J","Q","K")

def show(c,last="\n"):      #writes out card "c" in readable format. controls how the print ends. By default, it ends with a newline
    s, r = c                #Unpack tuple c suit index (1–4), rank index (1–13), c is a card tuple where s =1 and r =1
    print(suit[s-1], rank[r-1], end=last)      #Suits are stored in the color list, Ranks are stored in the rank list. Since Python uses 0-based indexing, we subtract 1. f = 1 → color[0] → gives the first suit (e.g., "♣")

#Updated game!
def comp(card_1, card_2):
    suit_1, rank_1 = card_1     #Unpack tuple!
    suit_2, rank_2 = card_2

    rank_1_value = 14 if rank_1 == 1 else rank_1        #treat Ace (rank 1) as 14 for comparison
    rank_2_value = 14 if rank_2 == 1 else rank_2

    if suit_1 > suit_2:         #compare suits first, standard way to represent comparison results returning value (1, -1, or 0) to use them later easier
        return 1                # 1 means first item (card 1) is higher
    elif suit_1 < suit_2:
        return -1               # -1 means second item (card2) is higher
    else:                       # if suits are equal, compare rank values
        if rank_1_value > rank_2_value:
            return 1
        elif rank_1_value < rank_2_value:
            return -1
        else:
            return 0    # cards are equal

# Create a new shuffled deck
play = new()

print ("Welcome to card comparison game 2.0!")

while True:
    if len(play) < 2:       #first check if enough cards in deck to draw two
        print("Not enough cards left to draw two.")
        break

    answer = input("Draw two cards! y/n?: ").lower()
    if answer != "y":
        break

    card_1 = give(play) # Draw the top card
    card_2 = give(play)

    print("You drew: ", end="") #keep cards on same line, show it this way, bcs show(...) prints the card, but returns None
    show(card_1, last=" and ") #last= to keep the last function used end="" bcs end is not a parameter of your function show() — it's a parameter of print(), and need to use print before bcs  if you try to print the function show card you´ll print None
    show(card_2)

    result = comp(card_1, card_2)

    if result == 1:
        print(" → First card is higher!")
    elif result == -1:
        print(" → Second card is higher!")
    else:
        print(" → Both cards are equal!")


