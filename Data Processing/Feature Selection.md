This notion page is dedicated towards understanding the feature selection techniques and the resources being used for this topic are basically the videos of CampusX and down below I am mentioning the pdf links of the session notebooks 📔    

- [Feature Selection Techniques in Machine Learning (Updated 2023)](https://www.analyticsvidhya.com/blog/2020/10/feature-selection-techniques-in-machine-learning/)
- [CampusX Feature selection (Filter Based)](https://drive.google.com/file/d/1CZPRLuSBmyPw7ftQVIyS7sreoemJGGn-/view)
- [Wrapper Method](https://drive.google.com/file/d/1l0D_YMFkVM8z3I3INn6ou2aCxrHSoeGK/view)

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


##### What do you mean by feature selection and what are the various techniques used ? 

Feature selection is one of the preprocessing step under feature engineering and the core idea behind feature selection is to chose the subset of most important features from the given set of features so that computational complexity of model could be reduced and data analysis could be  improved. There are 3 different types of techniques used

1. Filter based method
2. Wrapper based method
3. Embedded techniques

##### What is the need of doing feature selection and how it is different from feature extraction ? 

By doing feature selection we get only the most important features from the given set of features and with this the complexity of the model is reduced and the data analysis gets improved.

Now the way it is different from feature engineering is that in case of feature engineering we focus on creating new features by using the current features but in case of feature selection we only chose subset of features

##### What do you mean by filter based feature selection and what are various techniques used in it ? 

Filter based feature selection is a type of feature selection approach where we use some statistical measure to score all the features and only the features which have score more than the threshold we have decided will be considered rest the other features will be ignored. Under filter based feature selection we have various techniques

1. Variance threshold technique : Calculate the variance and the feature with variance less than threshold are ignored. Feature to focus on removing: Constant, or Quasi-Constant feature
2. Correlation technique : Calculate the correlation of feature with the target
3. [[Chi Square Test]] test for independence
4. [[ANOVA test]]
5. Mutual Information

##### What is the major drawback of using filter based feature selection ? 

The major drawback of filter based feature selection is that it is a univariate feature selection technique which do not consider the interaction of the feature with other features so there are chances that the feature might not have pass the threshold score but the feature might be having a strong interaction with some other feature. Example: Longitude might not be having threshold Variance threshold but this feature combined with latitude provide important information.

##### What do you mean by wrapper based feature selection and what are the various techniques used for this 

Wrapper method is a type of technique where we use predictive model to score combinations of the feature and chose that combination which gives us maximum performance results. The various wrapper based feature selection techniques are 

1. Exhaustive feature selection
2. Forward selection
3. Backward selection
4. Recursive feature elimination

##### Explain exhaustive feature selection and its drawback ? 

Exhaustive feature selection is a brute-force approach that evaluates all possible feature combinations to identify the subset of features that gives best results. The major drawback of this technique is that it is computationally expensive.

##### Explain forward and backward feature selection ? 

In case of forward feature selection we start of with an initial feature and then sequentially add the new feature and observe its performance and chose that subset which gives us best result.

![[Pasted image 20240719193150.png|400]]

In case of backward feature selection we start with all the features and then iteratively remove one feature at a time and observe the model performance.

![[Pasted image 20240719193404.png|400]]


##### Explain recursive feature elimination ? 

Recursive feature elimination is a wrapper based feature selection where we start of with all the features, then train a model on all features and remove the weakest feature ( means that feature with lowest feature importance score ). In context of linear models we can use the weights whereas in case of models like decision tree we can use its inbuilt feature importance functionality to identify the weakest feature.

Now after removing the weakest feature the same process is repeated recursively until our required number of features are not achieved



### Questions about filter based techniques

Here is the link to the 

- What do you mean by filter based feature selection technique ?
    
    Filter based feature selection technique is basically a univariate feature selection technique where we use some statistical measure and define a threshold value corresponding to that measure.
    
    After that the features for which the statistical value is more than threshold, only they are considered and rest are dropped.
    
- In filter method what are the various techniques we can use?
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/3c01fe12-9cc3-4f02-97fe-f6d8d9cf5ee1/Untitled.png)
    
- Explain variance threshold method?
    
    Variance threshold is one of the most simplest filter based feature selection technique where we first define the `minimum variance threshold` and after that all features having variance `less` than the threshold value are removed.
    
    <aside> 🎐 This technique is used identify and remove features that have low variance generally constant (same value feature) or quasi-constant features (Feature with extremely small variability).
    
    </aside>
    
    - Formula of variance
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/15384965-7d73-45e2-bfa9-bc1889233ee2/Untitled.png)
        
    - Video to understand variance
        
        [https://www.youtube.com/watch?v=sOb9b_AtwDg](https://www.youtube.com/watch?v=sOb9b_AtwDg)
        
- What are drawbacks of Variance threshold method
    
    1. This technique is univariate in nature because of which there is strong possibility that even if the current feature independently might not seem important but the same feature might have strong relationship with other features making it a strong feature. Example: Longitude and latitude.
    2. Sensitive to data scaling
    3. It is difficult to decide a minimum variance threshold value. Generally it is recommended to use any value between 0.01 to 0.1
- Explain correlation analysis method, techniques and the range interpretation?
    
    Correlation analysis method is an important filter based feature selection technique where we select the feature based on their correlation with the target variable.
    
    - We define the threshold value and the features which have more correlation value than the threshold value are considered and remaining are ignored
    
    <aside> 💡 Other than doing correlation with the target variable, the correlation among features is also done to address the issue of the multicollinearity.
    
    </aside>
    
    ### Correlation techniques used
    
    - Spearman’s rank correlation method
    - Pearson correlation method
    
    <aside> 💡 +1 means strong positive correlation, -1 means strong negative correlation and 0 means no correlation at all
    
    </aside>
- What are drawbacks of correlation method
    
    1. Correlation measures the linear relationship between two variables. It does not capture non-linear relationships well.
    2. Correlation only measures the relationship between two variables at a time. It may not capture complex relationships involving more than two variables.
    3. Sensitive to outliers and threshold value

The rest 2 methods are basically the hypothesis tests so we need to be aware about how does Chi square and ANOVA works to actually get better understanding of this techniques.

- Explain ANOVA test for feature selection ?
    
    - Mention how 1 Way ANOVA test is used in the context of machine learning
        
        One-way ANOVA can be used as a feature selection technique in machine learning to determine which features (independent variables) have a significant effect on the target variable (dependent variable)
        
        For example, in a credit risk prediction problem, you may have several features like age, income, credit history, etc. One-way ANOVA can help identify which of these features have a significant impact on predicting credit risk
        
        The steps would be:
        
        1. Treat each feature as a factor with different levels (values)
        2. Perform one-way ANOVA to test if the mean of the target variable is significantly different across the levels of each feature
        3. Select the features with p-values less than the significance level (e.g. 0.05)
        
        This helps reduce the dimensionality of the dataset by removing irrelevant features, improving model performance and interpretability
        
- Explain Chi-Square for feature selection ?
    
    - Where can we use the test for independence test
        
        We can use it as feature selection technique given that both the feature and target variable is categorical in nature. By using test of independence we will get to know that whether there actually exist some relationship between these 2 variables or not and if there would be not then we will simply remove that independent feature.
        
- How Mutual info can be used for doing the filter based feature selection ?
    
    This is an amazing resource that we can use to understand this approach
    
    [Mutual Information, Clearly Explained!!!](https://www.youtube.com/watch?v=eJIp_mgVLwE)
    
