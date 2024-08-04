This page is dedicated towards understanding the concept of logistic regression in machine learning and the resources used for this topic are basically the campusX video, The hands on machine learning book and the blogs posts which will be mentioned below `

- [Introduction to Logistic regression notebook](https://drive.google.com/file/d/1L2AY78TgqOlf7rlsRDZhQABAThqsRQRz/view)
- [Multiclass classification using Logistic Regression](https://drive.google.com/file/d/1neEFkUXbXx5RktYKoPe2qW8CV460G_rX/view)

### [What do you mean by logistic regression and how it is different from linear regression](#)

Logistic regression is a supervised machine learning algorithm which is used to solve classification problems, whereas the linear regression algorithm is used to solve the regression problems. Originally logistic regression got introduced to solve binary classification problems but with some modification we can also use it for the multi-class classification problems as well (For that use One Vs Rest approach).

### [What is the main idea behind this algorithm what was the initial technique used to find decision boundary and its drawback](#)

The main idea behind logistic regression algorithm is to simply form a decision boundary which separates the data points belonging to 2 different classes and in order to form this decision boundary earlier the logistic regression used `Perceptron Trick`. But the major drawback of this technique was the usage of step function in it because of which we didn't used to get any information about which decision boundary is more better (given that both decision boundaries are correctly classifying the data points).

![[Perceptron Trick drawback.png]](https://github.com/yuvraaj2002/AI-Notes/blob/master/Machine%20Learning/Images/Perceptron%20Trick%20drawback.png)

### [How the drawback of perceptron trick got solved ?](#)

To solve the problem of not being able to measure the quality of decision boundaries with the step function, we started using the sigmoid function in logistic regression. The sigmoid function outputs a value between 0 and 1, which represents the probability that a given data point belongs to a certain class. This means it gives us an indication of how confident our classifier is about its prediction.

![[Logistic Regression sigmoid.png]](https://github.com/yuvraaj2002/AI-Notes/blob/master/Machine%20Learning/Images/Logistic%20Regression%20sigmoid.png)

With this small change, our objective evolves. Now, we not only want the classifier to correctly classify data points but also to maximize the confidence in its predictions. To achieve this, we use [[Maximum Likelihood Estimation]] to define the objective function, also known as the log-likelihood function, in logistic regression. We then use [[Gradient Descent]] to find the parameter values that maximize this objective function.

![MLE Logistic.png](https://github.com/yuvraaj2002/AI-Notes/blob/master/Machine%20Learning/Images/MLE%20Logistic.png)



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
