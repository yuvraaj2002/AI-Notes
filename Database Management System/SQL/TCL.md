This page is dedicated towards understanding the concept of transaction control language in SQL and the resources that we will be using will be linked below.

### [What is TCL in SQL and what are the various commands](#)

TCL stands for Transaction control language and it is one of the type of SQL language which is used to deal with transactions in database and helps to maintain the integrity of the data. There are 3 TCL commands

1. `SAVEPOINT` : This command is used to temporarily save the database state to which we can rollback in case of any error during execution of transaction.
2. `ROLLBACK` : This command is used to revert back to specific or previous savepoint in case of any error during the execution of transaction.
3. `COMMIT` : This command is used when the transaction is completed and we want to permanently save the changes in the database.

### [Can we rollback after using `COMMIT` ](#)

Once we COMMIT the transaction, the changes made during the transactions are saved permanently and cannot be revert back to some savepoint using the rollback.

### [What is the difference between ROLLBACK and ROLLBACK TO in SQL](#)

- ROLLBACK : This command is used to revert back to the database state before transaction began
- ROLLBACK TO : This command is used to revert back to specific SAVEPOINT in the database.

### [Problem Scenario: Order Processing System](#)

You are managing an order processing system where you need to handle multiple related updates in a single transaction. Here's a step-by-step example:

1. **Order Processing:**
    - A customer places an order, which includes updating the inventory, recording the order details, and charging the customer's account.
    - You need to ensure that if any step fails, the entire transaction is rolled back to maintain data consistency.
2. **Steps Involved:**
    - **Insert Order Details:** Record the order in the `orders` table.
    - **Update Inventory:** Decrease the stock in the `inventory` table.
    - **Charge Customer:** Update the `accounts` table to reflect the charge.

`Solution` : To solve this problem we will be using very practical approach by first figuring out the database schema or ER model. After that we will proceed to execute the transaction.


### [How can you manage transaction isolation levels using TCL commands?](#)

### [What is the `SET TRANSACTION` command and how does it relate to TCL commands?](#)

### [How many number of save points can we create](#)

Modern DBMSs like PostgreSQL, Oracle, and MySQL support multiple savepoints, but the exact number may be limited by internal constraints or configuration settings.
