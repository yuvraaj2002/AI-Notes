This page is actually dedicated towards understanding the concept of bias and variance in the context of machine learning and deep learning. The resources used for this topic are the course videos of CampusX. I am giving down the links to the notebook Pdf’s

[Everything related bias and variance](https://drive.google.com/file/d/17YPjz8n3M1upSAWVQSmKvqZ8OXiHUQeX/view)

##### Explain what is bias and variance ? 

- Bias can simply be defined as the inability of the model to capture the true relationship of the data
- Variance can simply be defined as variability in model predictions/performance due to change in the input data.

##### What is the relationship between bias and variance ? 

Generally the bias have a inverse relation with the variance, which basically means when we try to reduce the bias then the variance increases and when we try to increase the bias then variance decreases and this thing is very intuitive, because if we will try to reduce the bias then it would mean that we want to minimize the mistakes done by the model on the training data, so to make it possible we actually end up creating a very strict regression line or decision boundary which shows us high variability in term of model performance with change in the data.

##### What do you mean by overfitting and how to deal with it ? 

Overfitting is basically a problem where our model perform very well on the training data but do not give us similar performance results on test data. This is actually a sign of low bias and high variance. Now in order to deal with this issue of overfitting we can use [[Regularization]]

##### What do you mean by underfitting and how to deal with it ? 

 Underfitting is basically a problem where our model fails to give us good results on the training data itself and it actually a sign of high bias and low variance. In order to deal with this issue of underfitting we need to either increase the data or increase the model complexity

##### Explain what is bias - variance decomposition ? 

Bias variance decomposition is an important concept in machine learning or deep learning and it is actually used to diagnose the errors of a model by breaking down it into 3 terms

- Bias
- Variance
- Irreducable error : This is actually the noise or hidden variance which can’t be captured mathematically and thus can't be reduced.

 The expected mean squared error (MSE) of a model can be decomposed as follows: $E[(y−f(x))^2]=(Bias^2+Variance)+Irreducible Error$  where,

- y is the true outcome.
- $f^(x)$ is the predicted outcome.
- The first term represents the square of the bias.
- The second term represents the variance.
- The third term is the irreducible error.
  
  Squaring the bias measures the magnitude of the error without considering its direction (positive or negative). This ensures that positive and negative deviations do not cancel each other out, providing a clearer picture of the model's average error.
