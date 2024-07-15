This notion page is dedicated towards understanding the concept of imbalance data in machine learning and the resources that I have used majorly are the videos of campusX and also the blog posts from analytics vidya.

1. [Imbalanced Data in Machine Learning | Undersampling | Oversampling | SMOTE | Ensemble Methods](https://youtu.be/9h2vxsnX1Ms?si=7KeOCYGxRBEC1jqw)
2. [Stop using SMOTE to handle all your Imbalanced Data](https://towardsdatascience.com/stop-using-smote-to-handle-all-your-imbalanced-data-34403399d3be)




- What do you mean by Imbalanced data in context of classification and regression?
    
    The definition of imbalance in the data will be different for classification and for regression problems.
    
    In the context of _**classification**_ imbalance in data would mean that there is uneven distribution of data points among classses in the target variable. **Example** : Credit card frauds
    
    On the other hand in context of _**regression**_ the imbalance in data would mean that most of data points lie within some specific range only and there are very few data points which are present outside of that range. **Example**: Prices of houses
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df5b8267-8779-43d7-ae73-a3c4a620b3c2/Untitled.png)

- Why do we even need to care about imbalance data ?
    
    Because of presence of imbalance in our data a lot of problems occurs ⤵️
    
    1. The model may get biased towards the majority class because of more training data belonging to majority class.
    2. The results of certain performance metrics becomes misleading like accuracy.

- How accuracy can be misleading can you explain little bit ?
    
    To better understand this let say we are trying to solve a fraud detection problem related to finance. And we need to classify that whether the current transaction is fraudlent or not and since it is obvious the number of fraudulent data points will be less in number than genuine transaction thus it will be case of imbalance in dataset.
    
    let say 95 points are geunine transaction and 5 are fraudulent. Now in this case even if we will use a very dumb classifier which classify all the data points to be geuine in that case also our model will have accuracy of 95% but it is not true representation of performance of the model.

- What are the possible reasons behind imbalance in data ?
    
    1. Data collection or data entry error
    2. Natural phenomenon. Like fraud detection or rare disease prediction usecases will generally have intrinsic imbalance

- What are the various ways using which we can handle imbalanced data?
    
    There are basically 3 different ways using which we can deal with imbalanced dataset⬇️
    1. Resampling technique
    2. Using appropriate evaluation metrics
    3. Using cost sensitive learning 

- What do you mean by resampling and what are its types in context of imbalance data ?
    
    Resampling is a statistical technique which involves taking out multiple samples from the given data with the intent of performing some statistical analysis like validate [[Central limit theorem]], evaluating the model [[Cross Validation]] or improving the model performance by UnderSampling or OverSampling.
    
    In the context of dealing with imbalance data by using resampling we can either Up sample   the minority class or down sample the majority class.

- What is the difference between under sampling and oversampling ?
	In undersampling we down sample the majority class whereas in case of oversampling wedown sample the majority class.

- What is the major drawback of Undersampling ?
    
    If the dataset is having extreme imbalance then doing undersampling will make our dataset thin. And would increase the bias of model and decrase the variance of model
    
- What are the various techniques which we can use for doing oversampling and drawback of oversampling in general ?
    
    There are a lot of approaches which we can use for over-sampling but out of all those techniques there are 3 techniques which are commonly used ⤵️
    
    1. Random over-sampling
    2. SMOTE
    
    ### Drawback of oversampling
    
    - Overfitting is the major drawback associated with oversampling because in oversampling since again and again we are taking the samples from the minority class so duplicate data points will be generated and due to this our model will overfit because by continuously giving same set of input feature values and corresponding output our model will actually learn the outcome instead of understanding the pattern.
    - Using SMOTE we might end up creating data points which are not natural

- Explain the working of SMOTE and drawback of SMOTE ?
    
    SMOTE stands for synthetic minority oversampling technique and it is an advanced algorithm for doing oversampling in which instead of Upsampling the minority class we generate new synthetic data by using the [[K Nearest Neighbor]] algorithm. The steps for generating new synthetic data points are mentioned below 🔽
    
    1. First we select a data point from the minority class
    2. We then calculate its k nearest neighbor
    3. Then we use below formula to get the new datapoint between K nearest neighbors using Interpolation
    
    ![[Pasted image 20240630061052.png|400]]
    
    ### Drawback of SMOTE
    
    - It can be computationally expensive for large dataset
    - It is very much sensitive to value of K, if k is less then we will get similar kind of data points and if k is large then we will get very diverse set of data points which may be unrealistic
    
    [SMOTE](https://towardsdatascience.com/smote-fdce2f605729)
    
- Which evaluation metrics we must use for imbalance data ?
    
    Rather than simply using accuracy, precision or recall either we should use the f1 score or look at overall classification report.
    
    Also we can make our own custom loss function to deal with imbalance data
    
- Other than resampling or using different evaluation metric is there any other method to deal with imbalance
    
    ### Cost sensitive learning
    
    Yes we can actually deal with problem of imbalance by assigning different weights to minority  and majority class data points. Basically we can assign more importance to minority class data points and less importance to majority class data points.
    
    ### Using models less sensitive to imbalance data
    Such as ensemble models such as Xgboost

**ADASYN**: ADASYN focuses on generating synthetic samples for minority class instances that are harder to learn (i.e., those that are near the decision boundary or are sparsely represented).

## SMOTE code

``` python
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE

# Generate an imbalanced dataset
X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0,
                           n_clusters_per_class=1, weights=[0.9, 0.1], flip_y=0, random_state=42)

# Visualize the original imbalanced dataset
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', s=50, cmap='coolwarm')
plt.title('Original Imbalanced Dataset')
plt.show()

# Apply SMOTE to balance the dataset
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Visualize the resampled dataset
plt.figure(figsize=(8, 6))
plt.scatter(X_resampled[:, 0], X_resampled[:, 1], c=y_resampled, edgecolor='k', s=50, cmap='coolwarm')
plt.title('SMOTE Resampled Dataset')
plt.show()
```
