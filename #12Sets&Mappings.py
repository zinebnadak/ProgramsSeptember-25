#klockan är 6.07 på morgonen hejhej


#1 Write a program that reads two textfiles
# and writes out the words that is common in both files

#compare texts
def create_wordset(f):
    m = set()                   # empty set to store all unique words from file, set removes duplicates auto
    remove = '.,?!:;'           #char thaat is being replaced by " "
    for s in f:                 #go through every row in file
        for c in remove:        #for every character in "remove" (one by one) that char in row
            s = s.replace(c," ")
        s = s.lower()
        word = s.split()        #create list with words on row
        m = m | set(word)       #expand set. m | set(word) is the union of sets — it adds all new words to m without duplicates.converts the list of words from this line into a set.
    return m        #Return the set of words

#Here the execution starts
n1 = input("Enter first filename: ")        #n1 and n2 store the names of the two files to compare
n2 = input("Enter second filename: ")

with open(n1,"r") as f1, open(n2,"r") as f2:
    m1 = create_wordset(f1)     #Calls the function for each file. m1 contains all unique words from file 1. m2 contains all unique words from file 2.
    m2 = create_wordset(f2)
    m = m1&m2       #common words
    print(m)


#2 ---------------------



#3 Run the Python interpreter in interactive mode and create a mapping table that translates the Roman numerals I, V, X, L, C, D, and M into ordinary integers.
# The numerals represent 1, 5, 10, 50, 100, 500, and 1000 respectively.
# Let the search keys be text strings.
# Test different ways of creating the table. Also write expressions that index the table.

#bsclly create a mapping from Roman numerals → integers, using a Python dictionary in interactive mode.
romans = dict(I=1, V=5,X=10,L=50,C=100,D=500,M=1000)        #When you create a dictionary using keyword arguments, like this, Python automatically converts the keywords into strings.So using dict(I=1, ...) or {"I":1, ...} both produce string keys. If you instead used something like romans = {I:1}, without quotes, Python would look for a variable named I, which would give an error
print(romans['I'])  # 1
print(romans['X'])  # 10
print(romans['M'])  # 1000

#OR using zip()
romans = ['I', 'V', 'X', 'L', 'C', 'D', 'M'] #keys
integers = [1, 5, 10, 50, 100, 500, 1000] #values

paired = (zip(romans,integers))       #first keys them values
print(list(paired))
#OR print by using get() - works for both set-formats
roman_to_int = dict(zip(romans, integers))
print(roman_to_int.get("X"))
print(roman_to_int.get('Z', 'Not found'))  # gives 'Not found' if first arg not gives.

#4 write a similar program to the one that compared tvo files and examined which words were common
#but this time just examine one file
#program will print how many times a word is occuring in that file. Program uses tvo Mappings

#Textanalysis
file_name = input("Filename?: ")
with open(file_name,"r") as f:
    d = dict()      #empty mapping
    remove = ".,?!;:"   #string of charachters replaced by " "
    t = str.maketrans(remove, " "* len(remove))         #str.maketrans(x, y): Creates a translation table that can be used with .translate(). x = string of characters to replace, y = string of replacement characters (must be same length as x). " " * len(remove) → creates a string of spaces of the same length as remove
    #so t is now a mapping table that tells Python: replace .,?!;: with spaces.
    for s in f:     #Iterates line by line through the file.
        s = s.translate(t)      #replace all unique char with spaces
        s = s.lower()           #Converts all characters in the string to lowercase
        word = s.split()        #Splits a string into a list of words using whitespace as the default separator.
        for e in word:          #Loops through each word in the list word
            d[e] = d.setdefault(e,0)+1      #dict.setdefault(key, default), this Ensures that each new word starts with count 0. Then adds 1 to increment the count. Can use .get() here too

    for k,v in d.items():            #dict.items(): Returns an iterator of key-value pairs as tuples (key, value)
        print(k,v)

#5 In Pthon you can easiliy store lists and mappings with functions dump and load: that is in a standardmodule named json
# Using json.dump and json.load is the standard way to store Python objects to files and retrieve them later in a simple, human-readable format.

import json

data = {        #Create a dictionary (mapping)
    "name" : "Alice",
    "age": 25,
    "languages": ["Python","Javascript","C++"]
}

