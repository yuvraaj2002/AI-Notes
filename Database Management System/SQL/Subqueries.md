This page is dedicated towards understanding the concept of Subqueries in SQL and the main resource used for this topic are the course videos of CampusX and also not only this, the questions that we are going to use for practice are from this link [W3 School](https://www.w3resource.com/sql-exercises/subqueries/index.php)


##### What do you mean by subquery and why they are used ? 

##### What are the types of Subqueries in term of data they return?

##### What are the types of Subqueries in term of working?



```SQL
CREATE DATABASE subquery;
USE subquery;

-- Create the table
CREATE TABLE salesman (
    salesman_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50),
    commission DECIMAL(3, 2)
);

-- Insert data into the table
INSERT INTO salesman (salesman_id, name, city, commission) VALUES
(5001, 'James Hoog', 'New York', 0.15),
(5002, 'Nail Knite', 'Paris', 0.13),
(5005, 'Pit Alex', 'London', 0.11),
(5006, 'Mc Lyon', 'Paris', 0.14),
(5003, 'Lauson Hen', 'San Jose', 0.12),
(5007, 'Paul Adam', 'Rome', 0.13);

-- Create the orders table
CREATE TABLE orders (
    ord_no INT PRIMARY KEY,
    purch_amt DECIMAL(10, 2),
    ord_date DATE,
    customer_id INT,
    salesman_id INT
);

-- Insert data into the orders table
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
(70001, 150.50, '2012-10-05', 3005, 5002),
(70009, 270.65, '2012-09-10', 3001, 5005),
(70002, 65.26, '2012-10-05', 3002, 5001),
(70004, 110.50, '2012-08-17', 3009, 5003),
(70007, 948.50, '2012-09-10', 3005, 5002),
(70005, 2400.60, '2012-07-27', 3007, 5001),
(70008, 5760.00, '2012-09-10', 3002, 5001),
(70010, 1983.43, '2012-10-10', 3004, 5006),
(70003, 2480.40, '2012-10-10', 3009, 5003),
(70012, 250.45, '2012-06-27', 3008, 5002),
(70011, 75.29, '2012-08-17', 3003, 5007),
(70013, 3045.60, '2012-04-25', 3002, 5001);


-- Create the customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    cust_name VARCHAR(50),
    city VARCHAR(50),
    grade INT,
    salesman_id INT
);

-- Insert data into the customers table
INSERT INTO customers (customer_id, cust_name, city, grade, salesman_id) VALUES
(3002, 'Nick Rimando', 'New York', 100, 5001),
(3005, 'Graham Zusi', 'California', 200, 5002),
(3001, 'Brad Guzan', 'London', 100, 5005),
(3004, 'Fabian Johns', 'Paris', 300, 5006),
(3007, 'Brad Davis', 'New York', 200, 5001),
(3009, 'Geoff Camero', 'Berlin', 100, 5003),
(3008, 'Julian Green', 'London', 300, 5002),
(3003, 'Jozy Altidor', 'Moscow', 200, 5007);

```



- What do you mean by subquery
    
    Subquery can simply be defined as the query inside the query
    
- What are the different types of subquery based on the return data
    
    On the basis of the return data there are actually 3 different categorization of subqueries and these are ⬇️
    
    1. Scaler subquery → In this the inner query will only return single value
    2. Row subquery → In this the inner query will return single row but multiple column
    3. Column subquery → In this the inner query will return multiple rows but single column
    4. Table subquery → In this the inner query will return multiple rows and multiple columns
- What are the different types of subquery based on the working ?
    
    Based on the working there are 2 different types of subqueries and these are ⬇️
    
    1. Independent query → In this both inner query and outer query operates independently
    2. Correlated query → In this the inner query actually depends on the outer query for working and inner query can’t be executed independently


IN operator wala rona

- 11
- 14 Good important
- 15 start