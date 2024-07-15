This page is dedicated towards understanding the concept of CASE statement in SQL and the main resource used for this topic are the blogs posts by W3 School.

##### What is CASE statement and what is the use of this ?

CASE statement is SQL is used to implement the IF/THEN logic for every tuple in SQL. Basically every CASE statement is followed by using atleast 1 pair of WHEN-THEN which is similar to like if this happens then do this, whereas if the expected result is not found then we can specify it using the ELSE (optional). Also one thing to keep in mind is that every CASE WHEN statement ends with END keyword always

Here is a practice problem to get familiar with the syntax : [Problem 1](Write a query that includes a column that is flagged "yes" when a player is from California, and sort the results with those players first.)

```SQL
SELECT *,
CASE
	WHEN age > 18 THEN "Adult"
	ELSE "Child"
END AS ac_condition
FROM table;
```

One important thing to keep in mind is that this alias with the END statement will act like new column for THEN and ELSE results.
##### Using multiple conditions

There is no restriction on how many number of WHEN statements we can put under CASE, we can use as many as require as per our logic

```SQL
SELECT player_name, weight, 
CASE 
	WHEN weight > 250 AND gender = "female" THEN 'over 250' 
	WHEN weight > 200 THEN '201-250' 
	WHEN weight > 175 THEN '176-200' 
	ELSE '175 or under' 
END AS weight_group 
FROM benn.college_football_players
```


##### Using CASE with aggregate functions and inside aggregate functions

```SQL
SELECT product_category,
       SUM(CASE WHEN sales_channel = 'Online' THEN sales_amount ELSE 0 END) AS online_sales,
       SUM(CASE WHEN sales_channel = 'In-Store' THEN sales_amount ELSE 0 END) AS in_store_sales
  FROM sales
 GROUP BY product_category;
```

```SQL
SELECT department,
       COUNT(CASE WHEN status = 'Active' THEN 1 END) AS active_count,
       COUNT(CASE WHEN status = 'Inactive' THEN 1 END) AS inactive_count
  FROM employees
 GROUP BY department;
```


https://mode.com/sql-tutorial/sql-case#sharpen-your-sql-skills