
#1 Write a program describing Fibinaccis number sequence, where each number is the sum of the two preceding ones.
n = int (input("How many numbers of fibonacci would you like?: "))

fibonacci_seq= [0,1]       #create new list, start with the two first

for i in range (2,n,1):     #i counts with index
    next_number = fibonacci_seq [i-2]+fibonacci_seq[i-1]    #take the two previous indexes from position "i" and add them
    fibonacci_seq.append(next_number)

print (fibonacci_seq)


#2 Program that will ask user to write words, count how many words user wrote, tell first word and last word
words = input("Enter some words: ").split()

print (f"You wrote {len(words)} words ")
print (f"First word was {words[0]}")        #first
print (f"Last word was {words[-1]}")       #To print the last word, you should access it using the index -1

#3 Write program that read in integres and tell you how many are less than 0
integers = input("Enter some integers: ").split()   #split only work on string

############################################ REP ############################################
integer = [int(i) for i in integers]     # convert each to integer by list comprehension in Python, and the square brackets ([ ]) are used to create a new list.

integers_less_than_zero = []
counter = 0

for num in integer:
    if num<0:
        integers_less_than_zero.append(num)
        counter = counter + 1

############################################ REP ############################################
print (f"Integers less than zero are {counter} :{" , ".join(str(num) for num in integers_less_than_zero)}")     #convert each number to a string and then joins them with commas
# str(num) converts each number to a string.
# ' '.join(...) combines them into one string with spaces (or commas, if you prefer).
# No more [], because we’re printing a formatted string, not the actual list object.

#4 Write a program that creates list with 100 random integers in intervall 1-1000. The program will then print the smallest and biggest number and calculate the two numbers average.
import random

num = [random.randint(1, 1000) for i in range (100)]           #create list with random numbers from 1-1000, let i run over it 100 times

#smallest
min(num)

#biggest
max(num)

#average
average = ((min(num)+max(num))/2)

print (f"List:{" , ".join(str(i) for i in num)}\nSmallest number:{min(num)}\nBiggest number:{max(num)}\nAverage:{average}")

#5 Write a program that reads in a list of integers and removes items that is 0.
# Tip think that there can be multiple items equal to 0
integers = input("Enter some integers: ").split()

int_list = [int(i) for i in integers]
new_l = []      #empty list

for i in int_list:
    if i == 0:
        continue
    new_l.append(i)

print (new_l)

#make code shorter with list comprehension
integers = input("Enter some integers: ").split()
new_l = [int(i) for i in integers if int(i) != 0]
print(new_l)
#It combines:
#A for loop
#An optional if condition
#And the expression for each element you want in the list
#[expression for item in iterable if condition]


#6 create a 10x10 multiplication table
for i in range (1,10+1):        #rows
    for j in range (1,10+1):    #colums
        print (f"{i}x{j}={i*j}\t\t", end="") #print values on same line
    print()

#OR as a Matrix
a = []                      # Step 1: Create an empty list 'a'

for i in range(0, 10):      # Outer loop:(10 iterations). Row i
    a.append([])            # Step 2: begin a new empty list inside list a ,for each outer loop start
    for j in range(0, 10):  # Inner loop: (10 iterations)
        a[i].append((i+1)*(j+1))  # Step 3: Calculate product and append result to row i
print(a)                   # Step 4: Print the final list 'a'

#7 Write a Python program that:
#Asks the user for the total number of prizes to distribute.
#Asks for the number of votes each contestant got.
#Removes contestants who got less than 10% of the total votes.
#Distributes prizes one by one to the contestant with the current highest “score” (score = votes / (prizes already won + 1)).
#Prints how many prizes each contestant gets.

# Ask for number of prizes
prizes = int(input("How many prizes to distribute?: "))

# Ask for number of contestants
num_contestants = int(input("How many contestants: "))
contestants = {}

# Gather all contestants and their votes
for i in range(num_contestants):
    name = input("Enter contestant name: ")
    votes = int(input(f"Enter number of votes for {name}: "))
    contestants[name] = votes       #add to new tuple

# Calculate total votes
total_votes = sum(contestants.values())         #always use name"values" to fetch votes

# Filter contestants who got at least 10% of total votes
winners = {}
for name, votes in contestants.items():
    if votes >= 0.10 * total_votes:
        winners[name] = votes       #add to new tuple

# Initialize prize counter
prizes_won = {name: 0 for name in winners}  #Uses each name in winners as a key,Assigns an initial value of 0 to each key (i.e., no prizes won yet)

# Distribute prizes one-by-one based on score
for p in range(prizes):
    scores = {name: votes / (prizes_won[name] + 1) for name, votes in winners.items()}      #dictionary comprehension, calculating a "score" for each contestant still in the running. Why divide by (prizes_won[name] + 1) - It reduces the score of contestants who have already won prizes, so the next prizes go to people who are under-rewarded.
    winner = max(scores, key=scores.get)        #Finds the name of the contestant with the highest current score. Find the name whose score is the highest
    prizes_won[winner] += 1                     #Add 1 prize to the winner's count. This changes the denominator for that person in the next round, so someone else might win.

# Print final prize distribution
print("Prize distribution:")
for name, count in sorted(prizes_won.items(), key=lambda x: x[1], reverse=True):        #see explanation below
    print(f"{name}: {count}")       #This prints each contestant and how many prizes they got:

# sorted(..., key=lambda x: x[1], reverse=True): This sorts the items based on the number of prizes (the count), from highest to lowest.
#prizes_won.items() : This gives you all the name → count pairs from the dictionary
# key=lambda x: x[1]: Sort by the second item in the tuple (i.e., the count)
# reverse=True: Sort in descending order (highest first)



#8 Write a program that reads a number of integers and prints them out in the same order as they were read.
# When printing, a certain number should only be printed once.
# If the number has already been printed earlier, it should not be printed again.
integers = input("Enter some integers: ").split()       #so that for loop reads one number at a time

integers = [int(i) for i in integers]           #convert to integers and create a list
used_integers = []                              #put used integers inside this list

for i in integers:
    if i not in used_integers:
        used_integers.append(i)

print (used_integers)