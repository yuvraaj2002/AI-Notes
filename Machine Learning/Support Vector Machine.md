This notion page is based on the explanation of everything related to the SVM algorithm. In this page we will talk about everything you need to know about SVM. The resources I have used for understanding this are basically the videos of campusX mentorship program 👨🏾‍🏫

- Notebook for [hard margin svm](https://drive.google.com/file/d/10-cpW7zDF91m1I4Otb2o9h4MVLnQ7CaP/view?usp=sharing)
- Notebook for [soft margin svm](https://drive.google.com/file/d/1M2fdMaMp8fKHZRf4HTkpx7OpdrIOQXeO/view)

First of all we will talk about hard margin and soft margin svm, followed by this we will then move on the concept of kernels in SVM

##### What do you mean by margin and support vector in context of SVM

- Margin can simply be defined as the distance between the support vector and the decision boundary
- Support vector of a class can simply be defined as the vector closest to the decision boundary and the position of the support vector significantly affects the orientation of the decision boundary. 

![[Pasted image 20240719151434.png]]

##### Explain hard margin SVM, its assumptions and the intuition behind algorithm

Hard margin SVM is also called Maximal margin classifier and it is one of the most earliest variant of SVM. Before actually implementing the hard margin SVM we need to make sure that the data is perfectly linearly separable and in the absence of this linearly separable thing hard margin SVM will not work.

The core idea behind the hard margin SVM is to find the margin maximizing decision boundary under the constraint that there must be no margin violation, which means all the data points should be correctly classified and well outside the margin.

- To solve the equation of the hard margin SVM we use quadratic programming

![[Pasted image 20240719152222.png]]

##### Can we solve multiclass classification problem using hard margin SVM

Originally hard margin SVM was introduced to solve binary classification problems but we can also use it to solve the multiclass classification problem by using OVR technique.

In the One-vs-Rest approach, you convert a multiclass classification problem into multiple binary classification problems. Here's a step-by-step explanation:

1. **Binary Classifiers**: For a problem with K classes, you create K binary classifiers. Each classifier is trained to distinguish class i from all other classes.
2. **Training**: Each binary classifier is trained using the original hard margin SVM method. For each classifier, the data points belonging to the class of interest are treated as the positive class, and all other data points are treated as the negative class.
3. **Hyperplanes**: This results in K hyperplanes, each separating one class from the rest.
4. **Prediction**: For a new data point, each binary classifier predicts whether the point belongs to its respective class. The final prediction is typically made by selecting the class with the highest confidence score from the binary classifiers.

##### Why we are so focused on maximizing the margin of decision boundary hyper-plane

In SVM and all its variants the main focus to maximize the margin under given constrain to make sure that the model is robust to the change in data. (We want to minimize the variability of model) thus deal with the problem of overfitting.

![[Pasted image 20240719153352.png]]


##### Why hard margin SVM is most prone to overfitting and talk about drawbacks of hard margin SVM

In case there is some noise or outliers, in that case the SVM is very much prone to overfitting and this is because of its strict margin violation conditions, which states that all the data points must be correctly classified and should lie well outside the decision boundary. This is infact one of the drawback along with the other drawback that it can work only with linearly separable data.


    
- Why hard margin SVM is most prone to overfitting
    
    Hard margin SVM is most prone to overfitting because of its strict constraint that there should be no margin violations and in order to ensure that this constraint is not violated we end up with very small margin which is sign of low bias and high variance
    
- What are some major drawbacks associated with hard margin SVM
    
    - It has very strict margin violation condition because of which it is very much prone to overfitting
    - It only works with perfectly linearly separable data.
    - If there are some outliers in our data then the performance is not very good because the outlier may get misinterpreted as the support vector
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/0cdbb5a3-9a62-4df5-bd9b-1e70c0b82da0/Untitled.png)
    
- How hard margin works during prediction time
    
    - Equate the query point in the hyper-plane or decision boundary equation
    - If the resultant value > 0 → Positive class, otherwise Negative class
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/b1db0907-6ee3-4d75-96db-814b2df04e2b/Untitled.png)
    

<aside> 💒 Before understanding how soft margin SVM deals with the problem associated with the hard margin SVM we needs to be aware about the concept of slack variable.

</aside>

- What do you mean by slack variable and what is the use of it?
    
    Slack variable is a measure used to calculate the degree of misclassification or we can say it is used to quantify the extent to which the margin violation is taking place for given data point
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/49a140c4-3afe-4dde-b504-5777c2a778e4/Untitled.png)
    
- When slack variable value is 0 and 1 what does this means
    
    0 means perfectly classified and 1 means on the decision boundary
    
- When slack variable value lies between 0 and 1 then what does this means
    
    It lies within the margin of the decision boundary
    
- If slack variable value is more than 1 then what does this means ?
    
    Data point is classified incorrectly
    
