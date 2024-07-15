Deadlock is basically a general topic operating systems and distributed systems but it is also related to [[Transactions - ACID]] in DBMS.

#### What is deadlock ? 

Deadlock is an important concept which is discussed when we are talking about the multi-processor system or distributed systems, but in context of DBMS deadlock is an important concept to be discussed when we are talking about concurrent transactions.

Deadlock in context of DBMS occurs when 2 or more transaction execution gets freezed because each one of them are waiting for some resource which is already being hold by some other transaction. Consider two transactions T1 and T2:

- **T1**: Locks resource A, then requests resource B.
- **T2**: Locks resource B, then requests resource A.

If T1 has locked A and is waiting for B, and T2 has locked B and is waiting for A, they will each wait indefinitely for the other to release the resource they need.

#### What are the conditions which lead to deadlock ? 

There are basically 4 different conditions which lead to deadlock and if and only if all 4 conditions will be true simultaneously then only the deadlock will happen otherwise deadlock will not happen in the system.

1. Mutual exclusion : It means that if some transaction holds a resource, others are prevented from accessing it until the transaction releases the resource then it can lead to deadlock.
2. Hold and Wait : If a transaction is already holding at least one resource and is still waiting to acquire additional resources that are currently held by other transactions.
3. No Preemption: If the resource cannot be preempted (forcefully taken) by some transaction then it can lead to deadlock.
4. Circular dependency: If there exist a circular chain of resource dependency among the transactions then it can lead to deadlock.

Now since we are already aware about all the conditions which lead to deadlock so now let us talk about what are the various ways using which we can actually deal with the deadlock and there are basically 4 different ways for dealing with them.

##### Deadlock Prevention

In case of deadlock prevention the core idea is to simply make sure that out of 4 conditions atleast one of the condition is not true and by doing so we simply prevent the deadlock in the system.
##### Deadlock Ignorance

Deadlock ignore is one of the most simplest but also the most ineffective way of dealing with deadlocks, because in this approach rather than preventing or recovering the system from the deadlock state we simply ignore it and rollback the system to the previous state and start the execution again. This is also called ostrich approach.
##### Deadlock Avoidance

In case of deadlock avoidance we use an algorithm called bankers algorithm and Banker's algorithm monitor the current state of the system and predict the impact of granting resource requests on future states.

##### Deadlock Detection and Removal

Deadlock detection and recovery is also a type of deadlock handling mechanism where we don't use any kind of mechanism to prevent or avoid the deadlock instead we move with the assumption that deadlock may happen in the system and we detect them periodically and once the deadlock is detected then move to recover the system from the deadlock.

Now in order to detect the deadlock we use wait for graph which is a type of graph where the nodes represents the transactions and the edges represent the resource dependency of some transaction. Example: If transaction T1 is waiting for some resource that is already occupied by Transaction T2 then an edge exist between T1 and T2.

After building the wait for graph we can use any directed cycle detection algorithm either the depth first approach or we can also use the typical Kahn algorithm ( with queue ).
