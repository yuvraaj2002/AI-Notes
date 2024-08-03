This page is dedicated towards understanding the concept of Activation functions in deep learning and the resources used for this topic will be mentioned below. Also rather than simply going over activation functions we must be aware about what qualities make a good activation function.


### What do you mean by activation function, their need and what would happen in the absence of them? 

Activation function is simply a mathematical function which used to determine that whether a particular neuron will activate or not, which in more simpler terms means that whether the output of the neuron will be propagated further or not. 

Also the activation functions are used to add non linearity in the neural network because of which our neural net becomes capable of capturing both linear and non linear pattern in the data and in the absence of activation function or with the use of linear activation function, our neural nets will simply behave like linear regression algorithm capable of only capturing the linear relationship in the data.

### What are ideal properties of activation function ? 

- Non linear : The activation function must be non linear in nature, as because of this only our neural nets will become more stronger at capturing complex relationship in the data.
- Non saturating : Saturating means squeezing the values, and the ideal activation function must be non saturating in nature (which means it should not squeeze the values to specific range) because by doing so our neural net become prone to vanishing gradient descent problem.
- Differentiable : Since every neural net need backpropagation algorithm to get optimized values of weights and backpropagation algorithm involves differentiation, so if we our activation function will not be differentiable in that case we will not be able to use backpropagation.
- Computationally inexpensive : Other than differentiable, the activation function must also be computationally inexpensive in nature.
- Zero centered or Mean centering: Experimentally it has been observed that the the convergence speed of the neural net improves when our data is mean centered (mean = 0), so if activation function makes our data mean centered then it comes under ideal characteristics of activation function.


### Explain step function, its domain range and drawback ? 

Step function is one of the most simplest and inefficient activation function which was being used in the perceptron. This mathematical function maps any real number to the range of 0 or 1. Basically we decide a threshold value which is generally 0.5, and after that any value which is larger than 0.5 is considered to be 1 otherwise it is considered to be 0. The worst thing about this function is that it is not continuous thus we can't use it in the hidden layers and instead can only use them in the output layer

- Domain : Real numbers
- Range : 0,1

Now we will evaluate this activation function based on the above mentioned ideal properties of the activation function.

- It is non linear ❌
- It is saturating ❌
- It is not differentiable ❌
- It doesn't do mean centering ❌

### Explain sigmoid function, its domain range and drawback ? 

Sigmoid function is relatively better activation function that step function because it is continuous and differentiable due to which we can use it in the hidden layers of neural nets, even though it is not recommended. 

- Domain : Real number
- Range : [0,1]

- It is non linear ✅
- It is non saturating  ❌
- It is differentiable ✅
- It is computationally expensive ✅
- It is mean centering ❌

### Explain Tanh function, its domain range and drawback ? 

Tanh stands for Hyperbolic tangent and it is an activation function which just like sigmoid function is also continuous and differentiable in nature, but the  main difference is that it is relatively less saturating than sigmoid and maps any real value between -1 to 1.

- Domain : Real number
- Range : [-1,1]

- It is non linear ✅
- It is non saturating ❌
- It is differentiable ✅
- It is computationally expensive ❌
- It is mean centering ✅

### Explain Relu function, its domain range and drawback ?

Relu stands for rectified linear unit and it is an activation function which got introduced to cover the drawback of tanh which was ( tanh was saturating function from both end), but this function is only saturating towards the negative side. Mathematically it is defined as $relu = max(0,x)$. Now even though the activation function is non saturating towards the positive end but it is not continuous at 0

- Domain : Real number
- Range : [0,Real Number)

- It is non linear ✅
- It is non saturating ❌ (Only towards positive end)
- It is differentiable ✅ (But piecewise)
- It is computationally expensive ❌
- It is mean centering ❌

### What is the issue of dead neurons and what are the reasons behind that, also tell how can we actually solve this issue?

The major problem associated with the use of Relu activation function is the problem called "Dead neurons". Basically if a particular neuron will have a negative value then after passing it through the relu activation function the output will become 0. Now since the output becomes 0 the neuron becomes inactive and can't be revived later and if will happen so with a lot of neurons in the network then the predictive power of the network will get affected and the network with suffer from underfitting.

So to deal with this few variants of Relu got introduced and these are
- Leaky Relu
- Parametric Relu
- Exponential Relu

### Explain the variants of Relu activation function ? 

- Leaky Relu: In this variant of leaky relu, if the input is negative then rather than giving 0 as output it gives us a small value (which we get after multiplying input * alpha). By doing so the problem of dead neurons gets solved. Note that the for the positive inputs the range is 0,R but for negative values the range becomes alpha * input. In short alpha is hyper parameter.
- Parametric Relu: It is an extension over leaky relu where rather than using the alpha as hyper parameter we multiply the negative value with the learnable or trained parameter.
- Exponential Relu: This variant got introduced to not only deal with the issue of dead neurons but also to speed up the convergence speed of the network. Here for the negative input we multiply it with $e^x - 1$

### Explain softmax function, its domain range and drawback ? 












Which activation functions we must use for classification and regression problems ?
    
	_Classification problem_
    
    - In case of binary classification problem
        - Relu → Hidden layer || Sigmoid → Output layer
    - In case of multi class classificaiton problem
        - Relu → Hidden layer || Softmax → Output layer
    
    ### _Regression Problem_
    
    - Relu → Hidden layer || Linear activation function → Output layer

- What are the different type for loss functions for classification and regression problems ?
    
    ### _Regression_ _Loss function_
    
    In case of regression problem we have 3 different type of loss functions
    
    ![Classification ( Loss functions )@2x.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a0287409-e411-477c-97d8-3bb4e98901d3/Classification_(_Loss_functions_)2x.png)
    
    ![This image contains mean absolute error and huber loss](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/90f4220c-a363-4800-b519-d6b9004d3443/SmartSelect_20220917_200713_Edge.jpg)
    
    This image contains mean absolute error and huber loss
    
    ![This image contains mean squared error](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/936c5c97-d372-4687-94bd-4c601b1ca7a3/SmartSelect_20220917_200455_Edge.jpg)
    
    This image contains mean squared error
    
    <aside> ➡️ Huber loss is the combination of MSE and MAE
    
    </aside>
    
    ### _Classification Loss function_

