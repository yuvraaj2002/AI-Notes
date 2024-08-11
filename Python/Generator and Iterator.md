This page is dedicated towards understanding the concept of Generator and Iterator in python and the resources used for this topic will be linked below.

- [Iterator in Python](https://github.com/campusx-official/python-iterators-and-iterables/blob/main/Iterators.ipynb)
- [Generator in Python]()

### [What do you mean by iteration ? ](#)

Iteration is a process of accessing the items of a sequence one after the another.

### [What is the difference between iterable and iterator ](#)

- Iterable : It is the object which can be iterated over by the iterator.
- Iterator : It is the object which is used to iterate over the iterable element by element without having to load complete data in one go in the memory.

```python
# num list is a iterable here
num = [1,2,3]

# For loop internaly creates iterator using iterable
for i in num:
    print(i)
```

### [Why do we even use the concept of iterator](#)

With the help of iterator we can actually iterator over the iterable element by element one at a time without having the need to load the complete data in the memory and with this we can actually deal with large size data, which we commonly encounter when we deal with deep learning. 

```python
import sys

# Defining the list
list = [item for item in range(1000000)]

# Comparing the size of list and iterator (bytes)
print(sys.getsizeof(list))
print(sys.getsizeof(iter(list)))
```

### [How to detect whether object is iterator or iterable ?](#)

To identify whether a python object is iterator or iterable we can simply use the `dir()` built-in method and this method will return us the list of special methods associated with the object.

##### [For Iterator](#)

If the list contains both the `__iter__` and `__next__` method then that object can be called as the iterator.

##### [For Iterable](#)

If the list contains only the `__iter__` method then that object can be called as the iterator.


### [If there is some iterable then how can we create a iterator using it ?](#)

By using the iter method we can actually create an iterator from the iterable.

```python
# num list is a iterable here
num = [1,2,3]

print(type(num))
print(type(iter(num)))
```

### [What would happen if we will create iterator of the iterator itself ? ](#)

We will get the same iterator object

```python
list = [item for item in range(100000)]

iterator1 = iter(list)
iterator2 = iter(iterator1)
print(id(iterator1))
print(id(iterator2))
```

### [Explain how for loop works](#)

- First of all the for loop creates an iterator using the iterable using the iter method
- Then it calls the next method of iterator object which return the value at current index and increment the iterator to the next index

```python
def mera_khudka_for_loop(iterable):
    
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break           

a = [1,2,3]
b = range(1,11)
c = (1,2,3)
d = {1,2,3}
e = {0:1,1:1}

mera_khudka_for_loop(a)
```

### [Write a python program to create own custom iterator](#)

Let's say we have created a user defined datatype and we want to add a functionality of iterating over the data stored into it, so for that we have 2 options 

1. In the user defined datatype (class) add the iter and the next method
2. Use generator for creating a iterator for custom object

##### Adding iter and next methods

```python
class CustomIterator:

  # Constructor to initialize class variables
  def __init__(self,start,end):
    
    self.start = start
    self.end = end

  # Function to return the iterator object
  def __iter__(self):
    return self


  # Function to return the next element
  def __next__(self):
    
    while self.start <= self.end:
      self.start += 1 
      return self.start-1
    raise StopIteration

  # Some functions of the class
  def some_operation(self):
    pass


# Creating an instance of class
instance = CustomIterator(1,5)

# Creating an iterator
iterator = instance.__iter__()

# Printing the items
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

# Here the error will be raised
print(iterator.__next__())
```