#To run in script mode:
#python console tab in bottom The Python Console opens — it’s an interactive REPL inside PyCharm.
#You can copy-paste parts of your script here, or type commands line by line and see immediate results.


from Mypackage import greetings
print(greetings.say_hello("zineb"))

from Mypackage import animals as a
print(a.fav_animal())

from Mypackage.colors import favorite_color, \
    least_fav  # import a certain functionname/definition directly? if the file with definitions is in a package
print(favorite_color())

from Mypackage import *    #to control what gets imported from Mypackage, define an "__all__" in __init__.py file
print (least_fav())     #now you have already imported module colors , otherwise Mypackage.colors


from package import *
from Mypackage import colors
print(colors.kökslista)
#eller
from Mypackage.colors import kökslista
print(kökslista)


import sys
print(sys.argv[0])     #Gives access to system-level info, if no argument passed and using [1] will give error different type of functions with sys. ...

import numpy
myarray = numpy.array([1, 2, 3])      #array vs list: A group of values in one structure, when working with numbers and you want to do math or data processing efficiently use array
print (myarray * 2)                   #treating each number independently, FAST

mylist = [1, 2, 3]                    #unlike normal list
print (mylist * 2)







#Why quotes and print function
#When calling say_hello(zineb), Python expects zineb to be a variable — you didn’t define zineb anywhere.
#So, Python raises a NameError: it doesn’t know what zineb means.
#To pass the actual text "zineb", you must give it as a string literal with quotes:

#Your function returns a string. It doesn’t print it.
#When you call greetings.say_hello("zineb"), Python evaluates it and gets the string "Hello, zineb!" back.
#But if you don’t do anything with that returned string, nothing appears on your screen.

#Summary
#Importing the function just makes it available in your file.
#How you call the function matters: you must give proper arguments (like strings with quotes).
#And you must decide whether to use the return value (e.g., print it) or ignore it.