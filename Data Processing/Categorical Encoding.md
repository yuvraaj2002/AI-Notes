This page is dedicated towards understanding how to deal with the categorical attributes and the resources which I have used are mentioned below.

- [The Concept Behind "Mean Target Encoding" in AI & ML | HackerNoon](https://hackernoon.com/the-concept-behind-mean-target-encoding-in-ai-and-ml)
- [K-Fold Target Encoding](https://medium.com/@pouryaayria/k-fold-target-encoding-dfe9a594874b)
    

##### What do you mean by categorical feature, its types and need to encode them ?

The feature which contains some predefined set of values will be called as a categorical feature and normally the categorical feature have values like (Red, blue and green). Now since machine learning algorithms can't understand text or strings thus we need to encode them in such a way that they could be understood by the algorithm. There are 2 different types of categorical features

1. Ordinal features : These are the features which have some hierarchy among the feature values such as Bachelors, Masters and PHD
2. Nominal features : These are the features which do not have some hierarchy among the features such as colors.

##### What are the various encoding techniques which we can use ? 

Based on the type of categorical feature there are different type of encoding techniques which we can use and these are

1. Ordinal features : Ordinal encoding
2. Nominal features : One hot encoding, Target encoding
3. Labels : Label encoding

##### Explain one hot encoding ? 

_One hot encoding is an encoding technique for nominal categorical values, which are basically those values in which there is no intrinsic hierarchy._ The overall working of one hot encoding can be explained into 3 different steps

1. First this algorithm figure out all the unique categorical values in that column.
2. After that N new columns are created, where N → Cardinality of that column
3. Finally the algorithm simply traverse through each and every categorical value and assign 1 to a column if that column is matches the categorical value and 0 if doesn’t.

For performing one hot encoding we can either use **get_dummies** function of pandas or we can use the [One hot encoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) class of scikit learn. 

##### What are the 2 main drawbacks of using one hot encoding ? 

- Can lead to curse of dimensionality in case the feature contains a lot of categories
- Leads to perfect multicollinearity making it impossible to calculate model coefficients in multiple linear regression setup
##### Explain Ordinal encoding works ? 

In case of ordinal encoding we can actually use the scikit learn ordinal encoder class and it will simply take the features values in the order we have defined while instantiation of the class and it will assign a unique integer value representing the hierarchy.


##### 





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
