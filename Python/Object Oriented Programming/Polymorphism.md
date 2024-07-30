This page is dedicated towards understanding the concept of polymorphism in object oriented programming and the resources used will be indexed below.


### [What is polymorphism in object-oriented programming?](#)

Polymorphism is one of the feature of object oriented programming which allow functions or operators with the same name to be executed on different objects.

- Polymorphism supports dynamic method resolution, meaning the method to be invoked is determined at runtime. This allows for dynamic and adaptable behavior, making it easier to implement sophisticated software designs such as design patterns.

### [What are the different types of polymorphism in Python?](#)

- `Compile time polymorphism` : It is also known as Static polymorphism and it is achieved through the operator overloading and function overloading.

```python
class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

math_op = MathOperations()
print(math_op.add(1, 2))       # This will raise an error because the second method overrides the first
print(math_op.add(1, 2, 3))    # Output: 6

```

- `Run time polymorphism` : It is also known as Dynamic polymorphism and it is achieved through the function overriding.

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Output: Woof! Meow!

```

### [Explain Operator overloading, Function overloading and Function overriding](#)

- Operator Overloading: It comes under compile time polymorphism and according to this based on the type of object or operands, the same operator behaves differently.

- Function Overloading : It comes under compile time polymorphism and according to this if we can define multiple function with the same name but different parameters (In terms of count and type). Also the decision about which function to call is made during the compilation.

- Function overriding : It comes under run time polymorphism and according to this if 2 functions with the same name and parameters are defined in parent-child class then the function defined in the child class will override the parent class function.


5. How does the `__str__` method demonstrate polymorphism in Python?
### [Can you give an example of polymorphism using interfaces or abstract classes?](#)

```python
from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Function to demonstrate polymorphism
def print_shape_info(shapes):
    for shape in shapes:
        print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")

# List of different shapes
shapes = [Rectangle(4, 5), Circle(3)]
print_shape_info(shapes)

```

### [Explain the role of the `super()` function in method overriding.](#)

When you override a method in a subclass, you may still want to call the method from the parent class. `super()` allows you to access and invoke the parent class's method.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()  # Call the parent class method
        print("Dog barks")

# Example usage
dog = Dog()
dog.speak()

```
### [How can you prevent method overriding in Python?](#)

```python
from typing import final

class Base:
    @final
    def final_method(self):
        print("This method cannot be overridden.")

class Derived(Base):
    def final_method(self):
        # This will raise a type checker warning, but not an error
        print("Attempt to override final_method.")

# Example usage
obj = Derived()
obj.final_method()

```

### [Code Exercises](#)

1. Implement a base class `Shape` with derived classes `Circle` and `Square`. Demonstrate polymorphism by implementing an `area` method.
2. Create a class `Animal` with a method `speak`. Implement subclasses `Dog` and `Cat` that override the `speak` method.
3. Write a Python program that uses operator overloading to compare two custom objects based on their attributes.
4. Design a class hierarchy for a vehicle rental system that includes cars, bikes, and trucks. Use polymorphism to implement a method that calculates the rental cost.
5. Create an abstract class `Employee` with an abstract method `calculate_salary`. Implement subclasses `FullTimeEmployee` and `PartTimeEmployee` that provide their own implementations of `calculate_salary`.