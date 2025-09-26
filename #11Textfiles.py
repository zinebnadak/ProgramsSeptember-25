#1 Write a functios "open" that describes a certain file (ex. T.py) a
# let user write in a files name
# opens file
# prints the contents line by line

name = input("Name of the file: ")
f = open(name,'r')      #first parameter to function open is name of file, then what to do and file type (default is "r" to read the file), then optionally how the file weare handling is coded.
for row in f:
    print(row,end="")   # Prints each line without adding extra newline
f.close()               # Closes the file

#2 Write a program that copies the contents of a file to a new file.
# Then program will print our number of rows and characters copied to the new file
print()
print()
file_name = input("File name you want to copy: ")
new_file = input ("New file name: ")

file_1 = open (file_name, "r")
file_2 = open (new_file, "w")   #opens file to write mode to use .write
r,c = 0,0                       #multiple assignment, also called tuple unpacking. Initializes two counters: r: Number of rows (lines) copied and c: Number of characters copied.
for row in file_1:                # do something with EACH ROW/LINE. Iterates over each line in the source file. (basically reads the file but row by row)
    c = c+ file_2.write(row)    # overall .write() returns the number of characters it wrote. .write(row) means write the string stored in row
    r = r+1                     #Increments the line counter r by 1 for each row copied
print(f"{r} rows and {c} characters copied to new file {new_file}")
file_1.close()
file_2.close()                  #Closes both files to free up system resources

#3 Write a program that reads in a number of names from the keyboard and saves the entered names into a text file called personer.txt.
# In the text file, there should be one name on each line.
# If the file with that name already exists, it should not be overwritten; instead, the new names should be added at the end of the file.
# Run the program twice and add some names each time.
# Before you run the program the first time, make sure that no file named personer.txt exists.
# After each run, you can use a text editor to see what is in the file personer.txt.
print("Enter names one at a time. Press Enter without typing a name to exit!: ")

with open("persons.txt","a") as f:      #this opens (or creates) a file named personer.txt, If it does exist, the behavior depends on the mode you use next, "a" stands for append. This mode adds new content to the end of the file. "as f" assigns that file object to the variable f
    while True:
        name = input("Enter name: ")
        if name == "":
            break   #Stop when input is empty
        f.write(name+"\n")

print("Names are saved to 'persons.txt'.")



#4 Write a program that reads in a text file containing a Python program.
# The program should ask for the file’s name.
# The program should examine which lines in the file contain comments.
# For simplicity, assume that the only comments are those of the type starting with #.
# The program should then print out what percentage of the lines in the file contain comments.
name = input("Enter filename: ")

comments = 0
total_lines = 0
with open (name,"r")as f:    #reads file
    for row in f:             #for every row
        total_lines = total_lines+1
        if "#" in row:        # not if row == "#". This checks if the entire line is exactly "#", which is almost never true.
            comments = comments +1

comment_percentage = (comments/total_lines) *100

print (f"File {name} has {total_lines} lines, and {comments} comments {comment_percentage} % are comments.")

#5 write a *script that reads a file with student results from an input (results.txt) and writes the names of students who passed (scored 50 or more points) to a new file (named passed.txt). The name of this new file is determined by another input

file_results = input("Enter name of file with results:")       #enter student_results
new_file_name = input ("choose name for *new file with students who passed: ")

with (open(file_results,"r")as file_1,open(new_file_name,"w")as file_2):        #Opens two files: file_results → opened for reading and new_file_name → opened for writing. The "with" statement ensures both files are properly closed after the block finishes (even if there's an error). file_results and new_file_name are strings (file names), and file_1 and file_2 are file objects that you can actually read from or write to
    for row in file_1:
        row = row.strip(' \n')      #This makes sure you don’t accidentally include unwanted spaces or newlines when processing or writing the line.
        i = row.rfind(" ")          #Finds the position of the last space in the line, Because the score is expected to come after the last space.
        points = int(row[i+1:])     #Extracts the score from the line and converts it to an integer. row[i+1:] gets the part after the last space, which is the scor
        if points>=50:              #Checks if the student passed (score is 50 or more)
            file_2.write(row+"\n")  #Writes the entire cleaned line to the output file (with a newline added at the end) ex. "Olivia Johnson 78\n"

print(f'Students who passed are in the new file "{new_file_name}"')

