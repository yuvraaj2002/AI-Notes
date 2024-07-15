
Order By is basically a clause in SQL which is used for sorting the data in some specific order and this could be either ascending order or the descending order.

```sql
SELECT * FROM
TABLE WHERE class = 12
ORDER BY id ASC;
```

- **Step 1**: Identify the table (`FROM TABLE`).
- **Step 2**: Apply the filter condition (`WHERE class = 12`).
- **Step 3**: Retrieve the data (`SELECT *`).
- **Step 4**: Sort the results (`ORDER BY id ASC`)

Other than performing the sorting on the single column we can also perform the sorting on multiple columns.

```sql
SELECT * FROM
TABLE WHERE class = 12
ORDER BY id ASC,sections DESC;
```

Another thing to mention is that we can also sort the data by using the column number rather than specifying the name of the column.

```sql
SELECT * FROM
TABLE WHERE class = 12
ORDER BY 1 ASC;
```

One last thing to specify is that we can also sort the values by creating some custom expression such as.

```sql
SELECT *
FROM table_name
ORDER BY ABS(numeric_column) DESC; -- Sorting numerically by absolute values

SELECT *
FROM table_name
ORDER BY CONCAT(column1, ' ', column2) ASC; -- Sorting concatenated varchar columns
```


### Time complexity and Sorting algorithm

O(n log(n) ) is the time complexity for performing sorting 

- [ ] Which sorting algorithm is being used in databases 