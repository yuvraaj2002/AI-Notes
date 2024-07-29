This page is dedicated towards understanding the concepts related to linear regression in machine learning and the resources used for this algorithm are basically the videos of CampusX.

[Linear regression Wikipedia](https://en.wikipedia.org/wiki/Linear_regression#:~:text=In%20linear%20regression%2C%20the%20relationships,models%20are%20called%20linear%20models)


##### What is linear regression and from where does the terms linear and regression comes from ? 

Linear regression is a statistical algorithm which is used to estimate the linear relationship between dependent and independent variable.

- Linear comes form the fact that there exist a linear relationship between dependent and independent feature and we need to estimate this relationship (in term of coefficient values)
- Regression means study the reliability and the strength of the relationship.

Also based on the number of independent variables there are 2 different versions of linear regression algorithm and these are 

- Simple linear regression → When there is only 1 independent feature
- Multiple linear regression → When there are more than 1 independent feature

##### Is linear regression algorithm parametric or not and if so then what are the various parameters associated with this ? 

Linear regression is parametric in nature because it makes an assumption about the data it is dealing with and there are 5 assumptions of linear regression. Also since the number of parameters won't increase with increase in data points so that is also the indication that linear regression algorithm is parametric in nature. There are 2 parameters associated with linear regression and these are slope and intercept

- Slope is used to define the rate of change of dependent variable with unit change in the associated independent variable. For example if slope value for some input feature is $W_1$ → 0.4 , it represents the output value will vary with rate of 0.4.
- Offset is used to **present a base line value** for our algorithm, like it is used in those scenarios where if the input*slope → 0, there must be some value as an output.

##### What is best fit line and what are ways to find it ? 

Best fit line is the mathematical function for which the value of cost function will be minimum. There are 2 techniques which we can use to find the best fit line and these are ⬇️

1. **Ordinary least square method** → Closed form expression, where we simply use a mathematical function to get the values of model coefficients, but incase of multiple regression setup this approach is not preferred due to high computational complexity of Matrix inversion operation $O(n^3)$
2. [[Gradient Descent]] → It is a Non closed form expression where we use iterative optimization algo.

The point to be noted is that in 3d we call it as best fit plane and in further higher dimension we call it as hyper plane and in order to find this mathematical function which is made up of slopes and intercept we need to minimize the objective function/ cost function.

##### Affect on performance algorithms based on (Scaling, Outliers, Missing values)

- Scaling: Since the convergence speed of gradient descent algorithms improves significantly with the scaled data so scaling improve the performance of the algorithm.
- Outliers: Linear regression algorithm is very sensitive to outliers and lead to overfitting and to deal with this we use [[Regularization]] and the variants of linear regression such as [[Lasso Regression]], [[Ridge Regression]] and [[Elastic Net Regression]]
- Linear regression can't work with missing values so we need to handle them either using univariate imputation techniques or using multivariate imputation techniques such as [[Missing Values]]

##### Talk about the bias variance tradeoff and how to deal with it ?

- Linear regression algorithm is sensitive to outliers and tries to capture them if not regularization is being done, and due to this suffer from overfitting and that is low bias and high variance, so deal with this we need to use regularization by adding penalty terms
- In case we are not using useful or sufficient number of features or attributes then our model will suffer from the issue of underfitting and that is high bias and low variance, so deal with this we need to focus on feature engineering or gather more data.
##### What are the assumptions of linear regression ? 



