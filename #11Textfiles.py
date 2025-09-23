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


