This page is dedicated towards understanding the concept of logistic regression in machine learning and the resources used for this topic are basically the campusX video, The hands on machine learning book and the blogs posts which will be mentioned below `

- [Introduction to Logistic regression notebook](https://drive.google.com/file/d/1L2AY78TgqOlf7rlsRDZhQABAThqsRQRz/view)
- [Multiclass classification using Logistic Regression](https://drive.google.com/file/d/1neEFkUXbXx5RktYKoPe2qW8CV460G_rX/view)

### [What do you mean by logistic regression and how it is different from linear regression and also explain why it is called regression ? ](#)

Logistic regression is a supervised machine learning algorithm which is used to solve classification problems, whereas the linear regression algorithm is used to solve the regression problems. 

The reason behind the usage of term regression comes from the fact that logistic regression algorithms belongs to family of linear models such as (linear, Ridge, Lasso and Elasticnet) regression and creates a linear decision boundary. On the other hand if the data will not be linear we will not get good results because a linear line will not be able to separate the data into classes.

### [What is idea behind logistic regression and what was the initial technique used to find decision boundary and its drawback](#)

The main idea behind logistic regression algorithm is to create a linear decision boundary which separates the data points belonging to 2 different classes and in order to form this decision boundary earlier the logistic regression used `Perceptron Trick`. But the major drawback of this technique was the usage of step function in it because of which we didn't used to get any information about which decision boundary is more better (given that both decision boundaries are correctly classifying the data points).

![[Perceptron Trick drawback.png]](https://github.com/yuvraaj2002/AI-Notes/blob/master/Machine%20Learning/Images/Perceptron%20Trick%20drawback.png)

### [How the drawback of perceptron trick got solved ?](#)

To solve the problem of perceptron trick of not being able to measure the quality of decision boundaries. We started using the sigmoid function rather than step function. 

The sigmoid function outputs a value between 0 and 1, which represents the probability that a given data point belongs to a certain class. This means it gives us an indication of how confident our classifier is about its prediction.

![[Logistic Regression sigmoid.png]](https://github.com/yuvraaj2002/AI-Notes/blob/master/Machine%20Learning/Images/Logistic%20Regression%20sigmoid.png)

With this small change, our objective evolves. Now, we not only want the classifier to correctly classify data points but also to maximize the confidence in its predictions. To achieve this, we use [[Maximum Likelihood Estimation]] to define the objective function or loss function. 

The loss function which we get from MLE is called binary cross entropy and after that we can use [[Gradient Descent]] to find the parameter values that minimize the value of the loss function function.

### [Derive the binary cross entropy loss function using MLE](#)

In order to derive the loss function using MLE there is a mathematical way and other is the intuitive way. So first of all let us understand it the intuitive way to derive the loss function.

![[Intuitive_MLE.png]](https://github.com/yuvraaj2002/AI-Notes/blob/master/Machine%20Learning/Images/Intuitive_MLE.png)

Now we need to find that line for which the likelihood value is maximum, but a point to consider is that we multiply multiple probabilities then we may suffer from problem of underflow so to deal with this we take the log of probabilities.

$$Loss = Log((P_1*P_2*P_3*P_4*P_5...*P_n))$$

After expanding it using the property of Log we will get the loss function value to be 

$$Loss = Log(P_1)+Log(P_2) + Log(P_3) + Log(P_4) + Log(P_5)...Log(P_n)$$

Also since we only need to multiply the probabilities of data point belonging to their actual class thus $Log(P_i)$ can be expanded as $Y_i*Log(Y^{Pred}_i) + (1-Y_i)*Log(1-Y^{Pred}_i)$ . With this for the positive class data point $Y_i = 1$ and for negative class $Y_i$ = 0.

The final change which we need to make to get to our Binary cross entropy function is that we will add negative sign with every Log probability value and the reasons is that value of log between 0 to 1 is negative, so in order to get the negative value we will be adding a negative sign with which our function will become.

$$Loss =  ∑ -Y_i*Log(Y^{Pred}_i) - (1-Y_i)*Log(1-Y^{Pred}_i)$$

With the addition of negative sign, since earlier we use to increase the value now we will try to find those values of model parameter (Weights and bias) for which the loss function is minimum.

![[MLE Logistic.png]](https://github.com/yuvraaj2002/AI-Notes/blob/master/Machine%20Learning/Images/MLE%20Logistic.png)


### [How Logistic regression can be used for multiclass classification](#)

Originally the logistic regression algorithm was created to solve binary classification problems only, but if we want to use it for the multi-class classification problem then we can use the One Vs Rest approach or we can use the categorical cross entropy rather than using binary cross entropy. Generally when we have large number of classes, in that case we prevent using the One vs Rest approach because of its computational complexity.

In One Vs Rest approach we train K different binary classifiers and after training the query point is passed to each of the classifier and the classifier which gives the maximum positive class probability is used as final class for the given data point.

![[OVR approach.png]](https://github.com/yuvraaj2002/AI-Notes/blob/master/Machine%20Learning/Images/OVR%20approach.png)

OVR should be applied when we have `class imbalance` and when `class data ponits are non mutually exclusive` (which means a data point can belong to more than 1 class)

### [Derive the loss function to solve Multiclass classification problem](#)

Because of usage of the Softmax function multinomial logistic regression is also called softmax regression

