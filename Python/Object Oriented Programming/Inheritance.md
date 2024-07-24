This page is dedicated towards understanding the concept of Inheritance in Object Oriented Programming in Python and the resources used for understanding will be linked below.

##### What do you mean by inheritance and what is the need for this

Inheritance is basically a type of relationship that the classes can have between them and in inheritance classes share a parent child relationship where the child class also called sub class will inherit the characteristics or properties of the parent or super class. There are couple of benefits of implementing inheritance

- Our Code becomes more manageable and helps to prevent code redundancy because there is a possibility that our application might be having some common component, so rather than re-writing the same piece of code we can actually create a parent class and then the child classes can inherit that functionality from that parent class.
- Other than this, because of inheritance we can also abstract the low level details and make the things seem less complex.

##### What do you mean by instance variable show with example

Instance variables are those variables whose values are specific and unique to every instance. For example take a look at the code below

```python
class Person:

  # Defining the constructor
  def __init__(self,name):
    self.__name = name

  # Defining the getter function to access the private variable
  def show_name(self):
    return self.__name

obj1 = Person('Yuvraj')
obj2 = Person('Tanish')

print("Object 1 name : ",obj1.show_name())
print("Object 2 name : ",obj2.show_name())
```


##### What do you mean by class variables how they are different from the instance variable and why they are used ? 

Class variables are those variables whose value is shared among all the instances of the class and are independent of the instances of the class and because of this we use the class name to access them rather than using the object or self. Incase we will not pass self in the function then it will automatically will be regarded as the static method.

*Static variable are used in those scenarios where we want to define some *

```python
class Inheritance:

    # Defining the static variable using single underscore
    counter = 0

    def __init__(self):
        Inheritance.counter += 1  # Use class name to access the class variable

    def get_counter():
        return Inheritance.counter  # Static method to access the class variable

    def change_value():
        Inheritance.counter = 2

# Creating instances of the class
obj1 = Inheritance()
obj2 = Inheritance()
obj3 = Inheritance()

# Accessing the counter using the static getter
print(Inheritance.get_counter())

Inheritance.change_value()

# Accessing the counter using the static getter
print(Inheritance.get_counter())
```

##### Can we access the static variable with the instance of class ? 

Yes since the class variable is shared among all the instances of the class so we can access them using the instance of the class as well, but it is always recommended to access them using the class name.
##### What are the types of inheritance ? 

There are 5 different types of inheritance and all such types are mentioned below 

1. Single: There are only 2 classes, one is parent and other is child
2. Multiple : There are more than 1 parent class but there is only single class
3. Multi-level : In this architecture the parent class itself have parent class
4. Hierarchical: In this type of inheritance we can see a tree like hierarchical structure
5. Hybrid: This is basically combination of existing inheritance architectures

##### Answer the Questions

##### What is the use of super keyword ? 

##### How to deal with diamond style ambiguity in inheritance ? 




\
7. What is method overriding and method overloading?
8. What are abstract classes and interfaces in Python?

10. How does polymorphism work in Python?

### Advanced Questions

11. What are dunder/magic methods in Python?
12. How do you implement operator overloading in Python?
13. What is a metaclass in Python?
14. What is the difference between composition and inheritance?
15. How do you implement design patterns in Python?

### Practical Questions

16. Write a Python class to represent a `BankAccount` with deposit and withdrawal methods.
17. Create a class hierarchy for different types of vehicles (e.g., Car, Truck, Motorcycle) with common methods and attributes.
18. Design a Python class to represent a `Library` which can add, remove, and search for books.
19. Implement a `Shape` class with subclasses for different shapes (e.g., Circle, Square, Rectangle) and a method to calculate area for each shape.
20. Write a Python program using OOP principles to manage a simple inventory system.

### Conceptual Questions

21. What are the advantages of using OOP in Python?
22. Explain the SOLID principles in OOP.
23. How do you handle exceptions in Python OOP?
24. What is the role of the `super()` function in Python?
25. How can you make a class immutable in Python?

### Real-World Scenarios

26. How would you design a data pipeline using OOP principles?
27. Discuss how you would use OOP to model a machine learning pipeline.
28. Explain how you would implement a microservice using OOP in Python.
29. How would you refactor a large procedural codebase into an object-oriented one?
30. Discuss the role of OOP in designing scalable data science applications.