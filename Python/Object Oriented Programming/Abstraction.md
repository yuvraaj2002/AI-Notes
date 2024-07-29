This page is dedicated towards understanding the concept of abstraction in Object oriented programming in Python and the sources used for this topic will be linked together.

- [Abstraction in OOP by W3Source](https://www.w3resource.com/python-interview/what-is-abstraction-in-oop-python.php)


### What is abstraction in OOP, why is it important and how do we achieve it ?

Abstraction in Object oriented programming is a concept where we hide or abstract the low level details and focus on what an object does rather than how it does it. Abstraction is done for simplification of complex system and to make the maintenance easy.

In python Abstraction can be achieved through `abstract` class and `interface` where,

- abstract class is used to define the blueprint for the other classes to inherit from and it cannot be instantiated on its own.
- Interface is used to define the contract that all subclasses classes must follow and implement. The abstract methods are used to define the interface

### How does abstraction differ from encapsulation?

- **Abstraction**: Here we hide or abstract the low level details and focus on what an object does rather than how it does it.
- **Encapsulation**: Here we focus on hiding the internal state of an object and protecting it from unauthorized access.

### How do we create abstract class in python and what do you mean by abstract methods? 

In python the `abc` module contains `ABC` base class which is inherited to create the abstract class. Also the member functions of an abstract class are called abstract methods and the unique thing about such methods is that they are only declared in the abstract class using `@abstractmethod` decorator but there is no implementation of such methods because they are used to define the interface or contract of the abstract class that all subclasses must follow.

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


# Defining the base class
class Dog(Animal):
    def make_sound(self):
        print("Bark")

    def move(self):
        print("Run")


# Instantiate subclasses
dog = Dog()

# Using the interface defined by abstract methods
dog.make_sound()  # Output: Bark
dog.move()        # Output: Run
```


### Can an abstract class have concrete (non-abstract) methods? Explain with an example and also can we instantiate abstract class on its own

Yes an abstract class can have both abstract and non abstract method (also called concrete method) with implementation and generally the non abstract methods are used to enforce some default functionality. And the answer to second query is that "No can we cannot instantiate abstract class of its own"

```python
from abc import ABC, abstractmethod

# Abstract class with both abstract and concrete methods
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        print(f"This is shape with area {self.area()} and perimeter {self.perimeter()}.")

# Concrete subclass implementing the abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Usage
rectangle = Rectangle(10, 5)
rectangle.describe()  # Output: This is shape with area 50 and perimeter 30.
```


### Can an abstract class inherit from another abstract class in Python? Provide an example.

Yes, an abstract class in Python can inherit from another abstract class. When an abstract class inherits from another abstract class, it can extend the functionality or add additional abstract methods to the inherited methods. Subclasses of the derived abstract class must implement all abstract methods from both the base abstract class and the derived abstract class to be instantiated.

```python
from abc import ABC, abstractmethod

# Base abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Method that all animals must implement to make a sound."""
        pass

    @abstractmethod
    def habitat(self):
        """Method that all animals must implement to describe their habitat."""
        pass

# Derived abstract class
class Mammal(Animal):
    @abstractmethod
    def has_fur(self):
        """Method to check if the mammal has fur."""
        pass

# Concrete class
class Dog(Mammal):
    def sound(self):
        return "Bark"

    def habitat(self):
        return "Domestic"

    def has_fur(self):
        return True

# Attempting to instantiate an abstract class will raise an error
try:
    animal = Animal()  # This will raise a TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    mammal = Mammal()  # This will also raise a TypeError
except TypeError as e:
    print(f"Error: {e}")

# Correctly instantiate a concrete class
dog = Dog()
print(f"Sound: {dog.sound()}")  # Output: Sound: Bark
print(f"Habitat: {dog.habitat()}")  # Output: Habitat: Domestic
print(f"Has Fur: {dog.has_fur()}")  # Output: Has Fur: True

```


### What is the difference between abstract class and concrete class ? 

| Abstract class                                                                                                 | Concrete class                                                                                                  |
| -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Abstract class is used to define the blueprint for all its subclasses and it cannot be instantiated on its own | Concrete class can be instantiated on its own                                                                   |
| It contains the abstract methods (for defining the interface) which are only declared but not implemented      | It contains the implementation of all its member function including those inherited from abstract base classes. |


