def print_menu():
    # Prints the program menu.
    print("\nWelcome to the String Lab!")
    print("1. Check palindrome")
    print("2. Extract initials")
    print("3. Check password")
    print("4. Normalize text")
    print("5. Exit")

def get_menu_choice(no_of_choices: int) -> int:
    # Gets the user's menu choice and validates it.
    while True:
        try:
            choice = int(input(f"Choose an option (1-{no_of_choices}): "))
            if 1 <= choice <= no_of_choices:
                return choice
            else:
                print(f"Invalid choice! Please enter a number between 1 and {no_of_choices}.")
        except ValueError:
            print("Invalid input! Please enter a number.")
