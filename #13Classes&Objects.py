# when going through doc use print() to separate the number you are working on



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


#8 How does Python knows which circle object’s radius to update when you call set_r?
# How does the method set_r know that it is the radius of circle1 that needs to be changed and not radius of another circle.
# Like we are only using self.r in distribution sentence....

#Every time you call a method on an object (e.g., circle1.set_r(7)), Python automatically passes that object as the first argument to the method, which by convention is named self.
#The method set_r knows which circle’s radius to change because the object you call it on (circle1, circle2, etc.) is automatically passed as the self argument.
# Therefore, self.radius refers specifically to the radius of that particular object, not all circles.

#9 Why know this?
# We need to know this because it explains how objects keep their own separate data in object-oriented programming.
# If you didn’t understand that self always refers to the current object, it might look like all Circle objects share one radius, which would make it impossible to have multiple independent circles.

#10 Use the previous programs made to calculate area and circumference of two new circles c1 and c2, let user type in radius
r1 = float(input("Enter radius of first circle: "))
r2 = float(input("Enter radius of second circle: "))

#We have an Class called "Circle", rest of the parameters will be defaulted...
c1 = Circle(radius=r1)
c2 = Circle (radius=r2)

# Calculate and display results
#functions area and circ are methods defined inside Circle class
print(f"Area: {c1.area():.2f}")
print(f"Circumference: {c1.circ():.2f}")

print(f"Area: {c2.area():.2f}")
print(f"Circumference: {c2.circ():.2f}")

#11 define a class "Rectangles" that describes rectangles. Add the class into a file amed "rectangle.py"
# Let the class contain instance variables describing rectangles start-point (upper left corner) , height and lenght
# And add a method that calculates the area and circumference

#see file Rectangles.py
# to use in this file type example:
#from rectangle import Rectangles

#r1 = Rectangles(x=2, y=3, height=4, length=6)
#print(r1)  # Rectangle at (2, 3) with height 4 and length 6
#print("Area:", r1.area())
#print("Circumference:", r1.circumference())


#12 Create a new file with class similar to class "Rectangles" named "Prectrangles"
# but this time so that the instance variables that describe height and lenght are considered private.
# Add get- and set- methods instead, and setter methods to update the private variables in a controlled way
# at last test it

#see file Prectangles.py
from Prectangles import Prectangles

#test
# Create a rectangle with default values, (you can also Create a rectangle with custom values)
rectangle_1 = Prectangles()
print (rectangle_1)
print("Area:", rectangle_1.area())
print("Circumference:", rectangle_1.circumference())

# Use setter methods to change height and length
rectangle_1.set_height(5)
rectangle_1.set_lenght(8)
print ("Updated rectangle after using setters:", rectangle_1)
print ("Area:", rectangle_1.area())
print ("Circumference:", rectangle_1.circumference())

# Use getter methods to read values
print("\nUsing getters for r2:")
print("Height:", rectangle_1.get_height())
print("Length:", rectangle_1.get_lenght())


#13 We can now do the same way as we did with instance variables, on Classvariables.
# Consider that we in the class "Bankacc" do not want the  interest rate to be able to be negative.
# we can then rename interestr to _interestr, adding "_"
# and define the methods set_interestr and get_interestr, these are called class methods
# Make these changes to Class Bankacc

class Bankacc:
    _interestr = 0.0        # private class variable (interest rate)

    def __init__(self):
        self.accowner = None  # None means "not yet assigned"
        self.saldo = 0
        self.earned_interest = 0

    @classmethod             # Class method to set interest rate
    def set_interestr(cls, new_rate):   #cls stands for class (just like self stands for the current object in instance methods).You use cls to access class variables or call other class methods.
        if new_rate >= 0:  # prevent negative interest
            cls._interestr = new_rate
        else:
            print("Interest rate cannot be negative!")

    @classmethod             # Class method to get interest rate
    def get_interestr(cls):
        return cls._interestr

    def apply_interest(self):           # Optional: instance method to apply interest to this account
        interest = self.saldo * Bankacc._interestr
        self.earned_interest += interest
        self.saldo += interest
        return interest

#14 Now test this by create a new account and set interest to 0.05%
Bankacc.set_interestr(0.05)     # Set class-level interest rate

acc_1 = Bankacc()               # Create an account
acc_1.saldo = 1000

acc1.apply_interest()           # Apply interest
print("Saldo after interest:", acc1.saldo)
print("Earned interest:", acc1.earned_interest)


#15 Now we move on to Classes describing different kind of Houses.
# All classes are supposed to be subclasses (direct or indirect) to a class "House" that describes houses in all generality.
# Class house will have instance variables length and width.
# Use method __str__ to get printout from a House
# Class house will also have method "quadratical" that examines if lenght and width is equal and method area that calculates the house´s total floor surfice area

class House:
    def __init__(self,length=0, width=0):        #constructor for a generic house
    self.length = length
    self.width = width

    def __str__(self):
        return f"House with length {self.length} and width {self.width}"

    def quadratical(self):
        return self.length == self.width

    def area(self):
        return self.length * self.width