- What are the possible ranges of slack variable and what information do they provide
    
    There are 4 possible values for slack variable
    
    - exactly 0 → Perfectly classified
    - between 0 and 1
    - exactly 1 → On decision boundary or hyper plane
    - More than 1 → Wrong classification
    
    ![1000009231.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/d04fe0fe-03be-47a7-92ed-47d3e4ffd688/1000009231.jpg)
    
- What do you mean by soft margin SVM and how it solved the drawbacks of hard margin SVM
    
    Soft margin SVM is basically an advancement of hard margin SVM which got introduced to cover the major drawback of Hard margin SVM which was that hard margin SVM due to its strict margin conditions was very prone to overfitting and could only work with linearly separable data.
    
    So to solve this soft margin svm got introduced which used the concept of slack variable to measure the extent to which margin violation is taking place. Basically in the equation of the soft margin svm we also consider the average slack variable value and multiply it by hyperparameter C.
    
    By making such modification we can basically achieve a margin maximizing classifier while controlling the margin violations. In short we can adjust the bias and variance
    
    ### Loss function of the soft margin
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/e8dc590c-b39e-41e2-b6d5-9800dc2944af/Untitled.png)
    
- Talk about bias variance tradeoff associated with C value in soft margin SVM ?
    
    ### For high value of C
    
    Taking high value of C means that we want to minimize the average slack variable value and for doing so we need to make sure that most data points have slack variable value either 0 or close to 0, so in the process of doing so we actually end up creating a very small margin decision boundary leading to overfitting (low bias and high variance)
    
    ### For small value of C
    
    It means we want to maximize the margin and in the process of doing so we actually end up creating a decision boundary with high bias and low variance (Underfitting)
    
- How do we find the value of C ?
    
    Try a range of C values, such as a logarithmic scale $10^−3,10^−2,10^−1,1,10,100,1000)$ and select the value of C that provides the best cross-validation performance.
    

### Questions about the kernels and hyper-parameters

[Why is Kernel Trick Called a "Trick"?](https://open.substack.com/pub/avichawla/p/why-is-kernel-trick-called-a-trick?r=235ihc&utm_campaign=post&utm_medium=email)

- What is the drawback of Soft margin SVC
    
    The major drawback of Soft margin SVC is that it can only work with linearly separable data but fails to work with non linearly separable data in the original feature space.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/f0581b7b-06f7-4caf-b895-b13c04f6baf5/Untitled.png)
    
- How to solve inability of Soft margin SVC to work with non linearly separable data ?
    
    We can actually use the concept of kernel to deal with non linearly separable data. Basically kernel are simply the mathematical function which takes the data point from current feature space and project them in the higher dimensionality feature space (making them linearly separable).
    
    Once we will be able to get the linearly separable data in higher dimension we could then use SVC and form our decision boundary.
    
- What are the different types of kernel function ?
    
    Basically we are free to use any mathematical function to map the data from current feature space to higher dimensional feature space, but we need to make sure that in higher dimensional feature space the data is linearly separable.
    
    Some commonly used kernel functions are ⬇️
    
    1. Linear function
    2. Rbf
    3. Polynomial
    4. Sigmoid
- Do we actually use only kernel to deal with non linearly separable data ?
    
    Even though using kernel functions to transform or map the data from original space to higher dimensional space sounds promising but in reality this process of transforming the data into higher dimension, forming the decision boundary and brining the data back to original feature space is computationally expansive.
    
    So rather than directly using kernel function we use another approach called _**Kernel trick**_
    
- What is kernel trick ?
    
    Kernel trick is an approach for dealing with non linear data, where rather than explicitly using the kernel function to transform the given feature space to higher dimensional feature space, then computing parameters for decision boundary and finally coming back to original feature space, instead we are actually able to get the model parameters in the original feature space itself without ever going to higher dimensional feature space, using some beautiful pieces of mathematics.
    
- How does SVM handle datasets that are not linearly separable?
    
    In case the data in not linearly separable in that scenario SVM uses a technique known as _**kernel trick**_ in which a kernel is used.
    
    > Kernel is a mathematical function that is used to transform the data from current space to high dimensional feature space due to which the data becomes linearly separable.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0c7bc2a2-0e8e-40ec-87df-d77f283ef5e2/Untitled.png)
    
- What do you mean by kernel, why we use it and what are its types?
    
    Kernel is a mathematical function that is used to transform the data from current input space to high dimensional feature space due to which the data becomes linearly separable.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/986099a4-b63b-49ef-bebf-23bbe4aa2898/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/acc1226e-ed9f-4825-b47e-0b793f629e8d/Untitled.png)
    
- How does linear kernel works and why do we use it?
    
    Linear kernel is a mathematical function that is used when the data is linear
    
- What is a kernel function, and how does it affect the SVM classifier?
    
- How does the choice of hyperparameters (e.g., regularization parameter, kernel type) affect the performance of the SVM classifier?
    
- Can SVM be used for multiclass classification problems?
    
- How can SVM be applied in real-world applications, such as image classification or text classification?