#6 Write a second version.
# Assume the file with results do not contain total points per pupil, but points for multiple part-exams. in file results2.txt
# So every row contains the pupils name and results with multiple results from different exams (or words as parts) seperated by white space.
# use function split to form a list where every word on the row gets added as an element in list
#add the students who got 50 points or more to new file passed2.txt

file_results = input ("Enter name of file with part-exam resluts:")         #OBS! be careful with when writing text input, no spaces or use .strip() at end
new_file_name = input ("Choose name of file with students who passed:")

with open (file_results, "r")as file_1, open (new_file_name,"w") as file_2:
# You need some logic to figure out how to separate the student's name (which could be multiple words) from their scores (which are numbers). Since we don't know exactly how many parts names have, let's just assume: The scores are all parts that are numbers, everything else is name.
    for row in file_1:
        row =row.strip()        #Removes whitespace (spaces, tabs, newlines) To clean the line so there are no extra spaces or newline characters interfering with processing.
        parts = row.split()     #splits by whitespace into a list of words. Using only row.split() only splits the line into words — it does NOT tell you which parts are the name and which parts are scores.
        name_parts = parts[:-3] #Takes all elements of the list parts except the last 3 and assumes those are the student’s name parts. Since student names can be one or multiple words, and scores come after, you need to identify where the scores start. Assuming first two words are first name and last name (adjust if needed), scores start from index 2 onwards
        score_start_index = 1   #Initializes score_start_index to 1.t's a starting guess for where the scores might begin (after the first word), to be updated in the next loop.
        for idx in range (1, len(parts)):   #Starts a loop from the second element (index=1) to the end of the parts list. To check each part to find the first one that can be interpreted as a score (an integer).
            try:
                int(parts[idx]) #Attempts to convert parts[idx] to an integer, works only if the string represents a valid integer number
                score_start_index = idx #this is where the scores start. Breaks out of the loop since we've found the first score.
                break
            except ValueError:  #If converting to integer fails (i.e., the part is not a number), it continues to the next element.
                continue

#creating lists
        name_parts = parts[:score_start_index]      #Creates a list name_parts with all elements before the first score index of student names
        score_parts = parts[score_start_index:]     #Creates a list score_parts containing all elements from the score start index to the end, which are the students part exam scores. These are the scores to be summed.

        points = sum(int(score) for score in score_parts)       #Converts each score in score_parts to an integer and sums them up. To calculate the total score for the student.

        if points >=50:     #Checks if the total score is at least 50.
            file_2.write(row+"\n")  #Writes the original row (line) to the output file, appending a newline.

print(f"Students who passed class is now added to {new_file_name}.")

#7 Write a program that reads a log file (log.txt) with rows containing a username followed by login times (in minutes).
# Find the user with the longest total login time and print their name and total minutes.

filename = "log.txt"

longest_user = None     # starts as None because no user processed yet
longest_time = 0        # longest_time to store the highest total login time found so far (starts at 0)

with open(filename, "r") as f:
    for row in f:
        if row.startswith("#") or row.strip() == "":    # Checks if the current line starts with # (a comment) or is empty after removing whitespace. First use of strip is for checking empty lines
            continue                                      # Skip comment lines and empty lines

        # .startswith() is a string method in Python. It checks whether a string starts with a specific substring and returns a Boolean (True or False).
        parts = row.strip().split()        # Second use of strip() is common to do this before .split(), so you don’t get an empty string or extra whitespace in your list.  Splits the line into a list of strings by whitespace (split()), storing it in parts. Example: "alice 30 20 15" → ["alice", "30", "20", "15"]
        username = parts[0]                # first item is username

        times = parts[1:]                  # The rest are login times in minutes, convert them to integers
        total_time = sum(int(t) for t in times)     # convert to int and sum them up

        if total_time > longest_time:
            longest_time = total_time
            longest_user = username

print(f"User with longest total login time: {longest_user} ({longest_time} minutes)")       # After processing all rows, print the user with the longest total login time

# 8 Write a verion of a the previous program that can edit the file with the pupils names and points (eg. results.txt file).
# Program can add new pupils in file and change points for a pupil who is already in file.
#To use this program user will enter new names or updates: like this: Alice Andersson 15
# The user will terminate with Ctrl+C

