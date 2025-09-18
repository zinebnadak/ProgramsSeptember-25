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



