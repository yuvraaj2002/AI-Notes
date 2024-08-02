This page is dedicated towards understanding the concept of decorator in python and the resources used for this topic will be linked below.

- [Decorator in Python](https://www.datacamp.com/tutorial/decorators-python)

### [Why functions are called first class citizen](#)

In programming first class citizen are those entities which can be 
- Passed as an argument
- Return as a result from function
- Assigned to a variable
- Stored in the data structure

Since function can be passed as argument, returned as result from function, assigned to variable and can be stored in some other data structures thus function are called first class citizen.

### [What is a decorator in Python and how do they work?](#)

Decorator in python is simply a design pattern which is used to add functionality on top of existing object (usually functions) without modifying the structure.

```python
# Original base function
def func():
    print("My name is Yuvraj Singh")

# Defining the decorator
def decorator(func):

    # Defining the wrapper on top of existing function
    def wrapper():
        print("Before function call")
        func()
        print("After function call")

	# Returning after adding functionality
    return wrapper

decorated_func = decorator(func)
func()
```

Other than this we can also use the @syntax to define the decorator

```python
# Defining the decorator
def decorator(func):

    # Defining the wrapper on top of existing function
    def wrapper():
        print("Before function call")
        func()
        print("After function call")

    return wrapper

@decorator
def base_func():
    print("My name is Yuvraj Singh")

base_func()
```

3. Explain the difference between a function decorator and a class decorator.
4. Can a decorator be applied to a class method? If so, how?
5. What is the purpose of the `@wraps` decorator from the `functools` module?

### Practical Implementation Questions

1. How would you create a simple logging decorator in Python?
2. Write a decorator that counts the number of times a function is called.
3. Create a decorator that caches the results of a function to improve performance.
4. How would you write a decorator that times the execution of a function?
5. Write a decorator that validates the input types of a function.

### Advanced Questions

1. How can you create a decorator that takes arguments?
2. Explain how to use multiple decorators on a single function.
3. Discuss potential issues with decorators and how to handle them.
4. How would you write a class-based decorator?
5. Can you use decorators with lambda functions? Why or why not?

### Code Exercises

1. Implement a decorator that retries a function if it raises an exception, up to a maximum number of attempts.
2. Write a decorator that ensures a function is only called once.
3. Create a decorator that transforms the output of a function to uppercase.
4. Implement a decorator that measures the memory usage of a function.
5. Write a decorator that logs the arguments and return value of a function.