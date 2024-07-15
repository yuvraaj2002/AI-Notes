This page is actually dedicated towards understanding the concept of bias and variance in the context of machine learning and deep learning. The resources used for this topic are the course videos of CampusX. I am giving down the links to the notebook Pdf’s

[Everything related bias and variance](https://drive.google.com/file/d/17YPjz8n3M1upSAWVQSmKvqZ8OXiHUQeX/view)

### Questions related to introduction

- Define what do you mean by bias ?
    
    Bias can simply be defined as the inability of the model to capture the true relationship of the data

- What do you mean by variance ?
    
    Variance can simply be defined as variability in model predictions/performance due to change in the input data.
    
    ![[Pasted image 20240701181158.png]]
    
    On the left we can see the model with high variance because the predictions of the model would change with the change in the input data and it clearly indicates that the model is very sensitive to the data on which it was trained on and it has actually learned the data itself rather than learning the pattern in the data.

- Is there are relation between bias and variance, if so then explain how they are related?
    
    We can say that there is inverse relation between bias and variance which means with the increase in the bias of model its variance would decrease and with the decrease in bias of model its variance would increase.
    
    ### Explanation of why inverse relation
    
    If we will try to reduce the bias of the model if would mean that we are aiming to perfectly capture the true relationship and in order to do so we need to minimize the mistakes as much as possible. Now the mistakes could be minimized we will try to focus on every data point and while doing so the variance of the model would increase.
    
    Because in the process of minimizing the error we will eventually build a model which is very sensitive to the specific data that is used to train and with the change in this data our model predictions would vary a lot.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/3befcc9b-a6b9-475a-aca8-a70d9c5642bb/Untitled.png)
    
    <aside> 💡 So we need to find a sweet spot between bias and variance.
    
    </aside>

- What do you mean by overfitting and how to deal with this
    
    Overfitting is basically a problem where our model perform very well on the training data but do not give us similar performance results on test data. This is actually a sign of low bias and high variance. Now in order to deal with this issue of overfitting we can use [[Regularization]]

- What do you mean by underfitting ?
    
    Underfitting is basically a problem where our model fails to give us good results on the training data itself and it actually a sign of high bias and low variance. In order to deal with this issue of underfitting we 

- What is bias variance decomposition and what is the use of it ? 
	
	Bias variance decomposition is an important concept in machine learning or deep learning and it is actually used to diagnose the errors of a model by breaking down it into 3 terms
	
	- Bias
	- Variance
	- Irreducable error : This is actually the noise or hidden variance which can’t be captured mathematically and thus can't be reduced.
	
  The expected mean squared error (MSE) of a model can be decomposed as follows: $E[(y−f(x))^2]=(Bias2+Variance)+Irreducible Error$  where,

	- y is the true outcome.
	- $f^(x)$ is the predicted outcome.
	- The first term represents the square of the bias.
	- The second term represents the variance.
	- The third term is the irreducible error.
  
  ### Why do we square the bias ?
  
  Squaring the bias measures the magnitude of the error without considering its direction (positive or negative). This ensures that positive and negative deviations do not cancel each other out, providing a clearer picture of the model's average error.



