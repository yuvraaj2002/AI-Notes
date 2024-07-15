This  page is dedicated towards understanding the concept of file handling in python and the main resources used for this topic are mentioned below

- [How computer memory works](https://www.youtube.com/watch?v=p3q5zWCw8J4)
- [CampusX File handling](https://www.youtube.com/watch?v=o-TAYRMQzIQ)
- [Selenium Udemy course](https://www.youtube.com/watch?v=o-TAYRMQzIQ)


Before actually understanding how we can actually do file handling using python we must first be aware about what are the types of data with which we deal with when performing the input output operation.

#### Types of Input Output data

When performing the input output operation there are basically 2 different types of data with which we deal with and these are 
- Text data 👉🏻 Sequence of Unicode characters. Example: In 1234 character `'1'` has a Unicode value of U+0031
- Binary data 👉🏻 Binary data is a sequence of bytes where every byte is normally made of 8 bits. Images, videos, audio files, executable files all are examples of binary data.

#### What operations can we perform on files

There are overall 4 operations which we can perform on the files and these are : Open a file, read data from the file , write data into a file, close a file. Now in order to understand each of these things we will simply see some of the codes where we will first be dealing with the text file and then with binary file. But before that let's first understand what is context manager ? 

#### What is context manager ? 

Context manager is basically a functionality offered to us by python programming language for efficient resource management. Basically in the absence of the context manager we would have to programmatically close the file after completing the the operation to free up the space in RAM and also to ensure the security.

But with context manager we don't need to care about closing the file after operation because it automatically close the file afterwards the operations.


#### How file travels from secondary memory ? 

Now finally before moving to how we can perform the read and write operation let us also understand how files are processed. Basically the steps followed are 

1. First the operating system loads the file from the secondary memory to RAM
2. After that in the RAM itself , a small temporary portion is allocated to store the data of the file before it's processed or used by the program.
3. The small temporary portion is called buffer memory and it optimize read and write operations.


#### When to use write and when to use writelines

In case we want to write a single string into an file we can use write but if we want to write multiple lines in that case we can use the writelines. Also another thing to keep in mind is that we want to add some data into existing file without overwriting then we must open the file in append mode rather than write mode.

```python
# This will create a new file and write contents into it
with open("Sample_small.txt",'w') as f:
    f.write("Yuvraj Singh")

# To append the data to existing file without overwriting it we can use append mode
with open("Sample_small.txt",'a') as f:
    f.write("\nAishveer Singh")

contents = ['\nGurpreet Singh','\nNavkiranjit Kaur']

# To append multiple lines into the file we can use write lines
with open("Sample_small.txt",'a') as f:
    f.writelines(contents)
```

#### When to use read and when to use readline

In case we want to directly load the complete data in the RAM itself in one go in that case we use the read, but incase the size of data is very big and our RAM size is limited then we can read the contents from the file in line by line manner and for this we can use the readline. 

- tell () : Used to get the current position of buffer pointer
- seek() : Used to adjust / repoint the buffer pointer

```python
# To load only subset of characters
chunk_size = 5
with open("Sample_small.txt",'r') as f:

    print(f.read(chunk_size))
    print("Current buffer pointer 1st load",f.tell()) # Should be at 5

    # This will laod next 5 characters
    f.read(chunk_size)
    print("Current buffer pointer 2nd load",f.tell()) # Should be at 10

    # Repointing the buffer pointer to 0
    f.seek(0)
    print("Current buffer pointer after repointing",f.tell()) # Should be at 0
```

```python
# If we want to read the data line by line
with open("Sample_long.txt",'r') as f:
    print(f.readline())

# If we want to read the data in chunks
chunk_size = 20
with open("Sample_long.txt",'r') as f:
    chunk = f.read(chunk_size)
    while chunk:
        print(chunk)
        chunk = f.read(chunk_size)
```


#### Why don't we always using the text files

The major drawback of text files is that they can only read or write Unicode characters, so in case we want to store some complex data structures such as dictionary, custom objects, images, files, audio files then we won't be able to do so and for that we need to use binary files. When dealing with binary files everything will remain same just the thing is that we will be using rb or wb as read binary and write binary mode in open function.

![[Pasted image 20240709102937.png|500]]

In the above example since we can see that if we want to write and read complex python data structures, then we need to make them as string and after doing so, when we will read them back we will lost them, so the only way we can deal with them is to [[Serialization and Deserialization]] of  the python objects.

- Talk about creating xPATH using tags as well as sometimes the attributes might not be present
- In Xpath we give the slash but in Css we give the space only
- Also in Xpath we use simple index but in Css we use nth-child 
![[Pasted image 20240709121741.png]]

- Servers are machines that understand IP addresses, interact with DBMS (Database Management Systems), perform computations on the data provided by the DBMS, and then return the data to users in the form of data packets over IP.

- CDNs are large-scale networks designed for global content distribution and performance optimization. Cache servers are typically used within specific applications or networks.