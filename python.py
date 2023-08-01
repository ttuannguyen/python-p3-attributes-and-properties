# ATTRIBUTES

# class Human:
#     species = "Homo sapiens" # class attribute
#     def __init__(self, name):
#         self.name = name


# guido = Human("Guido") # instance
# guido.species = "Python programmer"
# guido.name = "Tuan Nguyen"

# # adding new attributes using dot notation
# guido.nationality = "American"


# # print(guido.species)
# # print(guido.name)
# # print(guido.nationality)

# # print(Human.name) # error bc name is an instance attribute

# my_attr = "is_a_friend"
# getattr(guido, my_attr, False) 
# setattr(guido, my_attr, True)
# print(getattr(guido, my_attr, False) )


# PROPERTIES

class Human:
    species = "Homo sapiens" # class attribute
    
    def __init__(self, age):
        self.age = age
    
    def get_age(self): 
        # compiled by the property fuction and prints the below when we access age through dot notation or an attr() function 
        print("Retrieving age.")
        return self._age

    def set_age(self, age):
        # compiled by the property fuction and prints the below when we change our human's age 
        if (type(age) in (int, float)) and (0 <= age <= 120):
            print(f"Setting age to { age }")
            self._age = age # underscore to tell people this is a "private" property and there are methods that depend on its name and values
        else:
            print("Age must be a number between 0 and 120.")
    
    age = property(get_age, set_age) # "age" property - this function compiles our getter and setter and calls them whenever anyone accesses our human's age

guido = Human(age=67)
guido.age = 0 
guido.age = False
guido.age = 66
guido.age