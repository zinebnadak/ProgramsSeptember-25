
#Here, "Computer" is just the blueprint.
# Object / instance is the actual thing you create from the blueprint.

class Computer:     # In our seat we add behavioours eg methods/functions and attributes eg. variables
    def config (self):      #our method/function (variable name). self represents the instance (object) of the class that is calling the method. For example, if you later do com1.config(), self refers to comp1
        print("i5, 16gb, 1TB")  #our attributes/variables

a = 5.5
print(type(a))

#com1        #if we leave our variable like this, it do not have a type...
com1 = Computer()     #use parenthesis! so we need to make com1 an object to Class (computer). By using () com1 is now an object (instance) of Computer
print(type(com1))
com1.config()       #function/method that prints a list

print()
#SO...
#When you write com1 = Computer, wo parenthesis You’re just saying: “com1 is the class itself.
#When you write com1 = Computer() The () calls the class constructor. Python creates a new object (instance) of the class


#1 Define a Class that describes cars.
# Name the class "Car".
# One car vill have a registrationnumber,brand,year-model,curb weight, and engine power
#put the Class in a file Car.py
# When you run the program there wont happen anything bc it is not a complete program yet
# see "BMWM8-file"

#2 Complete the program "BMWM8" so the instance variables in two new "Car"-objects gets assigned some appropriate values
from BMWM8 import Car

#Create first car object
car1 = Car(
    owner = None,
    reg_num="ABC123",
    brand="BMW",
    model=2025,
    curb_weight=1880,
    engine_power=625,
)

#Create second car object
car2 = Car(
    owner= None,
    reg_num="DEF456",
    brand="BMW",
    model=2024,
    curb_weight=1825,
    engine_power=600,
)

#Option 2: Using positional arguments (shortest form), see what happens when removing #.
#car1 = Car("ABC123", "BMW", 2025, 1880, 625)
#car2 = Car("DEF456", "BMW", 2024, 1825, 600)



#3 An instance variable can be of whatever type , it can also be a reference variable.
#Create a Class Person to be used as the reference
# Create a Class describing a bankaccount, use a reference-variable "acc owner" as instance-variable.

class Person:
    def __init__(self, surname="",lastname="",birthyear=0,single=True, partner=None):         #because birthyear is a number use 0 insted of "" for strings
        self.surname = surname
        self.lastname = lastname
        self.birthyear = birthyear
        self.single = single        #hard coded "single" is Ture unless changed
        self.partner = partner

    #returns this (self.partner is used instead of boolean self.single which is now removed)
    def __str__(self):              #Important! tells Python to print as string when printed
        if self.partner:  # If there is a partner assigned
            partner_name = f"{self.partner.surname} {self.partner.lastname}"
            return f"{self.lastname} {self.surname}, born {self.birthyear}, Married to: {partner_name}"
        else:
            return f"{self.lastname} {self.surname}, born {self.birthyear}, Single"



Person_1 = Person(surname="Zineb", lastname="Nadak", birthyear=2004, single=False)
print(Person_1)

Person_2 = Person(surname="Mariam", lastname="Nadak", birthyear=2008, single=True)
print(Person_2)

print()

class Bankacc:
    def __init__(self):
        self.accowner = None        #None means "not yet refer to an object".
        self.saldo = 0
        self.earned_interest = 0

acc_1 = Bankacc ()
acc_1.accowner = Person_1       #You do not need to call Person() again. Just assign the existing object:. By creating a class named "Person" previously we could reference that person here by writing Person ()
acc_1.saldo = 30500.25
acc_1.earned_interest = 700.40

# Print bank account info
print(f"Account owner: {acc_1.accowner}")       #to get only sur/last name: print(f"Account owner: {acc_1.accowner.surname} {acc_1.accowner.lastname}")
print(f"Saldo: {acc_1.saldo}")
print(f"Earned interest: {acc_1.earned_interest}")
print()

#To summurize:
# acc_1 is a object to Class Bankacc..
# acc_1:s own “box”  holds saldo and earned_interest (=instance variables or attributes)
# while its accowner reference variable initially points to None (an empty placeholder) that can later point to another “box” containing a specific Person object.

#4 Add the class "Car" in a reference to a person as the cars owner .
# Then initiate the two different cars so every car gets its own owner

