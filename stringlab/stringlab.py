# Function is_palindrome that takes a string and checks if the text reads the same forwards and backwards.
# Any differences in uppercase/lowercase letters, spaces, punctuation, etc. should be ignored by using stringutils.normalize.
# Create a main function that runs when the program starts.
# Let main display a menu that initially only offers the option to check if a word is a palindrome.
# Main should utilize the functions in menu.py.
# Feel free to use match..case to handle the user's menu choice.
# The user should also be able to enter the string to be checked.


from menu import print_menu, get_menu_choice
from stringutils import normalize, extract_initials, check_password

# Function returns True if the text is a palindrome (ignores case, spaces, and punctuation).
def is_palindrome(text: str) -> bool:
    normalized = normalize(text)
    return normalized == normalized[::-1]


def main():
    while True:
        print_menu()
        choice = get_menu_choice(5)

        match choice:
            case 1:
                text = input("Enter a string to check if it is a palindrome: ")
                if is_palindrome(text):
                    print("✅ The string is a palindrome!")
                else:
                    print("❌ The string is not a palindrome.")

            case 2:
                name = input("Enter a full name: ")
                result = extract_initials(name)
                print(f"Initials: {result}")

            case 3:
                pwd = input("Enter a password to check: ")
                if check_password(pwd):
                    print("✅ The password is sufficiently secure!")
                else:
                    print("❌ The password does not meet the requirements.")

            case 4:
                text = input("Enter text to normalize: ")
                result = normalize(text)
                print(f"Normalized text: {result}")

            case 5:
                print("Exiting the program.")
                break

if __name__ == "__main__":
    main()

