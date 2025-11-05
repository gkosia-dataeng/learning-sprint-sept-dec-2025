'''
    Problem: Based on a parameter i want to create either object of typeA or of typeB

    Solution: Create a Factory object that implement the __new__ magic method and take the type as parameter 
'''

from typing import Union

class Dog():
    
    def speak(self):
        print("Gav, i am a dog")



class Cat():
    
    def speak(self):
        print("Meow, i am a cat")



class PetFactory():
    def __new__(cls, pet_type):
        
        if pet_type == "dog":
            return Dog()
        elif pet_type == "cat":
            return Cat()
        
        raise Exception("Unsupported pet type, {pet_type} is not a valid pet")
    


d = PetFactory("dog")
d.speak()

c = PetFactory("cat")
c.speak()