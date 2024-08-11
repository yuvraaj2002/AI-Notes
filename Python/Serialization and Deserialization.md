This page is dedicated towards understanding the concept of serialization and deserialization in python. So the resources that I will be using will be linked below.

### [What is the difference between serialization and deserialization](#)

`Serialization` : It is the process of converting the object or data structure into some structured format such as JSON. The main purpose of serialization is to save the state of an object or data structure so that it can be stored in a file, sent over a network, or saved in a database.

`Deserialization` : Deserialization is the process of converting serialized data back into its original object or data structure.

### [Give python code to serialize and deserialize the Python objects using JSON module](#)

```python
import json

# Defining the list
L = [1,2,3,4]

with open('demo.json','w') as f:
  json.dump(L,f)

# Defining the dictionary
d = {
    'name':'nitish',
     'age':33,
     'gender':'male'
}

with open('demo.json','w') as f:
  json.dump(d,f,indent=4)
```

After serializing the python object if we want to deserialize it back then we can actually use the `json.load()` method.

```python
# deserialization
import json

with open('demo.json','r') as f:
  d = json.load(f)
  print(d)
  print(type(d))
```


### [Give python code to serialize and deserialize the Python objects using pickle](#)

```python
import pickle

data = {"name": "Yuvraj", "age": 25}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)


with open("data.pkl", "rb") as f: 
	data = pickle.load(f) print(data) 
	# Output: {'name': 'Yuvraj', 'age': 25}
```

### [What is the difference between Pickle and JSON](#)

- Pickle module stores the object or data structure into binary data
- JSON module stores the object or data structure into the human readable format.