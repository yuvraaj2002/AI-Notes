This page is dedicated towards understanding the concept of ANOVA test in machine learning and statistics and the resources used for this topics will be mentioned below.

- [ANOVA test](https://drive.google.com/file/d/1gQAeNqaL2sBFSpAtONhtn9oBzWFh7c6h/view)

##### Define F distribution ? 

F distribution is a continuous probability distribution which that arises from the ratio of 2 independent values following chi square distribution divided by their corresponding degree of freedom. This distribution is commonly used in the analysis of variance (ANOVA).

![[F distribution.png]]

##### What do you mean by ANOVA and what are its types ? 

ANOVA stands for Analysis of Variance and it is a hypothesis test which have 2 different variants both serving their own different purpose.

1. One way ANOVA : It is a type of hypothesis test which is used to analyze the difference in mean of 2 or more groups of single categorical variable by using the continuous dependent variable.
2. Two way ANOVA : It is a more complex test which is used to understand the interaction between 2 independent variables and their affect on continuous dependent variable. 2 Independent variables could be either continuous or categorical.

##### What are the various things that we need to find for the F statistic value

- `Within group sum of squares` : Sum of squares of difference between the values of the group and group’s mean
- `degree of freedom corresponding to SSW_group` : n - k, where n are total number of data points and the k is the number of categories
- `Between group sum of squares` : Sum of squares of difference between group means and the grand mean of overall dataset
- `degree of freedom corresponding to SSB_group` : We can think this like if we have the SSB value then how many values do we need to calculate the remaining value and in this case it would be K-1

![[F statistic value.png]]

##### Explain how does One way ANOVA works with some example

Let us simply assume that some school called us as a researcher to determine that whether there is 3 newly teaching techniques are different or leading to some difference or not. Now in this case we will be using the One way ANOVA test as we will be determining that whether the average marks (means) of 3 teaching techniques are statistically different from each other or not.

1. Setting up null and alternative hypothesis : Null (There is no difference in the means of 3 groups) and alternative (This is some difference in the means of 3 groups)
2. Calculate the F statistic : By using Sum of squares within group, between group and corresponding degree of freedoms.
3. By using the F distribution for given degree of freedom and test statistic value we will find the corresponding p value and compare it with the LOS
4. if p value < LOS then reject null hypothesis

##### Explain how do we use ANOVA for feature selection ? 

In ANOVA we have 2 variants so we specifically use One way ANOVA as feature selection technique where we want to determine if there exist a difference among the means of 2 or more groups of single categorical variable by using continuous dependent variable. No if this exist for a variable then it means that feature is actually useful so we keep it otherwise we remove it.



