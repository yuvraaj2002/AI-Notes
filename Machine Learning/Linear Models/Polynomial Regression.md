This page is dedicated towards understanding the concept of polynomial regression algorithm in machine learning and the resources used for this algorithm are basically the Hands on machine learning book and other ones are mentioned below

- [Polynomial regression Blogpost](https://serokell.io/blog/polynomial-regression-analysis)

### [When do we use polynomial regression](#)

Polynomial regression is used in those kind of scenarios where the relationship between dependent and independent features is not linear and instead it is curved. Now since the relationship is not linear thus it is obvious that simple linear regression will underfit and will not give us good results, thus one way of dealing with this it create polynomial features upto a certain degree and then train a linear model like [[Linear Regression]] on these newly created features.

### [Important point to keep in mind (When generating polynomial features)](#)

Now an important and good thing about polynomial regression is that, for the given degree value let say 2 it will not only square the features values but at the same time it will also generate the polynomial combination of features upto given degree. For example if we have features x1 and x2 and polynomial degree is 2, then we will get new features as $x_1,x_2,(x_1)^2,(x_2)^2,x_1(x_2)^2,(x_1)^2x_2$

### [Why polynomial regression is called special case of linear regression or why we use term linear in polynomial regression ?](#) 

To understand this properly we must first be aware about what does the term linear means and then only we will be able to answer why we call polynomial regression as special case of linear regression.

Basically linear means linearity in the parameters, not necessarily in the variables themselves. So because of that in case of polynomial regression even after the presence of polynomial features like $x^2,x^3$ the model will still remain linear because it is linear in terms of its coefficients.


### [How to calculate how many number of features will be created](#)

By using the binomial coefficient formula we can actually calculate the number of features which will be created 
![[Pasted image 20240711175735.png]]


### [Bias Variance tradeoff](#)

- Basically for the very high value of polynomial degree our model rather than capturing the pattern will actually start capturing the noise as well (in short it will start learning the data itself rather than learning from it). In this way our model will suffer from overfitting and that is low bias and high variance ( so to deal with this we need to use smaller degree of value)
- In case we will use a small degree value than what we should use in that case our model will suffer from underfitting and that is the case of high bias and low variance, and in order to deal with this we should try with higher polynomial degree.

### [How to find optimal value of polynomial degree ?](#) 

- Cross validation
- Hyper parameter optimization


### [Robustness to scaling, outliers](#)

- When we introduce polynomial terms, the scale of the features change dramatically (e.g., $x^2,x^3$, etc.) and since polynomial regression will also use the [[Gradient Descent]] algorithm to get best set of parameter values so scaling will improve the performance of the algorithm as internally the convergence speed of gradient descent improves.
- Polynomial terms can exaggerate the effect of outliers even more, as high-degree terms (e.g., $x^3, x^4$) will produce extremely large values for outlying data points so the way we can deal with them is to handle outliers first and then use the algorithm.