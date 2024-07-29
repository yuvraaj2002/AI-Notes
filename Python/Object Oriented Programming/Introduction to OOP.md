This page is dedicated towards understanding the concept of Object Oriented Programming in Python and the resources used for understanding will be linked below, other than this before moving on to the direct modules of OOP first we must be aware about the basics.

##### What is OOP and what is the need for this ? 

OOP stands for Object oriented programming and it is a type of programming style where we work with user defined datatypes along with primitive datatypes. Now the main reason behind using this style of programming is to enhance the code readability and implement the DRY principle of computer science.

##### What do you mean by class and object ?

- Class can simply be defined as the user defined data type 
- Object can be defined as the variable of the user defined datatype, which actually occupies some memory.

##### How do you create a simple class in python

```python
class learning:

    # Defining the constructor
    def __init__(self):
        self.age = 21
        self.name = "Yuvraj Singh"

    def walk(self):
        print("He Can Walk")

    def talk(self):
        print("He Can talk")

# Creating an object of the class (aka variable of user defined datatype)
person = learning()
print("Age of person : ",person.age)
print("Name of person : ",person.name)
person.walk()
person.talk()
```

##### What is the use of self and init keyword in Python ? 

- **self** is basically an object pointer and it is used to interact or access all the class variables and member functions inside the class, basically when we instantiate the class or class the member function of the class by using the object then internally the address of the object also gets passed and it is then stored in this self.
- **init** keyword is used to specify the constructor in the class, which is a special type of member function that is used for instantiating the class variables or setting up initial configuration of the class. In other languages such as C++ to specify the constructor we use the same name of the class for member function but in Python we simply need to use init keyword

#####  What are the types of relationship classes can have in OOP ? 

There are 2 types of relationship classes can have in the context of object oriented programming and these are ⬇️

- Aggregation (has a relationship): Example Customer has a address
- Inheritance

##### Write a Python Program to show aggregation operation

When we instantiate a container class we pass the object of the other class. Not only this in case of Aggregation relation there is no hierarchy but in case of inheritance there is parent child relationship.

![[Aggregation.png]]

```python
class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def display_address(self):
        print(f"Street: {self.street}, City: {self.city}, State: {self.state}, Zip: {self.zip_code}")

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def display_customer_info(self):
        print(f"Name: {self.name}, Email: {self.email}")
        self.address.display_address()

# Creating an address object
address = Address("123 Main St", "Anytown", "CA", "12345")

# Creating a customer object with the address object
customer = Customer("John Doe", "john.doe@example.com", address)

# Displaying customer information
customer.display_customer_info()
```
##### Foundational Concepts of Object Oriented Programming

Now since we are aware about the basics of the Object Oriented programming so let us now look at the building blocks of Object oriented programming

- [[Inheritance]]
- [[Polymorphism]]
- [[Encapsulation]]
- [[Python/Abstraction]]