#first add an instance variable in Car class named owner (which is now set to None to later hold a reference to a Person object).
#You don’t need to rewrite the whole car creation. Since you already created the car objects with owner=None, you can just assign the owners afterward:
car1.owner = Person_1
car2.owner = Person_2
#test
print(car1)
print()
print(car2)

#5 Change instance variable "single" (True/False) in class Person to partner. and set it to None.
# This to use a reference to another person.
# change the def __str__(self), and include a if-else
# Create a new person and let him be married to Zineb

Person_3 = Person(surname="Prince", lastname="Charming", birthyear=2001)

# Assign partner
Person_1.partner = Person_3

print(Person_1)  # Should show Zineb is married to Prince Charming
print(Person_2)  # Still single
print(Person_3)  # Still single unless you assign a partner

#5 Create a class circle so that the one that creates a new object of Class circle can himself choose what initial values the instance variables will have
# The parameters for class Circle should be, x,y (for center) and radius
#do not test yet
import math         #for defining the methods later exercise
class Circle:
    def __init__(self, x=0, y=0, radius=0):     #__init__ is a constructor. Python automatically calls __init__ when you create a new object of the class. It initializes the object with the attributes you want it to have.
        self.x=x        #these are instance variables unique to that object and "self." refers to the specific object being created
        self.y=y        #This structure ensures that every Circle object can have its own center coordinates and radius, either default or custom.
        self.radius=radius

    def __str__(self):
        return f"Circle with center at ({self.x}, {self.y}) and radius {self.radius}"

    #___________________another exersice defining methods

    def set_r(self, new_radius):  # Method to change the radius
        self.radius = new_radius

    def area(self):  # Method to calculate the area
        return math.pi * self.radius ** 2

    def circ(self):  # Method to calculate the circumference
        return 2 * math.pi * self.radius


#6 Now test first with default values, then custom by user then only radius rest is default.

# Circle with default values
circle1 = Circle()
print(circle1)  # Output: Circle with center at (0, 0) and radius 0

# Circle with custom values
circle2 = Circle(x=5, y=10, radius=7)
print(circle2)  # Output: Circle with center at (5, 10) and radius 7

# Another circle with only some custom values
circle3 = Circle(radius=3)
print(circle3)  # Output: Circle with center at (0, 0) and radius 3

# Now you have Modified the Car class so that when you create a car, you can choose initial values for all the car’s attributes (owner, registration number, brand, model, curb weight, engine power).
# Instead create a new BMW class to have default values so that when you create a car object, you don’t have to provide all values every time.
#Example for a company to keep track of who the owner and reg numbers for the sold cars are.
# Create one car that has not been sold yet and another one sold to Zineb Nadak (use reference), print both

class BMW:
    def __init__(self, owner=None, reg_num="UNKNOWN", brand="BMWM8", model=2025, curb_weight=1880, engine_power=625):
        self.owner = owner
        self.reg_num = reg_num
        self.brand = brand
        self.model = model
        self.curb_weight = curb_weight
        self.engine_power = engine_power

    def __str__(self):      #to get string answer
        return (f"Owner: {self.owner}\n"
                f"Reg Number: {self.reg_num}\n"
                f"Brand: {self.brand}\n"
                f"Model: {self.model}\n"
                f"Curb Weight: {self.curb_weight} kg\n"
                f"Engine Power: {self.engine_power} HP")

# Create a BMW car object using default values
car1 = BMW()
print(car1)

#Company sold a car to Zineb Nadak
car2 = BMW(owner=f"{Person_1.surname} {Person_1.lastname}")      # Only set the owner (sur+last name), other attributes use defaults
print(car2)

#7 Evaluate the class Circle with three methods:
# set_r : one you can change the radius
# area : claculating area
# circ : calculating circumference
#OBS! You need to define these methods inside the Circle class
#lastly test and change radius to 7

#to test use the previous Circle1 object we created
print(circle1)      #looks like this from before
print(f"Circle with center at ({circle1.x}, {circle1.y}) and radius {circle1.radius}. Area: {circle1.area():.2f}. Circumference: {circle1.circ():.2f}")

#Now use method to change radius to 7
circle1.set_r(7)
print(f"Circle with center at ({circle1.x}, {circle1.y}) and radius {circle1.radius}. Area: {circle1.area():.2f}. Circumference: {circle1.circ():.2f}")


