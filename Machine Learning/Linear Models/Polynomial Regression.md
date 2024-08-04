This page is dedicated towards understanding the concept of polynomial regression algorithm in machine learning and the resources used for this algorithm are basically the Hands on machine learning book and other ones are mentioned below

- [Polynomial regression Blogpost](https://serokell.io/blog/polynomial-regression-analysis)

### [When do we use polynomial regression](#)

Polynomial regression is used in those kind of scenarios where the relationship between dependent and independent features is not linear and instead it is curved. Now since the relationship is not linear thus it is obvious that simple linear regression will underfit and will not give us good results, thus one way of dealing with this it create polynomial features upto a certain degree to capture non linearity and then train model on these newly created features.

![[Polynomial shape.png]]

### [Important point to keep in mind (When generating polynomial features)](#)

An important that we must keep in mind is that, for the given degree value let say 2 it will not only square the features but at the same time it will also generate the polynomial combination of features upto given degree. For example if we have features x1 and x2 and polynomial degree is 2, then we will get new features as
- $x_1$
- $x_2$
- $(x_1)^2$
- $(x_2)^2$
- $x_1*x_2$

### [Why polynomial regression is called special case of linear regression or why we use term linear in polynomial linear regression ?](#) 

To understand this properly we must first be aware about what does the term linear means and then only we will be able to answer why we call polynomial regression as special case of linear regression.

Basically linear means linearity in the parameters, not necessarily in the variables/features themselves. So because of that in case of polynomial regression even after the presence of polynomial features like $x^2$ the model will still remain linear in terms of its coefficients $β_0​,β_1,β_2$.

$$y=β_0​+β_1​x+β_2​x^2+ϵ$$


### [How to calculate how many number of features will be created](#)

By using the binomial coefficient formula we can actually calculate the number of features which will be created 

![Polynomial Feature calculation.png](https://github.com/yuvraaj2002/AI-Notes/blob/master/Machine%20Learning/Images/Polynomial%20Feature%20calculation.png)

### [What would happen if degree = 0 ](#)

Incase we will chose the degree to be 0 in that case only 1 feature will be created or exist and that would be the bias term only. So our model will underfit brutally. We can calculate the features by using binomial coefficient formula `0! = 1`

### [Bias Variance tradeoff](#)

- Basically for the very high value of polynomial degree our model rather than capturing the pattern will actually start capturing the noise as well (in short it will start learning the data itself rather than learning from it). In this way our model will suffer from overfitting and that is low bias and high variance ( so to deal with this we need to use smaller degree of value)
- In case we will use a small degree value than what we should use in that case our model will suffer from underfitting and that is the case of high bias and low variance, and in order to deal with this we should try with higher polynomial degree.

### [How to find optimal value of polynomial degree ?](#) 

Through `Hyper parameter optimization`

### [How can we find the coefficient values for polynomial regression](#)

To find the coefficients we can either use the Ordinary least square approach or iterative optimization algorithm such as [[Gradient Descent]]. But we always use Gradient descent because of the high computationally complexity of OLS technique due to its matrix inversion operation.

### [Robustness to scaling, outliers](#)

- When we introduce polynomial terms, the scale of the features change dramatically (e.g., $x^2,x^3$, etc.) and since polynomial regression will also use the [[Gradient Descent]] algorithm to get best set of parameter values so scaling will improve the performance of the algorithm as internally the convergence speed of gradient descent improves.
- Polynomial terms can exaggerate the effect of outliers even more, as high-degree terms (e.g., $x^3, x^4$) will produce extremely large values for outlying data points so the way we can deal with them is to handle outliers first and then use the algorithm.

### [What is the affect of Multicollinearity in polynomial regression](#)

The affect of multicollinearity will be same like the affect on [[Linear Regression]] algorithm, such as unstable coefficients and high standard error.

### [Python Code to implement Polynomial Regression](#)

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import operator

# Generate some data
np.random.seed(0)
x = 2 - 3 * np.random.normal(0, 1, 100)
y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 100)

# Transform the data to include another axis (Make data 2d)
x = x[:, np.newaxis]
y = y[:, np.newaxis]

# Define the polynomial features
poly = PolynomialFeatures(degree=3)
x_poly = poly.fit_transform(x)

# Fit the model
model = LinearRegression()
model.fit(x_poly, y)

# Visualize the results
plt.scatter(x, y, s=10)

# Sort the values of x before line plot
y_pred = model.predict(x_poly)
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x, y_pred), key=sort_axis)
x, y_pred = zip(*sorted_zip)
plt.plot(x, y_pred, color='m')
plt.show()
```