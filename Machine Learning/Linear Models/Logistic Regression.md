This page is dedicated towards understanding the concept of logistic regression in machine learning and the resources used for this topic are basically the campusX video, The hands on machine learning book and the blogs posts which will be mentioned below `

- [Introduction to Logistic regression notebook](https://drive.google.com/file/d/1L2AY78TgqOlf7rlsRDZhQABAThqsRQRz/view)
- [Multiclass classification using Logistic Regression](https://drive.google.com/file/d/1neEFkUXbXx5RktYKoPe2qW8CV460G_rX/view)

### Introduction to logistic regression

Before actually understanding the working of the logistic regression we actually needs to be aware about some initial concepts so let us take look at them.

In order to find whether the point belongs to positive region or negative region we simply need to insert the coordinate values in the equation of line and if the result is greater than 0 it means that point lies on positive region of that line and if smaller than 0 it means it lies on negative region.

- Ax + By + C > 0 means Positive region
-  Ax + By + C < 0 means Negative region


##### What is the aim of logistic regression in binary classification problem and how does it find that decision boundary (early approach)? 

In case of binary classification problem, we try to make sure that the decision boundary of the logistic regression is oriented in such a way that all the positive class data points lie in positive region of the decision boundary and all negative class points lie in negative region.

Now in order to find that decision boundary the logistic regression algorithm uses the perceptron trick.

##### What was the drawback associated with perceptron trick ? 

- The major drawback of perceptron trick was that it used the step function which made the classification very strict black and white and only simply assigned a class to a data point rather than giving information about how confident our model is that the data point belong to that class
- Not only this by using perceptron trick we were also not able to quantify how much a decision boundary is better than some other decision boundary.
   
##### How the perceptron trick problem got solved ? 

To solve this problem rather than using the step function, we started using the sigmoid function which gives us the output from 0 to 1, which means it now gives us that how confident our classifier is to about the prediction.

Now with this small change our whole objective changes, as right now we not only want the classifier that correctly classifies the data point but we also want the classifier which maximize in the confidence as well. We use [[Maximum Likelihood Estimation]] to define the objective function (log-likelihood function) in logistic regression. Then, we use [[Gradient Descent]] to find the parameter values that maximize this objective function.

![[Pasted image 20240711194634.png|400]]



### Logistic regression for multiclass classification

- What do you mean by multiclass classification problems
    
    Multiclass classification problems are type of problems where we have more than 2 possible predefined class for the query input

- How can we uses the logistic regression for multi class classification problem ?
    
    Originally logistic regression was designed to only solve binary classification problems but by right now we have 2 different ways using which we can use logistic regression for multi class classification setup ⬇️
    
    1. OVR approach
    2. SoftMax regression aka Multinomial logistic regression
- Explain how does the OVR method works ?
    
    ### What is OVR all about ?
    
    OVR stands for One Vs Rest and it is an approach which is being used to solve multi class classification problem using logistic regression.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/e977d8de-48f7-4499-bb38-4a705cdfa233/Untitled.png)
    
    ### How does OVR works
    
    The core idea behind this approach is that we breakdown multiclass classification problem into binary classification problems and then apply logistic regression on each of Binary classification problem.
    
    After training the models for their respective classes, finally during the prediction phase the class for which we will be getting maximum normalized probability value will be chosen as final output class for the given query input.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/ef681e1c-c7a4-42a4-a013-c1ed6b8667bc/Untitled.png)
    
    <aside> 💡 Number models = Number of classes
    
    </aside>

- When should we apply OVR method ?
    
    OVR should be applied when we have `class imbalance` and when `class are non mutually exclusive` (which means a data point can belong to more than 1 class)

- What are major drawbacks of using OVR method ?
    
    - It can be computationally expensive in case of large data sets
    - It is less interpretable
- How does Multinomial logistic regression works, like tell how is it different from the logistic regression ?
    
    Multinomial logistic regression is another type of technique which is being used for solving the multiclass classification using logistic regression.
    
    Basically in this approach the core idea is that rather that breaking down the multi class problem into multiple binary classification problems, instead we use SoftMax function rather than using the sigmoid function and by doing so we are actually able to create linear decision boundaries for multiple classes using single logistic regression model only.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/b47e7be9-b3db-405a-809e-cb4d1dae38ed/Untitled.png)

- What is the other name for the Multinomial logistic regression
    
    Because of usage of the Softmax function multinomial logistic regression is also called softmax regression
    
- Derive the loss function for the Multinomial logistic regression ?
    
    ![1000009087.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/7d5dfbac-696d-4580-b8a2-44e3757b255e/1000009087.jpg)
    
- When should we use the Multinomial logistic regression
    
    - When we want interpretability and efficiency
    - When classes are mutually exclusive from each other
    - Incase our data is not having class imbalance
- How things work during the prediction for Multinomial logistic regression ?
    
    During the prediction phase since all the decision boundaries/classifiers have been trained so we will simply calculate prediction for each of the class and the class having maximum probability value will be considered as final label for given query input.
