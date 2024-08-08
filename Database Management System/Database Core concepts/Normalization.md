This page is dedicated towards understanding the concept of normalization in databases and the main resources used for this topic are mentioned as,

- [Love Babbar Normalization lecture](https://www.youtube.com/watch?v=nweGaymEwGM)
- [Love Babbar lecture notes](https://drive.google.com/drive/folders/1vJuJLGSskrNM29z9SgJMg3NfX7CuPjvm)

#### Small introduction to functional dependency

1. Reflexive
	- If ‘A’ is a set of attributes and ‘B’ is a subset of ‘A’. Then, A→ B holds.
	- If A ⊇ B then A → B.
3. Augmentation
	- If B can be determined from A, then adding an attribute to this functional dependency won’t change anything.
	- If A→ B holds, then AX→ BX holds too. ‘X’ being a set of attributes.
4. Transitivity
	- If A determines B and B determines C, we can say that A determines C.
	- if A→ B and B→ C then A→ C.


##### What is normalization and what is its need

Normalization is basically a database optimization technique which used to deal with the issues created by data redundancy such as 

- Inefficient storage memory utilization
- Anomalies (Insertion, Deletion, Updation)

The overall idea behind the normalization is to breakdown larger tables into smaller tables and linking them in such a way that promotes efficient storage utilization and prevent any kind of anomalies. There are 4 different level of normalization 1NF,  2NF, 3NF and BCNF.


##### What is the harm if we will keep everything into a single table ? 

- The redundant data will exist
- We will suffer from anomalies such as Insertion, Updation and Deletion anomaly


##### Talk about 1 Normal form 

In 1 normal form our entire focus is to make sure that all the attribute stores atomic values only.

![[Pasted image 20240708094034.png|250]]
##### Talk about 2 Normal form 

2 form of normalization is built on top of 1st form of normalization , so before applying this we need to make sure that our table is 1 way normalization and after that the main focus is to make sure that there there are no partial dependencies.

Where partial dependency means that if there exist some relation between composite primary key attribute and non primary key attribute then the Non primary key attribute should be be fully dependent on the composite primary key and not on part of the primary key.

![[Pasted image 20240708095020.png|300]]

##### Talk about 3 Normal form 

Just like 2nd form of normalization is built on top of 1st form of normalization so just like that 3rd form is built on top of 2nd form and after dealing with partial dependency, in this form we need to make sure that there is no transitive dependency, which in simple words means that non prime key attribute should not be dependent on non prime key attribute.

##### Talk about BCNF Normal form 

This is also called Boyce Codd normal form and in this first of all the table must be 3 form normalized and after that we need to make sure that if there exist a functional dependency between A -> B then A should be super key only, which means that we need to make sure that prime attribute is not derived from any other prime or non prime attribute.

##### What is denormalization and why it is done 

Denormalization is simply the opposite of normalization and in this we simply reduce the normalization conditions on the tables and by doing so even though we might get data redundancy by combining by smaller tables into larger tables but the main advantage is that we get low latency of the read operations which might be more important in some scenarios such as Social Media Sites.
