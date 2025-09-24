#7 Write a program that reads a log file (log.txt) with rows containing a username followed by login times (in minutes).
# Find the user with the longest total login time and print their name and total minutes.

filename = "log.txt"

longest_user = None     #starts as None because no user processed yet
longest_time = 0        #longest_time to store the highest total login time found so far (starts at 0)

with open(filename, "r") as f:
    for row in f:
    if row.startswith("#") or row.strip() == "":    # Checks if the current line starts with # (a comment) or is empty after removing whitespace. First use of strip is for checking empty lines
        continue                                      # Skip comment lines and empty lines

#.startswith() is a string method in Python. It checks whether a string starts with a specific substring and returns a Boolean (True or False).
    parts = row.strip().split()        #Second use of strip() is common to do this before .split(), so you don’t get an empty string or extra whitespace in your list.  Splits the line into a list of strings by whitespace (split()), storing it in parts. Example: "alice 30 20 15" → ["alice", "30", "20", "15"]
    username = parts[0]






#8 Write a verion of a the previous program that can edit the file with the pupils name and points (results.txt).
# Program can add new pupils in file and change points for a pupil who is already in file. The user will terminate with Ctrl+C