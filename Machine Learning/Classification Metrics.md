
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


##### What are the different types of errors in machine learning and which error is more dangerous ? 


##### Explain precision ? 


##### Explain recall ? 


##### Out of precision and recall when should we use which metric ?


##### What to do incase we don't know which type of error is more dangerous ? 





        
        <aside> 📑 To solve this problem we can use confusion matrix using which we not only get the percentage representing correctness of our machine learning algorithm but also we get information about the type of error which our algorithm is making


- What are the different types of error?
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7fdff5bc-7d0e-4068-a67a-bf2c5915e421/Untitled.png)
    
    <aside> 📑 Out of both Type 1 error are relatively more dangerous, but we should actually consider the problem statement and then decide which error is more dangerous and need more attention
    
    </aside>
    
- Out of type 1 and type 2 error which one is more dangerous
    
    There is not fixed rule that one type of error will always be dangerous than other instead the the severity of the particular error should be completely based on the problem statement.
    
    To better understand this let us assume that our model is making type 1 error in 2 different scenarios and we will realize that in one scenario type 1 error will be important but in other it will be not that important.
    
    ### Problem Statement 1 : Email spam ham classification
    
    In this problem statement if our model is making type 1 error (False positive) then it means actually the mail was spam but our model labeled it as not spam. Now this is not a big deal but instead of this if our model conduct type 2 error (False negative) then it would mean in reality the mail was not spam but our model labeled it as spam and this is not good as mail might be important. So in this case `Type 1 < Type 2`
    
    ### Problem Statement 2 : Heart disease classification
    
    In this problems statement conducting type 1 error would mean that person is having disease but model is unable to detect so this is very crucial, also if the model would conduct type 2 error it would means person is not having disease but model labeled it as disease. So in this case `type 1 > type 2`
    
- What is confusion matrix, and what are the related terminologies?
    
    Confusion matrix is a classification metrics which got introduced to cover the major drawback of using accuracy of not providing any information about the type of error. By using confusion matrix we not only can find the accuracy but it also tells us about the type of error and also we can calculate other metrics as well like Precision and Recall.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/14819077-b609-42c7-9257-b9f10dc32449/Untitled.png)
    
    ### _Terminologies related to confusion matrix_
    
    In confusion matrix there are around 4 terminologies which we need to keep in mind 👇🏽
    
    1. **True positive** : It means our model is predicting that the output belongs to a particular class and it’s True
    2. **True negative** : It means when our model is predicting that the output doesn’t belongs to a particular class and its True
    3. **False positive** : It means when our model is predicting that the output belongs to a particular class but in reality that’s the output doesn’t belong to that class
    4. **False negative** : It means when our model is predicting that the output doesn’t belongs to a particular class but in reality the output belong to that class
    
    ### _Finding accuracy using confusion matrix_
    
    ![SmartSelect_20221117_125820_OneNote.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/969ef3c3-8310-46d4-89b8-1096355bc67b/SmartSelect_20221117_125820_OneNote.jpg)
    
- How the confusion matrix will look for multi-class classification ?
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d5bbdb16-3e25-4747-9b63-35808541e30b/Untitled.png)
    
- What is precision and when should we choose it?
    
    Precision can simply be defined as the accuracy of class predictions made by the model.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/46f90851-176c-4bde-9bdb-202aa196782e/Untitled.png)
    
    ### Visual understanding of concept
    
    ![We are calculating the accuracy of positive predictions](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/865594e5-29a5-450c-a4db-857bcdbc0012/Untitled.png)
    
    We are calculating the accuracy of positive predictions
    
    ### When to use Precision
    
    <aside> 📝 Precision should be used when type 1 error are more dangerous , which means we want to minimize type 1 error
    
    </aside>
    
- What is recall and when should we use it?
    
    Recall is used to measure the number of data points that are correctly classified by the model out of all the data points belonging to that class.
    
    The proportion of correctly classified in actual positives. Mathematically it is defined as 👇🏾
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5436af8c-18a4-4db2-abaa-41ce9e74e035/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ce13968d-f9e2-41af-86ae-f79334c8d747/Untitled.png)
    
    <aside> 📝 Recall should be used when type 2 error are more dangerous, means we want to minimize the false negatives
    
    </aside>
    
- What to do in case we don’t know that which type of error is more dangerous 🤷🏾‍♂️
    
    In case we are not aware about that whether type1 or type2 error is more dangerous we must use F1-Score, which is simply a harmonic mean of precision and recall. Mathematically F1-Score can be defined as 👇🏾
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/97fa38c2-64a4-44b6-b50a-e061f9e2b5b5/Untitled.png)
    
    <aside> 📝 In general, a greater F1 score is better than a smaller score, as it indicates that the classifier has a better balance between precision and recall,
    
    </aside>
    
- Why F1-Score uses harmonic means instead of geometric mean?
    
    Harmonic mean is chosen for the F1 score calculation because it effectively balances precision and recall, punishes extreme values, and provides a comprehensive evaluation of a model's performance
    
- When should we use macro precision and when to use weighted precision?
    
    In case all the classes are equally distributed → Macro precision
    
    In case there is some imbalance within the classes → Weighted precision
    
- ROC AUC curve
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/395111fc-7946-48be-81a0-97bc4f8c43bd/Untitled.png)
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/5ae96611-2f4b-430b-9a1d-bac92ec24862/Untitled.png)
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/3c0dd9c8-f9fa-4762-bdd9-f7092aa97216/Untitled.png)
    

[F1-score | Why exactly Harmonic mean in F1-score? | F1-score for multi-class | Data science Q&A](https://www.youtube.com/watch?v=p_0_HhQbsMY)