#11 define a class "Rectangles" that describes rectangles. Add the class into a file amed "rectangle.py"
# Let the class contain instance variables describing rectangles start-point (upper left corner) , height and lenght
# And add a method that calculates the area and circumference

class Rectangles:
    def __init__(self,x=0,y=0,height = 0, lenght =0):   #constructor for creating a rectangle
    self.x = x
    self.y = y
    self.height = height
    self.lenght = lenght

    def area(self):
        return self.height*self.lenght

    def circumference(self):
        return 2*(self.height+self.lenght)

    def __str__(self):
        return (f"Rectangle at ({self.x},{self.y}) with height {self.height} and lenght {self.lenght}")