#Function that takes a line in the file, extracts the name (w/o number), returns the name in lowercase
def get_name(row):              # get_name that takes one argument: row, which is expected to be a line from the file (e.g., "Alice Andersson 12")
    word = row.strip().split()  # cleans and splits a string into a list of individual words, .strip() removes any space characters, tab and newline characters - .split() splits the string by spaces (default separator) into a list of words
    names = [e for e in word if not e.isdecimal()]      # list comprehension. This creates a list of words that are not numbers. It goes through each element e in the list word and keeps only the elements that are not numbers (i.e., not digits). .isdecimal() returns True if the string only contains numbers (like "12")
    name = " ".join(names)                              # This joins all the elements in the names list back into a single string, with a space " " between them.
    return name.lower()                                 # This converts the final name to lowercase, so that the name comparisons are not case-sensitive

try:
    # Step 1: Ask for the file name and load all rows into a list
    print("Terminate with Ctrl+C")
    file_name = input("File with results?: ")

    with open(file_name, "r") as f:
        rows = f.readlines()  # This line right here loads the file into a list of strings. WHY? Lists are easy to work with (loops, indexes, append, string functions). Read the whole file into the list of strings called 'rows'. You're simply reading all the lines into a list of strings.

    # Step 2: Start input loop
    while True:         # as long as user doesn't type Ctrl + C
        new_row = input("> ") + "\n"  # Read user input and add newline character
        new_name = get_name(new_row)  # Extract name from the input

        if new_name == "":
            print("Invalid line! Must include first and last name.")
            continue  # Skip invalid input

        inserted = False  # This variable acts as a flag to help us keep track of whether the user's name already exists in the file (or rather, in the list of lines from the file). Boolean variable named 'inserted' and sets it to False.

        # Loop through the lines to find a matching name
        for i in range(0, len(rows)):
            existing_name = get_name(rows[i])
            if new_name == existing_name:
                rows[i] = new_row  # Replace the old line with the new one
                inserted = True
                break  # Stop searching

        if not inserted:
            rows.append(new_row)  # Name wasn't found, so add it at the end of the file

# Step 3: Save file when the user presses Ctrl+C
except KeyboardInterrupt:       # Pressing Ctrl + C while a Python program is running sends a KeyboardInterrupt exception. f you don’t catch it, the program just crashes and exits immediately. By using except KeyboardInterrupt, you're saying: → "If the user presses Ctrl + C, don’t crash — do this instead."
    print("\nSaving and exiting...")

    with open(file_name, "w") as f:                 #opens the file in write mode ("w"), which means: It will overwrite the file completely. You're preparing to write the updated list (rows) into the file. with is used so the file automatically closes afterward
        for row in rows:                            #This loop goes through each element (row) in the list of lines (rows) you've been editing during the program.
            f.write(row)                            #This writes each row back to the file


#OBS! Does not work maybe bcs Mac?

#9 Now write a second version to edit in the file, but this time use a temporary file
#This method is safer than modifying the file in-place because it ensures: The original file isn't corrupted if the program crashes halfway. You don't lose data if something goes wrong during editing.
import tempfile         # Import the tempfile module to create temporary files safely

# same as before
def get_name(row):              # get_name that takes one argument: row, which is expected to be a line from the file (e.g., "Alice Andersson 12")
    word = row.strip().split()  # cleans and splits a string into a list of individual words, .strip() removes any space characters, tab and newline characters - .split() splits the string by spaces (default separator) into a list of words
    names = [e for e in word if not e.isdecimal()]      # list comprehension. This creates a list of words that are not numbers. It goes through each element e in the list word and keeps only the elements that are not numbers (i.e., not digits). .isdecimal() returns True if the string only contains numbers (like "12")
    name = " ".join(names)                              # This joins all the elements in the names list back into a single string, with a space " " between them.
    return name.lower()                                 # This converts the final name to lowercase, so that the name comparisons are not case-sensitive

