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
        print("Retrieving age.")
        return self.age

    def set_age(self, age):
        print(f"Setting age to { age }")
        self.age = age
    
    age = property(get_age, set_age)

