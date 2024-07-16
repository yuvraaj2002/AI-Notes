This page is actually dedicated towards understanding the concept of gradient descent in machine learning and the resources used for this topic will be mentioned below, but the initial resource I used was course video of CampusX.

##### What the meaning of gradient in general ? 

Gradient can simply be defined as the vector pointing in the direction of the maximum increase, or mathematically it is also called as collection of partial derivatives. 

##### What is the difference between positive and negative slope ? 

- Positive slope means with the increase or decrease in value of one variable the value of other variable also increases or decreases accordingly
- Negative slope means with the increase in the value of one variable the value of other variable decreases vice versa

##### What do you mean by gradient descent and explain the working of this algorithm ? 

Gradient descent is an iterative optimization algorithm which helps us to find those values of function parameters which minimize the objective function. In short we take opposite steps in the direction of the gradient. Now the set of steps which are followed are 

1. Start with some random values of function or model parameters
2. Calculate the gradient at that point
3. For the specified learning rate value, we use the weight update formula (New = Old - Lr * Gradient)

Gradient : Partial differentiation of loss function wrt to model parameter


##### What is the difference between convex and non convex problems, also tell when does this algorithm stops ? 

- Convex optimization problems are those problems which have only 1 single global minima 
- Non convex optimization problems are those problems which along with 1 global minima also have multiple local minima and saddle points.

The stopping criterion of the gradient descent could either be hardcoded like in terms of number of epochs or we could also set a threshold of parameter change.


![[Pasted image 20240716045938.png]]
##### What is the affect of learning rate, scaling and loss function on gradient descent ? 

- Learning rate is a hyper-parameter which is used to define the rate with which the values of model/function parameters will be updated.
	- High learning rate →Rate of change will be high which could even lead to missing the global minima
	- Low learning rate → Rate of change will be low but will take more time converge 

- For convex loss function we will get the results relatively easy than non convex functions.

![[Pasted image 20240716103518.png]]

- Scaling improves the convergence speed (Standardization or Mean centering)

![[Pasted image 20240716103704.png]]
##### Talk about the variants of gradient descent (Batch and Stochastic ) ?

- Batch gradient descent: In this type of GD the parameters are updated after going through the complete dataset per epoch.
- Stochastic gradient descent: In this type of GD the parameters are updated on basis of every singe datapoint which is randomly selected. Basically for the particular epoch if there are total 100 data points then the 100 data points will be selected at random and the parameters will be updated 100 times per epoch.

##### Talk about the drawbacks of using both batch and stochastic gradient descent and how to solve them ?

- In case of batch gradient descent the convergence speed is slow because for every epoch we are utilizing the complete dataset and then making the changes in parameter after complete data. By utilizing the complete data it means that we make the prediction for all the data points using the same parameters and then calculate the loss and then update the parameters.
- In case of stochastic gradient descent since the parameter is done after every data point so the change in the parameter value could be very much abrupt.

So to cover the drawback of  both the variants we use the mini batch gradient descent where we define the batch and then update the parameter values after using that batch only.
