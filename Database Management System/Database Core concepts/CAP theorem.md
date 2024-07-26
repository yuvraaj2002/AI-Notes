This page is dedicated towards understanding the concept of CAP theorem in distributed designs or database and the main resource used for this topic are mentioned below

- [Lecture Notes](https://drive.google.com/drive/folders/1i80S1YymUX8pWId6tAnh10rS2FeO-Mbb)
- [Youtube Lecture Love Babbar](https://www.youtube.com/watch?v=EIl02n-FxTg)
- [CAP theorem blog post](https://blog.algomaster.io/p/15f1d791-86ce-40ed-8269-962dbddbefdb)

#### When do we consider talking about CAP theorem ? 

Before actually going over what is CAP theorem we must first be aware about what is the foundational topic behind CAP theorem. So CAP theorem is actually related to distributed system where there are multiple machines are connected with each other to achieve a common goal.

In the context of database we will be talking about distributed database system where multiple database servers will be connected with each other to serve the user queries efficiently.

#### What is CAP theorem ? 

CAP theorem states that a distributed system out of 3 conditions (consistency, availability and partition tolerance) only 2 conditions will be held true simultaneously. Also according to CAP theorem there will always be a tradeoff between the consistency and availability in case of partition.

But what does partition means ?  So partition refers to a situation where our network gets broken down into 2 or more groups which cannot communicate with each other and this breakdown occurred due to some issue.

#### Types of Distributed systems based on CAP theorem

⚠️ Since only 2 conditions can be held true simultaneously so based on this there are 3 different categories of distributed systems.

- CA systems : These are those type of systems which ensure both consistency and availability across all the nodes of distributed system but cannot handle partitions so if partition will take place which are bound to happen in distributed  system then there will always exist a tradeoff between consistency and availability.

- CP systems : These are those systems which ensure both consistency and partition tolerance but at the cost of availability. Basically in case of partition all the inconsistent nodes are turned off until partition is not fixed and by the time only the read operations are allowed and not the write operation. Example: Banking applications, because in such applications consistency is way more important than availability.

- AP systems : There are those database which ensure both availability and partition tolerance but at the cost of consistency so incase of partition, the user will not get the latest data but once the partition will be fixed, replication will take place and the new updated information could be served. Example: Social media sites need to be available