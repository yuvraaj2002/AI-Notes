This page is dedicated towards understanding the concept of the client server architecture in the system design and the main resources used for this topic are mentioned below

- [Client Server architecture blog](https://www.redswitches.com/blog/client-server-architecture/)

#### What is client server architecture

Client server architecture is a type of system which have only 2 entities that is client and a server. Basically the client through website or mobile app make a request to the server and the server give the response back.

![[Pasted image 20240710094428.png|400]]


There are basically different types of client server architecture and the detailed explanation of each of the method is given below.

#### Tier 1 architecture

Incase of tier 1 architecture the user interface, business logic and data all lies into 1 single system only and because of this the overall system is less complex. MP3 player is example of this and since the MP3 only player only deals with audio, so this architecture do not use any complex DBMS to manage and store data instead the MP3 directly access the data from the disk with the help of operating system.

#### Tier 2 architecture

In case of tier 2 architecture the user interface and the business logic lies on the client side and the data lies on the server side and in order here since everything is not on the same machine so a separate database management system is used for managing the data.

![[Pasted image 20240710102302.png]]

Tier 2 client server architecture works best in case we have the small scale application but as the the number of users increase it is obvious that the number of request would also increase, so in order to cope up with the increasing load on the database server and also to introduce more security we use 3 tier architecture.

For the first time the client will make request to DNS to resolve the IP  address corresponding to domain like www.swiggy.com. After that the client will make request to the server via that IP address. And the server will respond back and that response will be stored in CDN and also sent back to the client. In future if the user wants to access data like past order then instead of making
request to the server, CDN will provide the data.


#### 3 tier architecture

In case of 3 tier architecture, in between the client side and the server side we introduce another layer called application layer and this layer is responsible for dealing with the the business logic (about how to present the data coming from the server side to the client).

By introducing this layer in between client and the database not only the security is enhanced but also the client side becomes light as now the client side machine have to focus only on presenting the data processed by application layer.

![[Pasted image 20240710103504.png]]