#1 Define a Class that describes cars.
# Name the class "Car".
# One car vill have a registrationnumber,color, brand,year-model,curb weight, and engine power
#put the Class in a file Car.py
# When you run the program there wont happen anything bc it is not a complete program yet


class Car:      #A class to represent a car
    def __init__(self,owner, reg_num,brand,model,curb_weight,engine_power):       #The constructor method. It initializes the attributes of the Car object.
        self.owner = owner            #Assign correct attrubute to the object
        self.reg_num = reg_num
        self.brand = brand
        self.model = model
        self.curb_weight = curb_weight
        self.engine_power = engine_power

    def __str__(self):              #Important! tells Python to print as string when printed
        return (f"{self.owner}\n{self.reg_num}\n{self.brand}\n{self.model}\n{self.curb_weight}\n{self.engine_power}")


    #below Returns a string representation of the Car object.
    #This method is called when you print the object.
    #def __str__(self):
        #return(f"Registration Number: {self.reg_num}\n etc...")

