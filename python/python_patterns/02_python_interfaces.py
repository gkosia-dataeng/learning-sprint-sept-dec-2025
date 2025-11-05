'''
    Problem: Implement Interface class to make sure that the derived classes implement specific methods
            Python does not have Interface like other OOP languages
    
    Solution: Use abc module to implement interface
'''

from abc import ABC, abstractmethod


class ExampleInterface(ABC):

    @abstractmethod
    def must_implement(self):
        pass


class Child(ExampleInterface):

    def another_method(self):
        print("This is another method")



c = Child()