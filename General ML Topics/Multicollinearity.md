This notion page is dedicated towards understanding the concept of multicollinearity in machine learning and the main resource used for this topic is basically the course video of CampusX.
[Notebook](https://drive.google.com/file/d/131sJUu335FSldQmdP4qTbp4qdSG4jYN8/view) Pdf of this topic.


##### What do you mean by Multicollinearity and what is harm of this ? 

Multicollinearity is basically a problem where the independent features are highly correlated with each other and due to this high correlation, even though our prediction do not gets affected but the inference gets affected a lot due to unreliable coefficients. Not only this due to multicollinearity the data analysis also gets hampered.

Example: CGPA and IQ are features which might have high correlation between them.

##### What do you mean by perfect multicollinearity, what happens due to it and why does it happen at all ? 

Perfect multicollinearity is basically a problem where one independent feature is the linear function of some other independent feature. Example Marks in Percentage will be linear function of CGPA, where Marks (%) = CGPA * 10.

Sometimes the perfect multicollinearity could be due to the problem statement/randomly or it could be due to not being conscious while doing data processing. For example if we have a feature about gender having values male and female and we did one hot encoding without removing the one column then it will lead to perfect multicollinearity.

Due to perfect multicollinearity we are unable to find the regression coefficients in multiple linear regression setup using ordinary least square method and the reason is that in case of MLR with OLS technique we need to find the inverse of the matrix and to calculate the inverse we need to further calculate 2 things
1. Adjoint
2. Determinant

Now due to perfect multicollinearity the determinant of the matrix becomes 0 (singular matrix) and due to this the Inverse can be calculated as 1/0 is not a valid operation.

##### What do you mean by standard error and why it tends to increase due to multicollinearity ? 

Standard error can simply be defined as the standard deviation of the sampling distribution of some measure. Now since the perfect multicollinearity is not always found so it is not that we will not be able to find the coefficients due to 0 determinant, but still we will get small determinant value.

1/ smaller value = Larger value and when this larger value is multiplied with the adjoint of the matrix then the coefficients values gets larger and due to this the overall standard error also increases due to high coefficients in general.

##### What is the issue in case the standard error increase ? 

##### What are the ways using which we can detect multicollinearity ? 

There are basically 3 ways using which we can actually detect multicollinearity in machine learning and these are

1. High Correlation
2. Small determinant
3. Variance inflation factor or Tolerance


##### Explain variance inflation factor and also tell how the tolerance is related with the VIF

Variance Inflation Factor (VIF) is a measure used in regression analysis to quantify how much the variance of a regression coefficient is inflated due to multicollinearity among the independent variables. Mathematically it is given as 

$$VIF = 1 / 1 - R_{i}^2$$
where Ri is actually coefficient of determinant which we get after regressing one independent feature on all other variables. So if we have 4 independent features then we will be having 4 VIF's and we will be analyzing all the VIFs.

- If VIF ranges between 1 to 5 then it is moderate collinearity
- If VIF exceeds more than 5 then it represents high multicollinearity
##### How to remove multicollinearity ? 

There are couple of ways using which we can actually deal with multicollinearity

1. Adding more data
2. Removing highly correlated feature or combining highly correlated features into 1 feature
3. By using PLS which stands for Partial least squares and it is a technique where we first perform PCA and then use linear regression