try:
    print("Terminate program with Ctrl + C")
    f_name = input("File with results?: ")

    # Use valid mode "w+" for text read/write temporary file
    with tempfile.TemporaryFile("w+t") as temp:      # read more about these combos "w+t" lets you write and read in text mode, "w+" lets you write and read and If the file already exists, it clears (truncates) the file to zero length — so any old content is deleted.  tempfile.TemporaryFile creates a temporary file "temp" which is automatically deleted when it is closed, to read and write into = text mode

        while True:                                      # Loop forever until user presses Ctrl+C
            with open(f_name, "r") as f:                 # Open original file in read mode to scan existing lines
                new_row = input("> ") + "\n"             # Read new input line and add newline
                new_name = get_name(new_row)             # Extract name from the new input

                if new_name == "":                        # Check if name is empty (invalid input)
                    print("Error in row")                 # Warn user
                    continue                              # Restart the loop for a new input

                inputted = False                          # Flag to track if the name was found and updated

                for row in f:                             # Go through each existing line in the original file
                    if get_name(row) == new_name:         # If the name in this line matches the new input's name
                        temp.write(new_row)                # Write new row instead of old one
                        inputted = True                   # Mark that we updated this entry
                    else:
                        temp.write(row)                   # Otherwise, copy the old line as is

                if not inputted:                          # If the name was not found in the existing file, add it now
                    temp.write(new_row)                   # Correct variable name: temp, not t

            with open(f_name, "w") as f:                  # Open original file to copy all lines from the temp file and WRITE back into the original file
                temp.seek(0)                               # Move temp file cursor back to the beginning
                for row in temp:                           # Read every line in the temporary file
                    f.write(row)                           # Write each line from temp file to original file
                temp.seek(0)                               # Move cursor back to start for next iteration
                temp.truncate(0)                           # Clear temp file content to zero bytes

except KeyboardInterrupt:
    print("\nSaves and exits program...")  # Message shown when user exits with Ctrl+C
    exit()  # Exit the program cleanly


#10 Write a program that counts how many rows there is in a file .
# Program will start from commandorow.
# You can input multiple filenames as arguments.
# Program will then calculate amount of rows in all files.
# This is done for one file at a time and you´ll get an separate output for every file

#read multiple command line arguments with sys
#Loop through each filename passed as an argument
#For each file, count the lines
#Print the result for each file with its filename seperated by whitespace
#to use Save your script, Open a terminal / command prompt, Navigate to the folder, Run the script with file arguments
# right click on folder to copy path , Check you’re in the right folder type: ls
#obs! cd changes to the folder where your script is. python3 T.py ... tells the system: “Use Python 3 to run this script.”
# cd /Users/zineb/Pycharm/September/ProgramsSeptember-25
# python3 T.py file1.txt file2.txt
import sys

def count_lines(filename):
    try:
        with open(filename, "r") as f:         # read mode (default). You can only read from the file, not write to it
            return sum(1 for _ in f)           # "_" variable stands for line; we only count lines
    except FileNotFoundError:
        print(f'Error: File "{filename}" not found!')
        return None                             # The function count_lines is supposed to give back the number of lines.
                                                 # If the file doesn’t exist, there’s no valid number to return.
                                                 # None is Python’s way of saying “no value” or “nothing here.”

def main():                                     # All the code below (indented) will run when main() is called
    if len(sys.argv) < 2:                       # sys.argv is a list of all the arguments passed from the command line.
                                                 # If it’s less than 2, that means only the script name was given, and no filenames were provided.
        print("Usage: python script.py <file1> <file2> ...")  # If no filenames were given, we tell the user how to use the program correctly.
        return                                  # This exits the main() function. Useful because if no filenames are given, there’s nothing left to do.

    for filename in sys.argv[1:]:               # sys.argv[1:] means “take everything in the list starting from index 1 onward.”
                                                 # Index 0 is the script name (script.py), so we skip that.
                                                 # This loop will go through each filename the user typed in
        line_count = count_lines(filename)      # Calls the function we wrote earlier. Function opens the file and counts its lines
        if line_count is not None:              # Checks whether the function gave back a valid number.
                                                 # If the file didn’t exist, line_count would be None, and we’d skip printing.
            print(f"{filename}: {line_count} rows")  # If the file was read successfully, print the filename and number of rows

if __name__ == "__main__":
    main()



#11 Write a program that READS a textfile and writes out the textfiles contents In the command window.
# In the output, all "." characters should be replaced with one space character

def print_modified_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:     #If the text file contains special characters (like å, ä, ö in Swedish, or accents in other languages), opening it without specifying the encoding could cause errors or show weird characters.
            for line in file:
                modified_line = line.replace(".", " ")  # "." is old, replaced by" " new
                print(modified_line, end="")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

print_modified_file("example.txt")      # Replace "example.txt" with the name of your text file

# When you have time look why Ctrl C and tab do not work!




