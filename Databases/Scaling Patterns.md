This page is dedicated towards understanding the concept of scaling in the databases.

- [Database scaling patterns](https://www.youtube.com/watch?v=SOrhyETsz6w&list=PLDzeHZWIZsTpukecmA2p5rhHM14bl2dHU&index=20&t=2s)
- [Understanding data scaling patterns blog ](https://www.freecodecamp.org/news/understanding-database-scaling-patterns/)


In order to truly understand the need of scaling patterns used in database we must first be truly aware about what is the need of database scaling at all. So let say that we have built some application and in the initial stage the number of customers which are use our application are small in number so upto this point our current database will be able to handle the read and write queries efficiently.

But let say now our user base have increased and the data being generated is also increasing, so with this change in the condition it will not be appropriate to directly use the distributed data centers to deal with issue instead there around 6-7 scaling patterns which we can try based on the requirement.

- Query optimization and Connection pooling
- Vertical scaling
- Command query segregation
- Multi Primary replication
- Partitioning 
- Horizontal Scaling
- Data Center wise partitioning

#### Query optimization and connection pooling

This is the very first scaling pattern which we can implement to improve the performance of our database, and the core idea is that rather than reading everything from the database why not store some data in the cache memory ?.

Now the question arises which data should be stored in the cache memory and which should be not. The simple answer is that all the non dynamic data should be stored in the cache memory and the example of such data could be some past history and introductory product details. Other than using cache memory we should also consider doing the denormalization of our database to reduce the time complexity of query performing join operation across multiple tables.

The above content was about the query optimization but other than this we also need to consider creating connection pool to improve the database performance. The idea behind connection pool is that generally in our code there might be multiple the need of connecting to database multiple times and if we will establish new connection everytime then the entire process will become slow and costly since it requires some back & forth communication between client & server.

![[Pasted image 20240707071430.png]]


#### Vertical Scaling or Scaling Up

Vertical scaling or scale up is another scaling pattern which is being used to improve the latency and throughput of the database and in this the core idea is to simply upgrade the hardware like RAM and disk space etc.

Practically the new machine with stronger hardwire is set as the replica of the original primary machine and once the replication process is completed then the old machine is taken offline and the new upgraded machine starts serving the users.

#### Command Query segmentation

After doing the vertical scaling the next incremental scaling pattern which we can use is the query segregation and the idea behind the user of this scaling technique is that a database always deal with 2 type of operations only and that is read or write.

Now out of these 2 operations the write operations needs to considered as transaction and should hold all the ACID properties whereas companies can tolerate small delay in read operation. So from this fundamental idea the query segregation is done where we use the Primary machine for dealing with write requests whereas the replicas are used for dealing with the read operations.


#### Multi Primary replication

Multi Primary replication scaling pattern comes after the query segregation pattern and in this rather than using just single machine for dealing with the write operations we use multiple machines to handle both read and write operations in circular manner.

In the circular configuration any node could handle the write operation and after completing the write operation the replication process starts and all the other machines get the update.  On the other hand for the read request, it is basically broadcasted to all the nodes and the node which response first is used for serving the users. But one thing to note is that since replication takes some time generally so read operation is performed multiple times.

- Use concept of read and write operation speed




In databases, the read/write speed is typically measured using the following metrics:

1. **Latency**: This measures the time it takes to complete a single read or write operation. It is usually expressed in milliseconds (ms) or microseconds (µs). Lower latency indicates faster read/write operations.
    
2. **Throughput**: This measures the number of read or write operations that can be performed in a given time period. It is usually expressed in operations per second (OPS) or transactions per second (TPS). Higher throughput indicates a greater ability to handle multiple operations concurrently.
    
3. **IOPS (Input/Output Operations Per Second)**: This is a performance measurement used to benchmark the speed of storage devices like SSDs and HDDs, and it is also applicable to databases. It indicates how many input/output operations can be performed per second.
    
4. **Bandwidth**: This measures the amount of data that can be read from or written to the database per second. It is usually expressed in bytes per second (Bps), kilobytes per second (KBps), or megabytes per second (MBps). Higher bandwidth indicates the ability to transfer larger amounts of data in a given time period.
    

These metrics are essential for evaluating and optimizing the performance of databases, ensuring they meet the required speed and efficiency for various applications.