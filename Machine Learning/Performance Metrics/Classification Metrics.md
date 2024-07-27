[Why use harmonic mean](https://www.youtube.com/watch?v=p_0_HhQbsMY)
##### What do you mean by classification metrics, name them?

Classifications metrics are simply the statistical measures that helps us to [evaluate](https://you.com/search?q=Meaning+of+evalutate&fromSearchBar=true) the performance of a machine learning model solving a classification problem. There are a lot of classification metrics but some common ones are

1. Accuracy
2. Precision
3. Recall
4. F1 Score
5. ROC-AUC curve

##### Explain accuracy as evaluation metric and also tell its drawback 

Accuracy is one of the most simplest classification metrics that is used to get the percentage of correctness of our machine learning algorithm. The way we get percentage is by dividing total correct predictions with total predictions.

- In case there is uneven class distribution in the target variable in that case accuracy is not a good metric to use.
- It doesn’t give us any information regarding the type of error which our algorithm is making 🙅🏾, like whether it type1 or type2 error.


##### How much accuracy can be considered to be good ? 

The thing is that accuracy totally depends on the problem statement, and to better understand this point let us take 2 scenarios where in one 95% accuracy will be acceptable but in other it will not be acceptable.

- **95% accuracy is not acceptable**💊Let us assume that we have made a classification-based machine learning model that will help us to find out whether a person is having a brain tumor or not based on the clinical images we will feed into the model. Let's say that we got 95% accuracy but even after getting this much accuracy, it is of no use in the real world because 95% accuracy means that out of 100 people, the chances are that 5 people will be there having brain tumor but our model may not be able to predict it, now since in this case the stakes are very high thus 95% accuracy will not be considered as good accuracy.

- **95% accuracy is good** ⛈️ : Let us assume that we have made a machine learning model that on basis of some parameters such as temperature, humidity and wind speed will give us the predicted date on which rain could happen, in this case even though instead of 95% if we got 80% accuracy that will be considered as good because the stakes are not as high as in the 1st example.


##### Why accuracy is not a good metric in case of class imbalance ? 

To better understand this why accuracy should not be considered as good metric for class imbalance let us assume that we have a dataset in where there are 2 classes A and B and we have in total 100 data points where 98 data points belong to class A and 2 data points belong to class B.

Now rather than using some algorithm even if we will be using a simple function which will assign a class label to the data point based on majority class data point. In that case for all the data points we will get class A as the final label and in such scenario as well we will get 98% accuracy but this is not true representation of performance of our model because our model is not even capable of correctly classifying a single data point of class B


##### Explain what is confusion matrix ? 

Confusion matrix is a classification metrics which got introduced to cover the major drawback of using accuracy of not providing any information about the type of error. By using confusion matrix we not only can find the accuracy but it also tells us about the type of error and also we can calculate other metrics as well like Precision and Recall.In confusion matrix there are around 4 terminologies which we need to keep in mind 👇🏽

1. **True positive** : It means our model is predicting that the output belongs to a particular class and it’s True
2. **True negative** : It means when our model is predicting that the output doesn’t belongs to a particular class and its True
3. **False positive** : It means when our model is predicting that the output belongs to a particular class but in reality that’s the output doesn’t belong to that class
4. **False negative** : It means when our model is predicting that the output doesn’t belongs to a particular class but in reality the output belong to that class

##### What are the different types of errors in machine learning ?

There are 2 different types of errors that is Type 1 error (False positive) and Type 2 error (False Negative), where false positive means that our model is saying that the data point belongs to some specific class but in reality it doesn't, on the other hand type 2 error means the model is saying the data point do no belong to a particular class but in reality it does.

##### Which error is more dangerous ? 

There is not fixed rule that one type of error will always be dangerous than other instead the the severity of the particular error should be completely based on the problem statement. To better understand this let us assume that our model is making type 1 error in 2 different scenarios and we will realize that in one scenario type 1 error will be important but in other it will be not that important.

- Problem Statement 1 : Email spam ham classification : In this problem statement if our model is making type 1 error (False positive) then it means actually that our model said mail is spam but in reality it is not spam, whereas Type 2 error (False negative) would mean our model said email is not spam but in reality it is spam. Now if we will observe then we would realize that Type 1 error here is more dangerous as the mail not spam but labeled as spam could do harm.

- Problem Statement 2 : Heart disease classification : In this problems statement conducting type 1 error would mean that model is saying person is having disease but in reality person is not having disease, whereas the Type 2 error would be like person is not having disease but in reality person does have disease. So in this case `type 2 > type 1` is more dangerous.

##### Explain precision and when to use? 

Precision in single line is basically accuracy of a class and in other words we say that precision is a measure that out of all the data points belonging to a class how many data points **actually** belongs to that class. And precision is used when False positive is doing a lot of harm.

Precision = TP / TP + FP

##### Explain recall and when to use ? 

Recall is a measure that out of all the data points which **actually** belongs to that class how many are correctly classified by the model. Recall is used when Type 2 is more dangerous

Recall = TP / TP + FN



##### What to do incase we don't know which type of error is more dangerous ? 

In case we are not aware about that whether type1 or type2 error is more dangerous we must use F1-Score, which is simply a harmonic mean of precision and recall. Mathematically F1-Score can be defined as 👇🏾

$$F_1 Score = 2*Precision*Recal/(Precision+Recall)$$

Harmonic mean is chosen for the F1 score calculation because it effectively balances precision and recall, punishes extreme values, and provides a comprehensive evaluation of a model's performance

##### What do you mean by AUC ROC curve

![[Pasted image 20240721195136.png]]


![[Pasted image 20240721195148.png]]

![[Pasted image 20240721195201.png]]


