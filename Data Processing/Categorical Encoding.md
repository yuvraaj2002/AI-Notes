This page is dedicated towards understanding how to deal with the categorical attributes and the resources which I have used are mentioned below.

- [The Concept Behind "Mean Target Encoding" in AI & ML | HackerNoon](https://hackernoon.com/the-concept-behind-mean-target-encoding-in-ai-and-ml)
- [K-Fold Target Encoding](https://medium.com/@pouryaayria/k-fold-target-encoding-dfe9a594874b)
    

### Questions

- What do you mean by categorical feature and tell can categorical values be numerical?
    
    A type of feature which rather than having continuous numerical values have fixed number of categories to which a data point will belong to. Yes categorical feature can contain numerical values as well Example: Product rating (1,2,3,4,5)
    
    <aside> 💡 Categorical values are represented using object data type
    
    </aside>
    
- What are the types of categorical values/features and tell the difference between them ?
    
    There are 2 types of categorical values that is **nominal** and **ordinal** categorical values.
    
    |Nominal categorical values|Ordinal categorical values|
    |---|---|
    |The categorical values in which there is no intrinsic hierarchy are called nominal categorical values|The categorical values in which there is some intrinsic hierarchy are called Ordinal categorical values|
    |Example: Colors, gender|Example: Education level|
    
- What do you mean by categorical encoding and why we even need to encode the categorical data?
    
    In the context of machine learning, categorical encoding means giving an appropriate numerical representation to a category so that we could use it for model training or performing some statistical analysis.
    
- What are the various encoding techniques which we can use for encoding the data ?
    
    The use of encoding technique will be based on type of categorical attribute we are having ⬇️
    
    - **`Nominal category`** : One hot encoding, target encoding
    - **`Ordinal category`** : Ordinal encoding
    - **`Label encoding`** : Label encoding
- Explain the working of ordinal encoding ?
    
    _Ordinal encoding is an encoding technique which is used for ordinal categorical values, which are basically those values which have intrinsic hierarchy between them._
    
    ### Working of Ordinal encoding
    
    In case of ordinal encoding we simply map the categorical values to a numerical which represent its hierarchy in the group of values.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5082957f-3d6c-407c-8730-015df254b490/Untitled.png)
    
    <aside> 🛡️ For doing ordinal encoding we can use map function or [Ordinal encoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html) class of scikit learn
    
    </aside>
    
    ```python
    import pandas as pd
    import numpy as np
    
    dict = {'names' : ['Yuvraj','Pravesh','Tanish'],
            'education': ['Bachelors','phd','Master']}
    
    # Let's crete a dataframe
    df = pd.DataFrame(dict)
    
    map_edu = {'Bachelors':0,'Master':1,'phd':2}
    df['education']  =df['education'].map(map_edu)
    ```
    
- What is one hot encoding and explain how does it works ?
    
    _One hot encoding is an encoding technique for nominal categorical values, which are basically those values in which there is no intrinsic hierarchy._
    
    ### Working of One hot encoding
    
    The overall working of one hot encoding can be explained into 3 different steps
    
    1. First this algorithm figure out all the unique categorical values in that column.
    2. After that N new columns are created, where N → Cardinality of that column
    3. Finally the algorithm simply traverse through each and every categorical value and assign 1 to a column if that column is matches the categorical value and 0 if doesn’t.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/94eaebdf-14ed-4793-90d8-df6598374657/Untitled.png)
    
    ### Techniques we can use for doing One hot encoding
    
    For performing one hot encoding we can either use **get_dummies** function of pandas or we can use the [One hot encoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) class of scikit learn.
    
- What are the drawbacks associated with one hot encoding
    
    - Can lead to curse of dimensionality in case the feature contains a lot of categories
    - Leads to perfect multicollinearity making it impossible to calculate model coefficients in multiple linear regression setup
- What do you mean by dummy variable trap?
    
- What to do incase nominal categorical feature have high cardinality and explain it?
    
    Target encoding can be used in that case where target encoding is a nominal categorical encoding technique where we will be giving a numerical representation to the word by utilizing the target attribute.
    
    An important thing to keep in mind is that the target encoding is a broader term and in the target encoding there are many techniques which can be used some of the most common ones are ⬇️
    
    - Mean target encoding
    - Median target encoding
    - Bayesian target encoding
- What are the major drawback of target encoding in general ?
    
    The major drawback of target encoding is that it is very much sensitive to the values of target variable and the categorical distribution of the feature.
    
    - `Sensitivity to target variable` : Let say we have IMDB dataset in which we want to do nominal encoding of the genre feature, now incase the ratings are very biased (very small or very less) due to some reason in that case the target encodings for the category will also be biased.
    - `Sensitivity to categorical distributuion` : In case the nominal feature is having high cardinality but chronic imbalanced categorical distribution, in that case the target encoding will be generally small.
- How does cross validation in target encoding can be used to deal with the problem of overfitting?
    
    In K fold cross validation the intuition will be dividing the overall dataset into k folds and after that for very first time we will consider the 1st fold as test data and remaining for the training data and corresponding to that we will get some values for every category..
    
    - 1st time
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/774f5fe1-6b80-446a-9bda-9ebb05be8a6c/Untitled.png)
        
    - 2nd time
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/87e774a3-22c9-401e-baa3-665a7ce0e4ee/Untitled.png)
        
    
    Finally we will get the numerical values per the fold and at the we will simply find the mean of all the targe encoding values to get the final target encoded value
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/d71ab8e5-32cd-4725-bc5e-46b0bdca38b5/Untitled.png)
    
- What is smoothing and how does smoothing can be used in target encoding to deal with the problem of overfitting?
    

Mean encoding is a type of target encoding where we give the numerical representation to the category by calculating the mean of the corresponding target variable.

- For binary or multiclass target variable
    
    category = frequency count of
    
- For continuous target variable
