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

#form to play against computer now! :)

#2. MODULE TwentyOne.py


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

#----------------------- this definition will be used in TwentyOne 2.0
def new():          #creates a new, shuffeled play of 52 cards represented as tuples (suit, rank).
    play =[]
    for i in range (1,5):       #4 suits
        for j in range (1,14):  #13 ranks
            play.append((i,j))  #add each card as tuple (suit, rank) in the empty list
    random.shuffle(play)        #shuffle the deck of cards
    return play
#-----------------------

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