#16 Now assume we want to describe a multiple-story house.
# We can define a new class "Multi_story_house" as a subclass (to class "House")
# In this subclass we want to add an instance variable telling how many floors a house has
# the subclass should not be indented under class House BTW

class Multi_story_house(House):
    def __init__(self, length=0, width=0,floors=1):
        super().__init__(lenght,width)  # call the parent constructor
        self.floors = floors            # new instance variable for number of floors

    def __str__(self):
        return f"Multi-story house with length {self.length}, width {self.width}, and {self.floors} floors"

    def total_area(self):       #Calculates total floor area considering all floors
        return self.area() * self.floors

#17 In a subclass you can add a new definition of a method that in another case would have been inherited from superclass.
# We call this "override" in OOP (= a method in the subclass overrides the method in the superclass)
# explain what we used in last code that describes this

#In Multi_story_house class we defined a string method like this:
def __str__(self):
    return f"Multi-story house with length {self.length}, width {self.width}, and {self.floors} floors"

#The superclass House already has a __str__ method from before:
def __str__(self):
    return f"House with length {self.length} and width {self.width}"

#In Multi_story_house, you defined a new __str__ method,
#so when you print a Multi_story_house object, Python calls the subclass version instead of the House version.
#This is method overriding.
#So Override means a subclass provides its own version of a method that already exists in the superclassand, Python always calls the method of the object’s actual class first.
#Allows a subclass to customize behavior without changing the superclass.

#18 Dynamic binding in OOP:
# Construct the class School and let it be a subclass of the class MultistoryBuilding.
# Let the class School have an instance variable number_of_classrooms that specifies how many classrooms it has.
# Also add a method that calculates the average number of classrooms per floor.
# Then create two objects: one of the class MultistoryBuilding and one of the class School.
# Try setting the width for both objects to 15.
# Then try reading the number of classrooms for both objects using: getattr(object, "attribute_name", default_value) .What happens?

#Base-class MultistoryBuilding
class MultistoryBuilding:
    def __init__(self, length=0, width=0, floors=1):
        self.length = length
        self.width = width
        self.floors = floors

    def __str__:
        return f"Multistory building with length {self.length}, width {self.width}, and {self.floors}floors"


#Sub-class School
class School(MultistoryBuilding):
    def __init__(self, length=0, width=0, floors=1,number_of_classrooms=0):
        super().__init__(length, width, floors)
        self.number_of_classrooms = number_of_classrooms        # new instance variable

#to calculate Average num of classrooms per floor
    def average_classrooms_per_floor(self):
        if self.floors >0:
            return self.number_of_classrooms/self.floors
        else:
            return 0

    def __str__(self):
        return (f"School with length {self.length}, width {self.width}, "
                f"{self.floors} floors and {self.number_of_classrooms} classrooms")

#Create objects and test dynamic binding
building_1 = MultistoryBuilding(length=30, width=0, floors=3)
school_1 = School(length=40, width=0, floors=4, number_of_classrooms=12)

building_1.width =15  # Set width to 15 for both objects
school_1.width =15

print (building_1)     # calls MultistoryBuilding.__str__()
print(school_1)        # calls School.__str__()  -> dynamic binding: uses subclass method

# Try reading number_of_classrooms
# Python tries to look up the attribute named "attribute_name" in the object.
# If the attribute exists → it returns the value.
# If it does not exist → it returns the default_value
print(getattr(building_1, "number_of_classrooms", "Not defined"))  # Output: Not defined
print(getattr(school_1, "number_of_classrooms", "Not defined"))  # Output: 12

#Output reflection:
# Dynamic binding says: Python chooses which method or attribute to use based on the actual type of the object at runtime.
# Here, school_1 is a School, so Python finds number_of_classrooms in the subclass, even though MultistoryBuilding (the “mother” class) does not have it.
# building_1 is a MultistoryBuilding, so Python does not find the attribute in the parent class → returns the default.


























-----------------------------------------------
#19 Extend your class School from Exercise 13.13 with an overriding method area.
# Let the method calculate the area as the number of classrooms multiplied by 50.
# Then create a list with one object of type House and one of type School.
# Initialize the two objects so that they have the same length and width.
# Also initialize the variable number_of_classrooms in the School object.
# Then loop through the list and call the method area for the objects it contains.
# Write down the result and study what happens.


#20 A Object Oriented Example: shows the basics of classes, attributes, methods, and object interaction.
#Create a program that models a simple deck of cards.
	#1.	Define a class Card with two attributes: suit and value.
	    #•	Add a method __str__ that returns a text description of the card (e.g., “Ace of Hearts”).
	#2.	Define a class Deck that contains a list of Card objects.
	    #•	In the constructor, create a full deck of cards.
	    #•	Add a method shuffle() to shuffle the deck.
	    #•	Add a method draw() that removes and returns the top card.
	#3.	Write a short program that:
	    #•	Creates a deck,
	    #•	Shuffles it,
	    #•	Draws and prints 5 cards.







#BONUS to exercis 20:
# Change in the main-part of the program so that två human players can play against each other


#MORE REPETITION....LASTLY