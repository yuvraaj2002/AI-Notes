This page is dedicated towards understanding the concept of Window function in SQL and the main resources used for this topic are the videos of CampusX and blogs, other than this Window function demands the practice so we will also be taking look at the practice questions

- [Window function practice questions](https://www.machinelearningplus.com/sql/sql-window-functions-exercises/)


##### What do you mean by window functions, their need and name them

Window functions are also called analytical function because they are actually use to perform analytical operation such as ranking, cumulative sum, moving average on the set of rows which are defined within the window. In order to define the boundary of the window we use the OVER clause. The commonly used window functions are

1. Rank
2. Dense rank
3. Row number
4. First value
5. Last value
6. Nth value
7. Lead
8. Lag
9. Sum, Min, Max, Avg

##### Explain the difference between Rank and Dense rank window function ? 

- Rank window function do not give consecutive ranking, which basically means that if there exist multiple rows with same rank then the next rank will be (Current rank + Repetitive rows)
- Dense rank window function gives consecutive rank, which means even if there exist multiple rows with the same rank, the next rank will be current rank+1

![[Pasted image 20240714181526.png|400]]

##### What is the role of row_number window function ?

Row number is used to provide a unique sequential integer to every row within in the window and it can be used for sort of temporary primary key.
##### What do you mean by frames and what are the various frames ? 

Frames in SQL are used to define the subset of rows withing the window or we can say that it is like window inside a window. Using frames we get a lot of flexibility and Some of the most common frames are 

- ROWS BETWEEN UNBOUNDED PRECENDING AND UNBOUNDED FOLLOWING 
- ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
- ROWS BETWEEN 2 PRECEDING AND 1 FOLLOWING



##### What is the difference between Lead and Lag window function ? 

- LAG : By using this we get access to previous row relative to the current row within a window
- LEAD : By using this we get access to the next row relative to the current row withing window

##### What is the concept of Moving average ?

Moving average is a statistical concept which is used to smoothen the fluctuations in the data and provide understanding of underlying trend. Basically in this rather than finding the average of static data we calculate the average of moving data, where new data points gets added and old data points gets removed.

Concept of moving average is used a lot in the time series data