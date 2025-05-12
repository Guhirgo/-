from collections import namedtuple


def say_hi (name, age):
    

Person = namedtuple('Person', ['name', 'age'])

person = Person(name='Alex', age=32)