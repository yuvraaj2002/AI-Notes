This page is dedicated towards understanding the concept of transactions in Databases and the resources used for understanding this concept are mentioned below

- [Notes of the class](https://drive.google.com/drive/folders/1fidrKEB7OBccOhfr5jy_mGeNlIK8HE2O)
- [Youtube Video](https://www.youtube.com/watch?v=sS4gadQw5iM)


#### What do you mean by transaction 

Transaction can simply be defined as the unit of work having logical sequence of steps. Example: Transferring the money form one account to some other account is basically a transaction where there are couple of steps which needs to be executed in logical sequence

-  Reading the amount from the first account.
- Deducting the amount from the first account.
- Adding the amount to the second account.
- Updating the transaction records.  


#### What do you mean by commit, rollback and savepoint



#### What do you mean by ACID properties and what is the need of them ? 

In order to maintain the integrity of the database during transactions, there are around 4 properties which must be held true and these are 

- Atomicity : Every transaction must be considered as an unit of work which must be either completed completely and should not occur at all and in case some error occur during the execution of some step in the transaction then the data base must be rolled back to the previous state to ensure the data is consistent.
- Consistency : It means that the data in the database must be consistent before and after the completion of the transaction. In practical terms it should not be like that the amount is deducted from one account but it is not credited in the target account.
- Isolation : Isolations means that if there exist multiple concurrent transactions then they must be isolated from each other and should be executed sequentially so that no data anomalies occur.
- Durability: According to durability if the changes have been committed in the database then that change in the state of the database must be permanent.


#### Transaction states

There are various transaction states under which the transaction goes through and these transaction states are 

- Active state : The very first state of the life cycle of the transaction, all the read and write operations are being performed. If they execute without any error the T comes to Partially committed state. Although if any error occurs then it leads to a Failed state.
- Partially committed state : After transaction is executed the changes are saved in the buffer in the main memory. If the changes made are permanent on the DB then the state will transfer to the committed state and if there is any failure, the it will go to Failed state.
- committed state : When updates are made permanent on the DB. Then the T is said to be in the committed state. Rollback can’t be done from the committed states. New consistent state is achieved at this stage.
- failed state : When T is being executed and some failure occurs. Due to this it is impossible to continue the execution of the T.
- aborted state : When T reaches the failed state, all the changes made in the buffer are reversed. After that the T rollback completely. T reaches abort state after rollback. DB’s state prior to the T is achieved.
- terminated state : A transaction is said to have terminated if has either committed or aborted.

![[Pasted image 20240709185517.png]]
#### How to implement atomicity in transactions


#### What is schedule in DBMS and its types ? 

Schedule can simply be defined as sequence of operations like (read, commit, write) coming from multiple transactions and the ordering of these operations can significantly impact the data integrity of the overall database. There are basically 2 broad types of schedules 

1. Serial schedules : In case of serial schedules all the operations of the transactions are executed entirely and then the next transaction is considered.
2. Non serial schedules : In case of non serial schedule the operations from multiple transactions are executed in interleaving fashion.

![[Pasted image 20240710180517.png]]

#### What is serializability and what is the need ? 

Before moving on to what is serializability we must first be aware about what is the need of this, Now since the non serial schedules execute the operations from multiple transactions in interleaved fashion so there are chances of loss of integrity of data stored in database, so in order to test that whether the non serial schedule is safe or not we check if it is serializable or not.

A non serial schedule is said to be ***Serializable*** if it leads to a database state same as that of the database state if we would have executed schedule in serial fashion. So in order to check if a non serial schedule can be serializable or not we can use 2 different ways 

1. Conflict serializable
2. View serializable


#### What are conflict operations and in general how to detect if there is conflict ? 

Conflict operations are those type of operations which leads to loss of integrity of the data stored in the database and there are 3 different types of conflict operations.

- **Read-Write Conflict**: Transaction T1 reads a data item X that Transaction T2 subsequently writes to before T1 completes.
- **Write-Read Conflict**: Transaction T1 writes to a data item Y that Transaction T2 subsequently reads from before T1 completes.
- **Write-Write Conflict**: Transaction T1 writes to a data item Z that Transaction T2 also writes to.

Now the way we can actually detect if there is some conflict in the schedule or not is by building a precedence graph of all the transactions, where
- Nodes will represent the transactions 
- Edges will represent the conflicting operations 

Finally after building the precedence graph then using directed graph Cycle detection algorithm we can detect whether there exist a conflict or not. 