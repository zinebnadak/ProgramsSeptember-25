
#Here, Computer is just the blueprint.
# Object / instance is the actual thing you create from the blueprint.

class Computer:     # In our seat we add behavioours eg methods/functions and attributes eg. variables
    def config (self):      #our method/function
        print("i5, 16gb, 1TB")  #our attributes/variables

a = 5.5
print(type(a))

#com1        #if we leave our variable like this, it do not have a type...
com1 = Computer()     #use parenthesis! so we need to make com1 an object to Class (computer). By using () com1 is now an object (instance) of Computer
print(type(com1))

#SO...
#When you write com1 = Computer, wo parenthesis You’re just saying: “com1 is the class itself.
#When you write com1 = Computer() The () calls the class constructor. Python creates a new object (instance) of the class
#.

print("hello")
