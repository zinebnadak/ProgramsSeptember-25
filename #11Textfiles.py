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

#7