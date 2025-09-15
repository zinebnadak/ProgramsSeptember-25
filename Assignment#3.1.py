#DelUppgift 1. Function-based temperature conversion (Celsius, Farenheit & Kelvin)


def main():      # Runs the program and manages the loop until user chooses to terminate, calls the functions: print_menu, get_menu_choice, get_unit, convert and keeps tack of the latest choosen scales
    start_unit = "C"  # Default "from" scale is Celsius
    to_unit = "F"     # Default "to" scale is Fahrenheit

    while True:      # infinite loop
        print_menu(start_unit,to_unit)   # Display current menu and unit choices
        choice = get_menu_choice(4)      # Ask the user to choose 1–4

        if choice == 1:
            start_unit = get_unit()      # Ask user to set the "from" unit, so I get "get" it
        elif choice == 2:
            to_unit = get_unit()         # Ask user to set the "to" unit
        elif choice == 3:
            convert(start_unit, to_unit) # Perform conversion using current units
        elif choice == 4:
            print("Goodbye!")            # Exit message
            break                        # Exit the loop , ends the program


def print_menu(start_unit, to_unit):        # Displays the menu with the current selected units
    print(f'1.Set "from" unit\n2.Set "to" unit\n3.Convert from scale {start_unit} to {to_unit}\n4.Quit')
    print() #blank line

def get_menu_choice(no_of_choice:int)->int:      # Asks the user for a menu choice (1–4), n_of_choice tells what choice user asked for, converts to an int
    while True:     # infinite loop
        try:        # block is used to attempt code that might crash (raise an error). If the code inside the try block runs successfully, continue as normal
            choice = int(input("Enter choice no. 1-4:"))     # ask user for input
            if 1 <= choice <= no_of_choice:                  # check if valid number input
                return choice                                # ends function. Sends a valid choice back to where function was called
            else:
                print("Invalid choice! Please enter choice no. 1-4:")
        except ValueError:                                    # sends error message if user tries to enter something that is not integer
            print("Please enter a number!:")


def get_unit() -> str:      # Asks the user for a temperature scale (C/F/K) and validates it
    units = ["C","F","K"]       # Allowed units
    while True:                 # infinite loop
        unit = input ("Enter a unit (C/F/K): ").strip().upper()     # So users can enter c, f, k or add spaces and still be accepted.
        if unit in units:       # Check if the unit user entered is in my list of valid units
            return unit
        else:
            print("Invalid unit!")


def convert(start_unit, to_unit):       # Handles the entire conversion flow for one temperature
    temp = get_temperature(start_unit)                     # Ask user to enter a temperature in start_unit
    temp_c = convert_to_celsius(temp, start_unit)          # Convert input temperature to Celsius
    result = convert_to_target(temp_c, to_unit)            # Convert Celsius to target unit
    print_result(result, to_unit)                          # Print final result and unit


def get_temperature(scale):      # Asks the user to enter a temperature value
    while True:     # infinite loop
        try:
            temp = float(input(f"Enter temperature of ({scale}):"))       # Ask for temperature in the given scale
            return temp                                                   # return temperature as float
        except ValueError:                                                # Handle invalid number input
            print("Invalid number!")


def convert_to_celsius(temp, scale):     # Converts a temperature from any scale to Celsius
    if scale == "C":
        return temp                      # No conversion needed
    elif scale == "F":                   # F to C
        return (temp-32)*5/9
    elif scale == "K":                   # K to C
        return temp - 273.15


def convert_to_target(temp, scale):      # Converts a temperature from Celsius to the target scale
    if scale == "C":
        return temp                      # No conversion needed
    elif scale == "F":                   # C to F
        return (temp * 9/5)+32
    elif scale == "K":                   # C to K
        return temp + 273.15


def print_result(temp, scale):       # Prints the result
    print (f"Converted temperature: {int(round(temp))}°{scale}")   # Round to integer, show scale
    print() #empty line

if __name__ == "__main__":      #so the code runs functions when you start the script
    main()