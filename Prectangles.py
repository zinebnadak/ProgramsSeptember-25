class Prectangles:
    def __init__(self, x=0, y=0, height=0, lenght=0):       # constructor for creating a rectangle
        self.x = x
        self.y = y
        self.__height = height   # __ after . sets to private
        self.__lenght = lenght   # private

    # Getter and Setter for height
    def get_height(self):
        return self.__height

    def set_height(self, new_height):       #called  "setter method" (set_height, set_length) ,allows you to update the private variable in a controlled way.
        self.__height = new_height   # simply updates the private variable __height

    # Getter and Setter for length
    def get_lenght(self):
        return self.__lenght

    def set_lenght(self, new_lenght):       #setter method
        self.__lenght = new_lenght   # simply updates the private variable __length



    # Methods
    def area(self):
        return self.__height * self.__lenght

    def circumference(self):
        return 2 * (self.__height + self.__lenght)

    def __str__(self):
        return f"Rectangle at ({self.x}, {self.y}) with height {self.__height} and length {self.__lenght}"
