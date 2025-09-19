
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
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result is {result}")
finally:
    print("Execution finished.")

#5 catch all exceptions using a bare except or by catching the base exception class Exception and adding it at bottom.
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