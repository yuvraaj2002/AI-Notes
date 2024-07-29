This page is dedicated towards understanding the concept of encapsulation in object oriented programming and the resources used for this topic will be linked below.

- [Encapsulation Blog](https://www.datacamp.com/tutorial/encapsulation-in-python-object-oriented-programming)

### [What is encapsulation in OOP and why is it important?](#)

Encapsulation is one of the feature of object oriented programming which focuses on bundling the class variables, the member functions and mechanism to interact with the crucial components (i.e. private variables or functions) into a single unit.

- If class have its class variables + Member functions + Mechanism to access crucial components then we call that class to be strongly encapsulated.
- If class have its class variables + Member functions but not any kind of Mechanism to access crucial components then we call that class to be loosely encapsulated.

### [How does encapsulation differ from abstraction?](#)

- Abstraction is all about hiding the complex low level details of an object and only focusing on what an object does rather than how that object does.
- Encapsulation is all about bundling everything into a single unit and making sure that the object internal state is protected from any kind of unauthorized access.

### [Explain the concept of access modifiers in Python (public, protected, private).](#)

Access modifiers are simply the keywords which helps us to control the visibility or accessibility of the class variables or member functions outside the class. Basically Python does not enforce a very strict access control just like other languages.

##### Public class members
Public members are accessible from anywhere, both inside and outside the class.

```python
class MyClass:
    def __init__(self):
        self.public_var = "I am public"

    def public_method(self):
        return "This is a public method"

# Usage
obj = MyClass()
print(obj.public_var)  # Output: I am public
print(obj.public_method())  # Output: This is a public method

```

##### Protected class members

Protected class members are intended to be accessed only within the class and by its subclass only but not outside the class. We can convert make any class member to be protected by using `single underscore`.

`Note`: We are using the word `INTENDED` to use within the class and by its subclass, but in case we are aware about the class member 

```python
class MyClass:
    def __init__(self):
        self._protected_var = "I am protected"

    def _protected_method(self):
        return "This is a protected method"

class SubClass(MyClass):
    def access_protected(self):
        return self._protected_var

# Usage
obj = MyClass()
print(obj._protected_var)  # Output: I am protected (accessible, but should be avoided)
print(obj._protected_method())  # Output: This is a protected method (accessible, but should be avoided)

sub_obj = SubClass()
print(sub_obj.access_protected())  # Output: I am protected

```


##### Private class members

Private members are intended to be used only within the class and we can make a class member to be private by using `doube underscore`. Python prevents the access of private class member outside the by using name mangling, where the class member name is modified by adding class name at the front.

`Note` Since python do not enforce strict access control so one can still access the private class member outside the class by using the syntax $_Classname__privateClassMember$

```python
class MyClass:
    def __init__(self):
        self.__private_var = "I am private"

    def __private_method(self):
        return "This is a private method"

    def access_private(self):
        return self.__private_method()

# Usage
obj = MyClass()
# The following lines will result in an AttributeError
# print(obj.__private_var)
# print(obj.__private_method())

# Accessing private members through name mangling
print(obj._MyClass__private_var)  # Output: I am private
print(obj._MyClass__private_method())  # Output: This is a private method

# Accessing private member through a public method
print(obj.access_private())  # Output: This is a private method
```

### [What is the purpose of getter and setter methods in encapsulation, and how are they implemented in Python?](#)

Getter and Setter are simply the member functions which are used to provide a controlled access to crucial components of an object, where crucial components means protected and private class members.

- Getter function is used to access the values of crucial class members
- Setter function is used to update the value of crucial class members

```python
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  # Public attribute
        self.__balance = balance              # Private attribute

    # Getter method for balance
    def get_balance(self):
        return self.__balance

    # Setter method for balance
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid balance amount")

# Usage
account = BankAccount("123456789", 1000)
print(account.get_balance())  # Output: 1000

account.set_balance(1500)
print(account.get_balance())  # Output: 1500

account.set_balance(-500)  # Output: Invalid balance amount

```

### [Practice Problems](#)

-  Create a class `BankAccount` with private attributes for balance and methods for deposit and withdrawal. Ensure that the balance cannot be directly accessed or modified from outside the class.
- Define a class `Car` with private attributes for make, model, and year. Implement properties to access and modify these attributes, ensuring that changes are valid (e.g., the year should be positive).
- Implement a class `Student` with private attributes for student ID and grades. Provide methods to add grades and calculate the average, while keeping the grades hidden from direct access.