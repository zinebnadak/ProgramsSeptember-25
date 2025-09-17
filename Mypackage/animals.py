#this file has functions related to animals

def fav_animal():
    return "Cat"

def list_of_animals():
    return ["Dog", "Cat", "Elephant", "Fox"]

def is_mammal (animal):
    mammals = ["Dog", "Cat", "Elephant", "Fox"]
    return animal in mammals

if __name__== "__main__":
    print(list_of_animals())    # This runs only when the file is executed directly

