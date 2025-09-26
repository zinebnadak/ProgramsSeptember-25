
def print_modified_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:     #If the text file contains special characters (like å, ä, ö in Swedish, or accents in other languages), opening it without specifying the encoding could cause errors or show weird characters.
            for line in file:
                modified_line = line.replace(".", "          ")  # 10 spaces
                print(modified_line, end="")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

print_modified_file("example.txt")      # Replace "example.txt" with the name of your text file