with open ("data.json", "w") as file:   #Write (eg. dump) the dictionary to a file
    json.dump(data,file)                # stores the dictionary in JSON format


with open ("data.json", "r") as file:   #Read (eg. load) the dictionary back from the file
    loaded_data = json.load(file)

print(loaded_data)

#6 The Morse alphabet is shown in the following table, where dots and dashes are used to denote short and long signals, respectively.
A .-      B -...    C -.-.    D -..     E .      F ..-.
G --.     H ....    I ..      J .---    K -.-    L .-..
M --      N -.      O ---     P .--.    Q --.-   R .-.
S ...     T -       U ..-     V ...-    W .--    X -..-
Y -.--    Z --..    Å .--.-   Ä .-.-    Ö ---.

# Write a program that reads in a message and translates it into Morse code.
# Then write a program that reads in a message given in Morse code, decodes it, and prints out the message. In the input message, there should be a blank space between each letter.
# bscally: two small Python programs: one for encoding a message into Morse code, and one for decoding Morse code back into text



#encode morse code
text_to_morse = {           # Morse code mapping
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',  'E': '.',    'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',  'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    'Å': '.--.-', 'Ä': '.-.-',  'Ö': '---',
    ' ': '/'                # Use '/' to denote space between words
}
#In your text_to_morse dictionary, you have: 'Ö': '---'  # Ö in Morse, 'O': '---'  # O in Morse. Dictionary cannot have duplicate keys. So '---' now maps to 'Ö', not 'O'. Change by Remove  non-English letters (Å, Ä, Ö) that share Morse codes with standard letters.

# Read message
message = input("Enter a message to encode: ").upper()
# Encode each character
morse_message = ' '.join(text_to_morse[char] for char in message if char in text_to_morse)      #  loop over each character in the string message. if char in text_to_morse only process characters that are keys in the text_to_morse dictionary.  for char in message ... inside ' '.join(...). This is a generator expression, which produces a sequence of Morse code strings for each valid character. ' '.join(list_of_strings) takes all the strings in a list (or generator) and concatenates them into a single string, separated by spaces.
print('Words seperated with "/" Morse code:', morse_message)

print()



#decode morse code
morse_to_text = {v: k for k, v in text_to_morse.items()}        # Create a reverse mapping for decoding
#.items() is a dictionary method that returns key-value pairs as tuples. Each element is (key, value)
# {v: k ...} creates a new dictionary where the keys and values are swapped
# for k, v in text_to_morse.items() is a for loop inside a dictionary comprehension.

morse_input = input("Enter Morse code to decode (use space between letters, / for word space): ")       # Read Morse code message (letters separated by spaces)
letters = morse_input.split(' ')    # Split Morse code into letters
decoded_message = ''.join(morse_to_text.get(code, '?') for code in letters)     # Decode each Morse code symbol

print("Decoded message:", decoded_message)





#7 A company has an inventory with several different types of articles.
# For each type of article, the following information is stored: article designation (a code), article description (a text), number of this item in stock, and sales price.
# Write a program that allows the user to enter information about the inventory into a mapping table where the article designations are the search keys.
# Then let the program store the information in a file using JSON.

# program that allows the user to enter information about the inventory into a mapping table where the article designations are the search keys.
# Then let the program store the information in a file using JSON.

import json

inventory = {}          # Create an empty dictionary to store inventory

while True:             # Loop to input inventory items
    code = input('Enter article code (or "done" to finish): ')
    if code.lower() == "done":        # This is a string method in Python that converts all characters in a string to lowercase. Could be user input like "DONE" or "Done"
        break

    description = input("Enter article description: ")

    while True:             # Make sure stock is stored as an integer
        try:
            stock = int(input("Enter number in stock: "))
            break
        except ValueError:
            print("Please enter a valid integer for stock.")

    while True:             # Make sure price is stored as a float
        try:
            price = float(input("Enter sales price: "))
            break
        except ValueError:
            print("Please enter a valid number for price.")

    inventory[code] = {      # Store item information in dictionary. Using inventory[code] means: “store this item under this unique key.”
        "description": description,
        "stock": stock,
        "price": price
    }

filename = "inventory.json"
with open(filename, "w") as f:    # opens/creates a new file named inventory.json. Use 'f' here
    json.dump(inventory, f, indent=4)  # Use the same variable 'f'

print(f"Inventory saved to {filename}")     #content saved in inventory.json