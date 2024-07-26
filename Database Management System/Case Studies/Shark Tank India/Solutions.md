This page is actually dedicated towards the solutions of all the questions which are mentioned in the PDF and in this page I will be sharing my approach in term of SQL query and also I will be explaining my thought process.

### You Team must promote shark Tank India season 4, The senior come up with the idea to show highest funding domain wise so that new startups can be attracted, and you were assigned the task to show the same.

To solve this problem there are 2 approaches which are coming in my mind, so let's me explain you both the approaches sequentially.

##### Approach 1 (Using Window function)

1. Define a window over Industry that means PARTITION BY Industry
2. For every window arrange the tuples in descending order of the Total Deal amount 
3. For the defined window use the ROW_NUMBER() window function because DENSE_RANK() will assign same rank to 2 tuples having same value and our data have such tuples as well.
4. After executing above steps we will only be focusing on the Industry, Total Deal amount, Row number and return all these in form of subquery.
5. By using the outer query we will filter out only those tuples where the Row number is 1

```sql
SELECT T.Industry,T.Highest_Funding FROM (
SELECT Industry,`Total_Deal_Amount(in_lakhs)` AS "Highest_Funding",
ROW_NUMBER() OVER(PARTITION BY Industry ORDER BY `Total_Deal_Amount(in_lakhs)` DESC) AS "RNum"
FROM st) as T
WHERE T.RNum = 1;
```

##### Approach 2 (Using GROUP BY)

1. Perform group by on basis of Industry
2. Select the industry and by using aggregate function select the maximum Total deal amount for every group

```sql
SELECT Industry,MAX(`Total_Deal_Amount(in_lakhs)`) AS "Highest_Funding"
FROM st
GROUP BY Industry;
```

### You have been assigned the role of finding the domain where female as pitchers have female to male pitcher ratio >70%



### You are working at marketing firm of Shark Tank India, you have got the task to determine volume of per season sale pitch made, pitches who received offer and pitches that were converted. Also show the percentage of pitches




### As a venture capital firm specializing in investing in startups featured on a renowned entrepreneurship TV show, you are determining the season with the highest average monthly sales and identify the top 5 industries with the highest average monthly sales during that season to optimize investment decisions?



### As a data scientist at our firm, your role involves solving real-world challenges like identifying industries with consistent increases in funds raised over multiple seasons. This requires focusing on industries where data is available across all three seasons. Once these industries are pinpointed, your task is to delve into the specifics, analyzing the number of pitches made, offers received, and offers converted per season within each industry.



### Every shark wants to know in how much year their investment will be returned, so you must create a system for them, where shark will enter the name of the startup’s and the based on the total deal and equity given in how many years their principal amount will be returned and make their investment decisions



### In the world of startup investing, we're curious to know which big-name investor, often referred to as "sharks," tends to put the most money into each deal on average. This comparison helps us see who's the most generous with their investments and how they measure up against their fellow investors.



### Develop a stored procedure that accepts inputs for the season number and the name of a shark. The procedure will then provide detailed insights into the total investment made by that specific shark across different industries during the specified season. Additionally, it will calculate the percentage of their investment in each sector relative to the total investment in that year, giving a comprehensive understanding of the shark's investment distribution and impact



### In the realm of venture capital, we're exploring which shark possesses the most diversified investment portfolio across various industries. By examining their investment patterns and preferences, we aim to uncover any discernible trends or strategies that may shed light on their decision-making processes and investment philosophies



### Explain the concept of indexes in MySQL. How do indexes improve query performance, and what factors should be considered when deciding which columns to index in a database table

