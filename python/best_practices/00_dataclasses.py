'''Dataclasses are classes design to hold only data values
   They dont have any methods

'''

from dataclasses import dataclass
from typing import Tuple, List

@dataclass
class Person():
    name: str 
    age: int
    height: float


p = Person(name='Gab', age=34, height=1.67)

print(p)


@dataclass
class CompexPerson():
    name: str
    friends: List[str]
    lucky_numbers: Tuple = (4,7)

c = CompexPerson(name = 'Gab', friends=['me', 'you'], lucky_numbers=(5,6,7))

print(c)


# dataclasses can inherit from others
@dataclass
class Man(Person):
    job: str

m = Man(name='Gab', age=34, height=1.8, job='IT')
print(m)