This page is actually dedicated towards understanding the concept of Partitioning and Sharding in database and the resources used for this topic is this Google drive.

[Love Babbar Lecture 18 ](https://drive.google.com/drive/folders/19WIVAOZzQxfIVCOQCaaa6Jtg_ctTrO8p)
[Ankit Bhayani](https://www.youtube.com/watch?v=wXvljefXyEo)

##### What is the need of these ? 
Basically both partitioning and sharding are the database optimization technique which are used in those kind of scenarios where we want to improve the performance of the database in term of data accessibility speed, because when our application is catering millions of user then it is very common to experience degradation in the throughput of the database.

![[Pasted image 20240706193407.png]]


##### What is partitioning and what are its types ? 
Partitioning is a technique where we divide the database into smaller manageable chunks called partitions and this distribution of data among the partitions actually helps us to optimize the database performance in terms of data retrieval.

![[Pasted image 20240706185831.png|300]]

Also by doing partitioning we can actually reduce the cost, which we would have to bear for doing [[Scaling Patterns]] and that is either scaling up or scaling. So there are basically 2 different types of partitioning 

- Horizontal partitioning : In this we divide the rows of the database into multiple partitions
- Vertical partitioning : In this we divide the columns of the table into multiple partitions and each partition contains the subset of the columns

Since the partitioning is done on the data level so we can have multiple partitions on the same database

##### What is sharding 
Sharding is a specific type of horizontal partitioning where divide the rows of the tables in database into multiple database instances. The database instances in this case are called shards.

The way it is different from partitioning is that incase of partitioning the rows the table are divided and distributed among the partitions which are present on the same machine, but in case of sharding the shards are present on different machines.

![[Pasted image 20240706195524.png]]
![[Pasted image 20240706195948.png]]

#### Drawback of sharding 

The major drawback of sharding is that in case of data which we want to retrieve is spread across multiple shards then it becomes complex and expensive to retrieve the data. So whenever we are dong sharding we always make sure that the data is distributed among the shards in such as way that all the queries could be answered for that shard only.