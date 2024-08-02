This page is dedicated towards understanding the concept of Views in SQL and the resources used for this topic will be linked below.

### [What do you mean by Views in SQL and what is the use of views ? ](#)

View can simply be defined as a virtual table which helps us to present the data from one or more than one table in simplified and abstract manner. There are 2 reasons behind using views and these are ⬇️ 

1. To restrict the access of the user to certain data only. For example : If we want to the user to only see 3 columns of the table then we can create a specific view for it.
2. To enhance code reusability : With the help of views we can actually encapsulate complex SQL query which we can execute again and again.

### [How do views differ from tables in SQL?](#)

| Table                                                     | Views                                                                                        |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| The data is physically stored                             | View only stores the query and then execute it to retrieve the data.                         |
| Tables allow updation, insertion and deletion of the data | View do not allow updation, insertion and deletion of data unless view is in updatable mode. |
| Indexes are directly applied on to the table              | Indexes are not directly applied but indexed views (materialized views) can be created.      |

### [What are the different types of views in SQL](#)

There are 4 different types of views in SQL and these views are 

1. `Simple View` : The view which is created from single table without the usage of any GROUP BY clause
2. `Complex View` : The view which is created using complex SQL queries, involving joins and GROUP By.
3. `Inline View` : It is the temporary table created from a subquery and it is used in the `FROM` clause of the Parent query.
4. `Materialized View` : It is used to store the snapshot of the results of the query physically and by doing so the performance is improved by avoiding the re-execution of complex SQL query. The materialized view can be updated periodically.

Before understanding different types of SQL views let us first create a table and insert the values into that table so for that, here we have the SQL commands.

```sql
CREATE DATABASE Views;
USE Views;

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    hire_date DATE,
    salary DECIMAL(10, 2),
    department VARCHAR(50) 
);

INSERT INTO employees (employee_id, first_name, last_name, email, hire_date, salary, department)
VALUES
(1, 'John', 'Doe', 'john.doe@example.com', '2022-01-15', 60000.00, 'HR'),
(2, 'Jane', 'Smith', 'jane.smith@example.com', '2023-02-20', 65000.00, 'HR'),
(3, 'Emily', 'Johnson', 'emily.johnson@example.com', '2021-03-10', 70000.00, 'HR'),
(4, 'Michael', 'Brown', 'michael.brown@example.com', '2024-04-25', 72000.00, 'Finance'),
(5, 'Sarah', 'Williams', 'sarah.williams@example.com', '2023-05-30', 68000.00, 'Finance'),
(6, 'David', 'Jones', 'david.jones@example.com', '2022-07-22', 62000.00, 'Finance'),
(7, 'Laura', 'Miller', 'laura.miller@example.com', '2021-08-14', 71000.00, 'IT'),
(8, 'Robert', 'Davis', 'robert.davis@example.com', '2024-06-12', 75000.00, 'IT'),
(9, 'Nancy', 'Wilson', 'nancy.wilson@example.com', '2023-09-01', 67000.00, 'IT'),
(10, 'James', 'Taylor', 'james.taylor@example.com', '2022-11-19', 69000.00, 'Marketing');
```

##### [Simple View](#)

```sql
CREATE VIEW SIMPLE_VIEW AS 
SELECT first_name,last_name,hire_date
FROM employees;

SELECT * FROM SIMPLE_VIEW;
```

##### [Complex View](#)

```sql
CREATE VIEW COMPLEX_VIEW AS 
SELECT department,SUM(salary) AS "Salary_Per_Dept"
FROM employees
GROUP BY department;

SELECT * FROM COMPLEX_VIEW;
```

##### [Inline View](#)

```sql
SELECT department, AVG(salary) AS average_salary
FROM (
    SELECT department, salary
    FROM employees
    WHERE hire_date > '2023-01-01'
) AS filtered_employees
GROUP BY department;
```

##### [Materialized View](#)

```sql
CREATE MATERIALIZED VIEW department_salary_summary AS
SELECT department, SUM(salary) AS total_salary, AVG(salary) AS average_salary
FROM employees
GROUP BY department;

REFRESH MATERIALIZED VIEW department_salary_summary;
```

### [What are materialized views, and how do they differ from regular views?](#)

| Views                                                                     | Materialized Views                                                                                |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Views are used to display the data of 1 or more tables in abstract manner | Materialized views are used to store the snapshot of query results                                |
| View do not store the data physically and thus are called virtual tables  | Materialized views store the query results physically                                             |
| Views are slower because they re-execute the SQL query                    | Materialized views are relatively faster because they simply need to retrieve the stored results. |

### [Can you update or delete data through a view? Explain your answer.](#)

Whether we can update or delete the data through the view is completely based on the type of the view and the underlying query. There are 2 types of views based on whether we can update or delete the data

1. Updatable view : This type of view allows both the updation or deletion of the data
2. Non updatable view : This type of view do not allow the updation or deletion of the data.

For the view to be updatable there are few conditions which must be satisfied and these are ⬇️

1. There must be single base table
2. No aggregation and GROUP BY must be applied
3. The view should not include columns that are calculated or derived from expressions.

`Note` : If any of the above mentioned conditions is not met then we will simply call that view to ne non updatable.

### [How do you create and drop a view in SQL](#)

```SQL
-- Creating the view
CREATE VIEW COMPLEX_VIEW AS 
SELECT department,SUM(salary) AS "Salary_Per_Dept"
FROM employees
GROUP BY department;

SELECT * FROM COMPLEX_VIEW;

-- Deleting the view
DROP VIEW COMPLEX_VIEW;
```