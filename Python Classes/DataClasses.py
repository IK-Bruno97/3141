#data class auto implements __repr__ and __eq__
from dataclasses import dataclass, field

import random

#creating immutable class attributes/data with dataclasses
#frozen prevents the attr to be modified within and outside the class
@dataclass(frozen=True)
class Immutable:
    value1 : str = 'Value_1'
    value2 : int = 0

    def somefunc(self, newVal):
        self.value2 = newVal

immutable = Immutable()
#im.value2 = 4 FrozenError
#immutable.somefunc(4) FrozenError
print(immutable)

@dataclass
class Book:
    '''title : str
    author : str
    pages : int
    price : float'''

    #can provide default values in 3 ways
    #NB: default values have to come first before non-default

    #1. directly.
    '''title : str = "No  title"
    author : str = "No author"
    pages : int = 0
    price : float = 0.0'''

    #2. dataclasses.field
    '''title : str = "No  title"
    author : str = "No author"
    pages : int = field(default=1.0)
    price : float = field(default=1.0)'''

    def price_func():
        return float(random.randrange(20, 40))

    #3. use a function
    price : float = field(default_factory = price_func)
    title : str = "No  title"
    author : str = "No author"
    pages : int = 0
    

    def bookinfo(self):
        return '{}, by {}'.format(self.title, self.author)


#b1 = Book("What the Dog saw", "Malcolm Gladwell", 490, 39.95)
#b2 = Book("Blink", "Malcolm Gladwell", 390, 31.15)
#b3 = Book("Blink", "Malcolm Gladwell", 390, 31.15)
#print(b1 == b2)
#print(b2==b3)
#print(b2.bookinfo())

b1 = Book()
print(b1)