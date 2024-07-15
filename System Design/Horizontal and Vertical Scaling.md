This page is actually dedicated towards understanding the concept of horizontal and vertical scaling and the resources used for this topic are mentioned below

- [Scaling techniques blog](https://blog.algomaster.io/p/system-design-vertical-vs-horizontal-scaling)


#### When do we even need to consider doing scaling ? 

Basically when we have a small user base in that case our current system can handle the read and write request efficiently and provide reasonable low latency and throughput but as the user base will increase it is obvious that the number of request will increase and corresponding to that the data in the database will also increase so because of this the latency and throughput of the queries will be affected and to tackle with this we need to do scaling.

For doing the scaling we have 2 different options and these are horizontal scaling (scaling out) and vertical scaling (scaling up).

#### What is vertical scaling and drawback of it? 

In case of vertical scaling we simply boost the power of existing system by increasing the resources like RAM and disk space. But there are 2 major drawbacks of using vertical scaling

1. Vertical scaling have a hard limit because we cannot have infinite amount of RAM or disk space
2. Incase of any kind of fault, if this new powerful machine will go down then everything will go off.

![[Pasted image 20240709193136.png|550]]

But if we have these 2 drawbacks then still at the early stage vertical scaling is preferred because it is easy as compared to horizontal scaling, as here we don't need to make a lot of architectural changes.

#### What is horizontal scaling and drawback of it? 

Horizontal scaling is also called scaling out and in this type of scaling rather than boosting the existing machine with upgraded resources, instead we introduce multiple database servers / nodes to handle the load and reduce the latency. This type of scaling must be used when there is rapid growth and high availability needs

![[Pasted image 20240709194155.png|450]]

Now since multiple nodes gets introduced so to distribute the queries or request properly among nodes a load balancer is used. The 2 major advantages of doing this horizontal scaling are : 

1. Scalability
2. Fault tolerance capability

Distributing the application across multiple servers introduces complexity in terms of data consistency, load balancing, and inter-server communication.