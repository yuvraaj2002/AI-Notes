This page is dedicated towards understanding the concept of Namespace in python and the resources used for this topic will be mentioned below

- [CampusX Code File](https://colab.research.google.com/drive/1P5jtGzaVkIjEFFr6WSrzs0capal32QPn?usp=sharing)


### [What do you mean by namespace and what are its types](#)

Namespace can simply be defined as the space which stores the identifier and its value (object) in the key-value pair. We basically need to be aware about this concept so that we could actually prevent any kind of naming collision in large codebase.

In python there are 4 different types of namespace 

1. Local namespace
2. Enclosed namespace
3. Global namespace
4. Built-in namespace

![[Namespace Intro.png]](https://github.com/yuvraaj2002/AI-Notes/blob/master/Python/Images/Serialization_Need.png)

In the above image the `temp` and `name` are part of global namespace whereas `a` is part of the local namespace.

### [What do you mean by scope in python and what are the various scopes?](#)

Scope is simply a region where the namespace is directly accessible and just like namespaces, scopes also have 4 types

1. Local Scope
2. Enclosed Scope
3. Global Scope
4. Built-in Scope

### [Define LEGB Rule](#)

According to LEGB rule in python, the python interpreter looks for the identifier from bottom up fashion which means from local scope towards the built-in scope. To better understand this let us take a look at the Python Programs.

##### [Local Scope](#)

```python
def temp():
    
    # Variable a is part of local scope
    a = 10
    
name = "Yuvraj Singh"
temp()
print(a) # This will raise NameError
```

##### [Global Scope](#)

```python
# Variable b is part of global scope
b = 20

def temp():
    
    # Variable a is part of local scope
    a = 10
    print("Printing a in local scope",a)

	# Interpreter will look for b in E,G,B scope
    print("Prinitng b while in local scope",b)
    
name = "Yuvraj Singh"
temp()
print("Prinitng b while in Global scope",b)
```

##### [Enclosed Scope](#)

```python
# Variable b is part of global scope
b = 20

def temp():
  c = 40

  def inner():
    # Variable a is part of local scope
    a = 10
    print("Printing a in local scope",a)
  
  inner()
  print("Prinitng c in enclosed scope",c)  

name = "Yuvraj Singh"
temp()
print("Prinitng b in global scope",b)
```

##### [Built-in Scope](#)

```python
# Variable b is part of global scope
b = 20

def temp():
  c = 40

  def inner():
    # Variable a is part of local scope
    a = 10
    print("Printing a in local scope",a)
  
  inner()
  print("Prinitng c in enclosed scope",c)  

name = "Yuvraj Singh"
temp()
print("Prinitng b in global scope",b)
print("Using Built-in length function",len(name))
```

### [While being inside some scope can we access higher namespace identifier? ](#)

Yes we can access the higher namespace while being inside the name space which comes lower. To understand this 

```python
# Variable b is part of global scope
b = 20

def temp():
  c = 40

  def inner():

    # Variable a is part of local scope
    a = 10
    print("Accessing the enclosed scope variable",c)
    print("Accessing the global scope variable",b)
  
  inner()

name = "Yuvraj Singh"
temp()
```

### [While being inside some scope can we update higher namespace identifier ?](#)

Even though it is not recommended to update higher namespace identifier while being inside the lower scope but still we can update them by using the keyword `global` and `nonlocal` accordingly.

```python
# Variable b is part of global scope
b = 20

def temp():
  c = 40

  def inner():

    # Variable a is part of local scope
    a = 10

    # Updating the global namespace
    global b
    b = b + 40
    print("Accessing the global scope variable afte updation",b)

    # Updating the global namespace
    nonlocal c
    c = c + 40
    print("Accessing the enclosed scope variable after updation",c)
    
  inner()

name = "Yuvraj Singh"
temp()
```


### [While being inside some lower scope can we create a identifier in higher scope ? ](#)

```python
def temp():
  
  def inner():

    # Variable a is part of local scope
    a = 10

    # Creating the identifier in global namespace 
    global d
    d = 40
    print("Global identifier",d)
    
  inner()

name = "Yuvraj Singh"
temp()
```

Also the point to keep in mind is that we cannot actually create the enclosed namespace identifier while being inside the local scope.

[Python Tutor Visualizer](https://pythontutor.com/render.html#code=def%20temp%28%29%3A%0A%20%20%0A%20%20def%20inner%28%29%3A%0A%0A%20%20%20%20%23%20Variable%20a%20is%20part%20of%20local%20scope%0A%20%20%20%20a%20%3D%2010%0A%0A%20%20%20%20%23%20Creating%20the%20identifier%20in%20global%20namespace%20%0A%20%20%20%20global%20d%0A%20%20%20%20d%20%3D%2040%0A%20%20%20%20print%28%22Global%20identifier%22,d%29%0A%20%20%20%20%0A%20%20inner%28%29%0A%0Aname%20%3D%20%22Yuvraj%20Singh%22%0Atemp%28%29&cumulative=false&curInstr=10&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
