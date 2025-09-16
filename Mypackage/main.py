#in this file import and use your package functions
# IMPORTANT: “Run main.py as a module inside the Mypackage package,” so the relative imports (.filename) like from .greetings are valid.


from .greetings import say_hello, say_goodbye, welcome_message  #use dot befole file name, and leave .py
from .animals import fav_animal, list_of_animals, is_mammal
from .colors import favorite_color

#using a greeting
print (say_hello("Zineb"))

#checking if elephant is a mammal in the list of mammals
print (f"Is Elephant a mammal? {is_mammal("Elephant")}")

#What is my favorite color
print (favorite_color())


#Avoid relative imports (not recommended)
# If you switch to absolute imports (e.g., from Mypackage.greetings import ...),
# you could run main.py as a script directly.


#otherwise
#Step-by-step:
#Open PyCharm and open your project (ExercisesSeptember-25).
#Go to the top menu and click:
#Run → Edit Configurations...
#In the Run/Debug Configurations window:
#Click the + button (top-left)
#Choose Python
#Fill in the fields as follows:
#Name: Run main as module (or whatever you want)
#Module name: Mypackage.main #obs module not script!
#Mypackage.main
#(This is key — write your package name + dot + main file name WITHOUT .py)
#Working directory:
#This should be the root folder of your project, e.g.,
#/Users/zineb/PycharmProjects/ExercisesSeptember-25
#Script path: Leave this empty (because you are running as a module)