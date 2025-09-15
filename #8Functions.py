#1 define a function that calculates the biggest of two integers
def biggest(a,b):
    if a>b:
        return a
    if b>a:
        return b

result = biggest(5,9)
print(result)

# 2 Use Bool-type: Define a function that examines if a certain year is a leap year
def leap_year(year):
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

leap_year_input = int(input("Enter a year: "))

answer = leap_year(leap_year_input)
print(answer)

#3 Write a function that counts number of numbers in an integer. Assume the integer is over 0.
# Tip! count number of loops instead of counting the number sum
a = input("Enter a value for integer a: ")

def int_num(a):
    counter = 0     #assign the value inside function or outside but specify it is taken globally.
    for i in a:
        counter = counter +1
    return counter

print(f"The number {a} has {int_num(a)} digit(s).")

#4 The product of Multiplying all whole numbers from n down to 1 is in mathematics called the factorial of the number n.
# The factorial is written as n!. The factorial of 0, i.e. 0!, is defined as 1.
# (For negative numbers, the factorial is not defined.)
# Write a function named n_fac that receives an integer n as a parameter and calculates and returns the value of n!.
# You may assume that n is not negative.
# Also, write a small program that calls the function and prints the result from it.
n = int(input("Enter the value of faqualty 'n': "))

def nfak(n):
    product = 1         #1 is the identity for multiplication.starting from 0 will get you nowhere
    for i in range (1,n+1):     #to get all numbers from 1 to n
        product = product * i
    return product

print (f"Factorial of {n}! is {(nfak(n))}.")

#5 Write a function named is_perfect that determines whether a number was perfect.
# The function should take the number as a parameter and return a value of type bool as the result.
# Insert the function into a complete program that reads a number and tests whether it is perfect.
# sum of all proper divisors of num (excluding itself) == num

num = int(input("Enter a number to see if it is perfect: "))

def perf(num):
    divisors = []
    for i in range (1,num):     #skipping 0 (because dividing by 0 causes an error) and num itself (because we don’t include it for perfect numbers)
        if num % i == 0:
            divisors.append(i)

    if sum(divisors)==num:
        return (f"The number {num} is perfect! ")       #obs! only return the text in a string!
    else:
        return (f"Not a perfect number!")

print (perf(num))#not using print() inside the function — which means you're avoiding None being returned.


#print() outputs text but doesn’t return a value (returns None).
# If you do return print(...), the function will print something but return None.
# Assigning the function call to a variable stores None, not the printed text.

#6 Referenses as parameters
# Write a function that calculates sum of all elements greater than or equal to x in a list or tuple
#1 using list and append
numbers = list(range(1,101))        #list with a hundered positive integers (100 incl) The bigger the list, the more memory it takes. You can’t go to infinity. But make an if statemnet

x = int(input("Enter a positive number (1-100): "))

def summary(x):
    total = []
    for i in numbers:           #obs! you cannont loop over a list: eg. for i in range (numbers)
        if i >= x:
            total.append(i)     #works only with lists
    return sum(total)

# Call the function and print the result
print (f"Sum of numbers >= {x} is {summary(x)}")

#2 using tuples and counter of sum
numbers = tuple(range(1,101))        # can’t be changed!

x = int(input("Enter a positive number (1-100): "))

def summary(x):
    sum = 0
    for i in numbers:           #obs! you cannont loop over a list: eg. for i in range (numbers)
        if i >= x:
            sum = sum +i     #works only with lists
    return sum

# Call the function and print the result
print (f"Sum of numbers >= {x} is {summary(x)}")

#7 Write a new function calculating sum of all elements greater than or equal to x,
# but use list comprehension and standarfunction sum!
numbers = tuple(range(1, 101))  # Could be list or tuple

x = int(input("Enter a positive number (1–100): "))

def summary (numbers, x):      #two parameters (inputs it needs to work). Obs! order matter!
    return sum([i for i in numbers if i >= x])

# Call the function
print(f"Sum of numbers ≥ {x} is {summary(numbers, x)}")

#8 Write a function that calculates average of elements in a sequence of integers.
# Call function two times  at end of program.
# One as a list, another a tuple as parameter.
def average(sequence):
    return sum(sequence)/ len(sequence)

# Example list and tuple
my_list = [10, 20, 30, 40, 50]
my_tuple = (5, 15, 25, 35, 45)

#Call and print
print(f"Average of list: {average(my_list)}")
print (f"Average of tuple: {average(my_tuple)}")


#9 Create functions that simulates a deck of playing cards. It includes:
# Creating a standard 52-card deck as tuples of (suit, rank)
# Shuffling the deck randomly
# Drawing (removing) the top card from the deck
# Displaying a card’s suit and rank in readable form
import random

def new():          #creates a new, shuffeled play of 52 cards represented as tuples (suit, rank).
    play =[]
    for i in range (1,5):       #4 suits
        for j in range (1,14):  #13 ranks
            play.append((i,j))  #add each card as tuple (suit, rank) in the empty list
    random.shuffle(play)        #shuffle the deck of cards
    return play

def give(play):     #give the top card in play of cards
    if len(play) > 0:
        return play.pop()
    else:
        return None     ## Return None if the deck is empty

color = ("♣️", "♦️", "♥️", "♠️")
rank =("E","2","3","4","5","6","7","8","9","10","kn","D","K")

def show(c,last="\n"):      #writes out card "k" in readable format
    f, v = c                #This unpacks the tuple, f is suit index (1–4), v is rank index (1–13), c is a card tuple
    print(color[f-1], rank[v-1], end=last)      #Suits are stored in the color list, Ranks are stored in the rank list. Since Python uses 0-based indexing, we subtract 1. f = 1 → color[0] → gives the first suit (e.g., "♣")

# Create a new shuffled deck
play = new()

# Draw the top card
card = give(play)

# Show the drawn card
show(card)

