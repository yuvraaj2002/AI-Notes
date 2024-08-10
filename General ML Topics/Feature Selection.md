This notion page is dedicated towards understanding the feature selection techniques and the resources being used for this topic are basically the videos of CampusX and down below I am mentioning the pdf links of the session notebooks 📔    

- [Feature Selection Techniques in Machine Learning (Updated 2023)](https://www.analyticsvidhya.com/blog/2020/10/feature-selection-techniques-in-machine-learning/)
- [CampusX Feature selection (Filter Based)](https://drive.google.com/file/d/1CZPRLuSBmyPw7ftQVIyS7sreoemJGGn-/view)
- [Wrapper Method](https://drive.google.com/file/d/1l0D_YMFkVM8z3I3INn6ou2aCxrHSoeGK/view)
- [Mutual Information, Clearly Explained!!!](https://www.youtube.com/watch?v=eJIp_mgVLwE)

- Syllabus
    
    - What is Feature Selection?
    - Why to do Feature Selection?
    - Types of Feature Selection
    - Filter based Feature Selection
        1. _Duplicate Features_
        2. _Variance Threshold_
        3. _Correlation_
        4. _ANOVA_
        5. _Chi-Square_
        6. _Advantages and Disadvantages_
    
    1. **Session 55: Feature Selection Part 2**
        - Wrapper method
        - Types of wrapper method
        - Exhaustive Feature Selection/Best Subset Selection
        - Sequential Backward Selection/Elimination
        - Sequential Forward Selection
        - Advantages and Disadvantages
    2. **Session on Feature Selection part 3**
        - Embedded Methods
            1. _Linear Regression_
            2. _Tree based models_
            3. _Regularized Models_
        - Recursive Feature Elimination
        - Advantages and Disadvantages


### [What do you mean by feature selection and what are the various techniques used ?](#) 

Feature selection is one of the preprocessing step under feature engineering and the core idea behind feature selection is to chose the subset of most important features from the given set of features so that computational complexity of model could be reduced and data analysis could be  improved. There are 3 different types of techniques used

1. Filter based method
2. Wrapper based method
3. Embedded techniques

### [What is the need of doing feature selection and how it is different from feature extraction ?](#) 

By doing feature selection we get only the most important features from the given set of features and with this the complexity of the model is reduced and the data analysis gets improved.

Now the way it is different from feature engineering is that in case of feature engineering we focus on creating new features by using the current features but in case of feature selection we only chose subset of features

### [What do you mean by filter based feature selection and what are various techniques used in it ?](#) 

Filter based feature selection is a type of feature selection approach where we use some statistical measure to score all the features and only the features which have score more than the threshold we have decided will be considered rest the other features will be ignored. Under filter based feature selection we have various techniques

1. Variance threshold technique : Calculate the variance and the feature with variance less than threshold are ignored. Feature to focus on removing: Constant, or Quasi-Constant feature
2. Correlation technique : Calculate the correlation of feature with the target
3. [[Chi Square Test]] test for independence
4. [[ANOVA test]]
5. Mutual Information

### [What is the major drawback of using filter based feature selection ?](#) 

The major drawback of filter based feature selection is that it is a univariate feature selection technique which do not consider the interaction of the feature with other features so there are chances that the feature might not have pass the threshold score but the feature might be having a strong interaction with some other feature. Example: Longitude might not be having threshold Variance threshold but this feature combined with latitude provide important information.

### [What do you mean by wrapper based feature selection and what are the various techniques used for this](#) 

Wrapper method is a type of technique where we use predictive model to score combinations of the feature and chose that combination which gives us maximum performance results. The various wrapper based feature selection techniques are 

1. Exhaustive feature selection
2. Forward selection
3. Backward selection
4. Recursive feature elimination

### [Explain exhaustive feature selection and its drawback ?](#) 

Exhaustive feature selection is a brute-force approach that evaluates all possible feature combinations to identify the subset of features that gives best results. The major drawback of this technique is that it is computationally expensive.

### [Explain forward and backward feature selection ?](#) 

In case of forward feature selection we start of with an initial feature and then sequentially add the new feature and observe its performance and chose that subset which gives us best result.

![[Pasted image 20240719193150.png|400]]

In case of backward feature selection we start with all the features and then iteratively remove one feature at a time and observe the model performance.

![[Pasted image 20240719193404.png|400]]


### [Explain recursive feature elimination ?](#) 

Recursive feature elimination is a wrapper based feature selection where we start of with all the features, then train a model on all features and remove the weakest feature ( means that feature with lowest feature importance score ). In context of linear models we can use the weights whereas in case of models like decision tree we can use its inbuilt feature importance functionality to identify the weakest feature.

Now after removing the weakest feature the same process is repeated recursively until our required number of features are not achieved


### [Explain embedded feature selection method and how it is different from wrapper method ?](#) 

Embedded methods is another approach which is used for doing feature selection and just like wrapper method it also involves the usage of the machine learning algorithm to find the best set of features, but the only difference is that in case of embedded technique the model training and feature selection happens parallelly whereas in case of wrapper method we either add or remove feature and then observer the model performance.

- **Lasso Regression**: Shrinks some coefficients to zero, selecting features.
- **Tree-Based Methods**: Provide feature importance scores to determine the relevance of features.



    
    

