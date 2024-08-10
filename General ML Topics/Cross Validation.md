This page is dedicated towards the understanding of the concept of cross validation in machine learning and the various variants of cross validation. The resources used are the videos of CampusX course.



### [What do you mean by resampling and what are the reasons behind doing resampling](#)

Resampling is a statistical technique which involves taking out multiple samples from the given data with the intent of performing some statistical analysis, evaluating the model using cross validation or improving model performance by handling imbalanced data.

### [What are various techniques which comes under resampling ?](#)

1. Bootstrap
2. Cross validation

### [Explain hold out method and the drawback](#)

Hold one out is is basically a data preparation step which is done before training the model and in this technique the core idea is that we keep one part of the complete data for doing one task and remaining data for the other task. In the context of machine learning these task are training the model and testing the model.

<aside> 💡 Now because we completely isolate one part of data for doing training of the model, that’s why it is called hold out method.
</aside>

There are 2 major drawbacks associated with hold out method and these are ⬇️

1. **Inefficient usage of the data** : In hold out method since we only use one part of the data for training, so rest of data remains unused for training so there is not efficient usage of complete data for model training.
2. **Variability in model performance**: In scikit learn there is a function called `train_test_split()` which helps us to divide the data into training and test data. Now in case we will not specify the random state then everytime we will get different training and test data and it is obvious that will see some variability in term of model performance and as a data scientist it is not a good thing because we will not be able to provide a single answer to how well our model is performing

 Even though there are drawback but it is used because of these reasons
 
- It is very simple
- It is computationally not expensive


### [What is cross validation, how it works in general and what is the drawback of CV in general  ?](#)

Cross validation is basically a resampling technique which is used for evaluating the performance of the model with change in data. In short we cay say it measures the variance of the model.

Now the way this technique works is that based on the type of CV we divide the data into k folds and then use K-1 folds for training and remaining 1 fold for testing and the same process is repeated k times. Corresponding to the k folds we will get the performance results and at the end we will simply provide the average value of the performance results.

##### Drawback of Cross validation

1. Cross validation becomes computationally expensive in case of large dataset and complex machine learning algorithm
2. Even though cross validation solves the issue of high variability in model performance by giving us the average of the performance results of all the folds but the issue of inefficient usage of data still exists

### [What are the various types of cross validation ?](#)

- Leave one out cross validation
- K fold cross validation
- Stratified cross validation
- Nested k fold
- Repeated k fold


### [Explain leave one out cross validation method and tell what is the major drawback of this technique ?](#)

##### Working of Leave one out cross validation

- Leave one out cross validation is one of the cross validation technique in which for a single instance we use n-1 subsets for training and remaining one for testing.
- The same process is repeated n times and at the end we simply find the average of the evaluation metric values to get the overall understanding of how well our model is performing

##### Drawback of using LOOCV

- It can become very much computationally expensive for the large datasets
- This technique represent high variance because we are using only single data point for testing our model and if in some case that point is outlier then the evaluation metric value will also reflect that outlier thus for small change in testing data point our model will give different result
- It do not give us good result when there is class imbalance. To understand this let say we have 100 data points training data and in this data there are 95 points belonging to some class and remaining 5 to some other class. Now once we will do LOOCV then 95 times the model will be trained on only 1 type of class and due to this its corresponding evaluation metric value will also be very high and due to this overall we will get very high value of evaluation metric which is actually not correct.
- We can’t use all evaluation metrics such as r2 score


### [What do you mean by k fold cross validation and how it is better than leave one out method](#)

K fold cross validation is another type of cross validation technique which got introduced to cover the major drawback of LOOCV technique which was that LOOCV was very much computationally expensive so in this type we simply divide the training data into k folds and then use k-1 folds for training and remaining one for testing. The same process is repeated k times where every time we use different fold for testing and remaining ones for training.

    ![[K Fold.png]]

##### Advantages of K fold over Leave one out cross validation

- It is computationally less expensive as compared to leave one out cross validation
- It is having less variance than LOOCV because here we are not using single data point for testing instead we are using set of data points
- We can now use r2 score as evaluation metric because of more than 1 data point for testing
- The affect of outliers on evaluation metric value is relatively less
- It is little bit more robust to class imbalance

### [What are the drawbacks of k fold cross validation and when to use it then ?](#)

It suffer when there exist class imbalance as there are chances some folds might not contain any data points of minority class which can lead to misleading performance results

<aside> 💡 We must use k fold cross validation when there doesn’t exist class imbalance</aside>

### [How the drawbacks of k fold cross validation can be covered ?](#)

The drawback of K fold cross validation can be solved by using a more advanced version of Cross validation that is stratified cross validation. In this type of cross validation other than simply creating k folds out of training data we also make sure that the each fold contain same distribution of classes as it was in the overall dataset.
    
    ![[Pasted image 20240630171208.png|400]]

### [What is the difference between training, test and validation data ?](#)

- Train data → This subset of complete data is actually used to train the algorithm which involves finding out the relationship between dependent features and independent features or extracting some useful pattern from the data.
- Validation data → This is actually a intermediate data between the training data and test data and it is actually used to validate our model performance before final testing. Basically by using this data we generally do hyper parameter tuning.
- Test data → This is actually the data which we use understanding how well our model will perform in real world scenario.

### [What is the proper ratio between train, test and validation data and what would happen if we change the proportion ?](#)


Basically the common ratio between train, test and validation data is actually 80:10:10, but this is not one size fit for all, instead sometimes the things depend on the algorithm as well and its complexity.

To better understand the affect of the increase and decrease in size of training data let us assume that we have linear regression algorithm.

- For large training data → The model performance might increase as more data means generally means more better understanding but with large size data the computational cost may also increase also the data used for model evaluation will decrease so our confidence 
- For small training data → The model could either overfit due to small data and also underfit due to less data.

    <aside> 💡 So at the end everything is experimental, but if we will move with the ratio of 80:10:10 or 75:15:15 in that case we will not only be having sufficient data for training but also for testing
    </aside>
