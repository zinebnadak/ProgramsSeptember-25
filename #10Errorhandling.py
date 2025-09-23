
#1 give an example of some code to give me traceback/stacktrace
def divide(a, b):
    return a / b

def main():
    x = 10
    y = 0
    result = divide(x, y)  # This will cause a ZeroDivisionError
    print(result)

main()      #call function will give error

#2 generate exceptions during RuntimeErrors using assert-statemnet
def check_positive(number):
    assert number > 0, f"Number must be positive, got {number}"     #The assert statement checks if 10 > 0 — which is True, Since the condition is True, the assert passes silently.

def main():
    check_positive(10)  # This passes
    check_positive(-5)  # This will raise an AssertionError

main()


#3 generate exceptions during RuntimeErrors using raise-statemnet
def risky_operation(value):
    if value < 0:
        raise RuntimeError(f"Negative value error: {value} is not allowed")
    return value * 2

def main():
    print(risky_operation(10))   # This works fine
    print(risky_operation(-5))   # This raises RuntimeError

main()

#4 Use the try, except, else, and finally - blocks.
# Contains of a try-part and multiple except-parts.
# If no error occurs the try part is excecuted,
# if errors occur the runtime terminates in try-part and the program directly jumps to except-part.
# Except-parts tells what kind of errors we can handle. Ex. valueError, divisionbyzeroError...
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:          #every except block is checked independently
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:                                       #Runs only if no exception was raised in the try block.
    print(f"Result is {result}")            #Runs always, whether or not an exception was raised or caught.
finally:
    print("Execution finished.")

#5 catch all exceptions, use a base class "Exception as *variablename" ,and add the type of the exception adding it at bottom.
try:
    # Code that might raise any exception
    risky_code()
except Exception as e:
    print(f"Caught an error: {e}")
    print(type(e))
    # Program continues running here


#6 You never return to the try-part if an error occurs there, give an example of how to repeat code until valid answer is entered?
while True:
    try:
        num = int(input("Enter a number: "))
        break  # Exit loop if input is valid
    except ValueError:
        print("That's not a valid number, try again.")

print(f"You entered: {num}")


#6 Let user write a number, and check if it is a number or not.
# Use bool-type for this, not pythons built in .isdigit

answer = input("Write a number: ")

ok = True
for i in answer:
    if i < "0" or i > "9":      # checking if the input is numeric. If any character is not between "0" and "9", it sets ok = False. We can use numbers as strings bcs they follow same order in ASCII numbering, so 1 is greater than 0 too...etc
        ok = False
        break

if ok:
    print("Number is OK")
else:
    print("Not a number!")

#7 Let user write a number, and check every item independently
answer = input("Write a number: ")

for i in answer:
    if "0" <= i <= "9":
        print ("Number is OK!")
    else:
        print("Not a number!")


#8 Why do i need to make it complicated with variable "ok" why not just add break-statement, else-part and if-statement in first version of program
# like this:
answer = input("Write a number: ")

for i in answer:
    if "0" <= i <= "9":
        print ("Not a number!")
        break
else:
    print("Number is OK!")

#9 Write a function that checks if leap year or not and that only accepts
# input year from 1754 and up
# use an assert-statement to control this
# leap year is a year that
# leap year is a year that is divisible by 4 but not by 100, unless it's also divisible by 400

year = int(input("Enter a year: "))

def leap_year(year):
    assert year >= 1754, ("Too early year", year)
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

print(leap_year(year))      #will give you boolean answer

#10 Write a function that controls with a variable "user_input"
# that text is a mail-adress
#There needs to be at least a dot after @ sign
# use a raise statement for error handling so returns True or False for valid/invalid email

user_input = input("Enter email: ")

def is_not_email(user_input):
    if "@" not in user_input:
        raise ValueError('Missing "@" in the email adress')

    at_index = user_input.index("@")           #This line finds the position (index) of the @ symbol in the string user_input
    if "." not in user_input [at_index:]:        #from index of "@" and forward
        raise ValueError ('Missing "." after the "@" in the email adress!')

    return ("Valid email")      #check each if statement independently before returning...

    # No error means it's a valid basic email format

email = is_not_email(user_input)
print (email)


# 11 A recursive function can use a lot of memory, since each new recursive call creates its own copy of local variables and parameters.
# If the memory runs out, an error message of the type RecursionError is generated.
# Test the recursive function nfak and investigate how large values of n you can give as arguments before this happens.

def nfak(
        n):  # fakulty of n
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n * nfak(n - 1)

    # Write code that:


# Calls nfak with increasing values of n.
# Catches RecursionError when it happens.
# Prints the largest n that works without error

max_n = 0

try:
    for i in range(1, 2000):        # Start with a big number and go down to find the max safe n , Or start small and increase - up to you
        result = nfak(i)
        max_n = i
except RecursionError:
    print(f"RecursionError at n = {i}")

print(f"Largest n for nfak without RecursionError is: {max_n}")


#You can solve a problem either with an iterative or recursive approah