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
- Leads to perfect [[Multicollinearity]] making it impossible to calculate model coefficients in multiple linear regression setup
##### Explain Ordinal encoding works ? 

In case of ordinal encoding we can actually use the scikit learn ordinal encoder class and it will simply take the features values in the order we have defined while instantiation of the class and it will assign a unique integer value representing the hierarchy.


##### What do you mean by cardinality and what should we do incase the nominal categorical feature have high cardinality ? 

The cardinality of the feature means the number of categories present in the feature and incase we have nominal feature with high cardinality then using one hot encoding on it will actually lead to a problem of curse of dimensionality. So rather than using OHE we should use Target encoding, which utilize the target variable value to assign number to a category.

For the target variable with the binary values or target variable with continuous values we can easily replace the categorical value with the mean but for the target variable with more than 2 values let us understand how does it works

| Record | Product_Type | Sales_Category |
|--------|--------------|----------------|
| 1      | A            | Low            |
| 2      | B            | Medium         |
| 3      | C            | High           |
| 4      | A            | Medium         |
| 5      | B            | High           |
| 6      | C            | Low            |
| 7      | A            | High           |
| 8      | C            | Medium         |
For this first of all we will do label encoding and assign a unique integer value to each category in the target variable and after that our table will look like

| Record | Product_Type | Sales_Category | Sales_Category_Numeric |
|--------|--------------|----------------|------------------------|
| 1      | A            | Low            | 1                      |
| 2      | B            | Medium         | 2                      |
| 3      | C            | High           | 3                      |
| 4      | A            | Medium         | 2                      |
| 5      | B            | High           | 3                      |
| 6      | C            | Low            | 1                      |
| 7      | A            | High           | 3                      |
| 8      | C            | Medium         | 2                      |

Now finally we will simply calculate mean for each of the category for example for A = (1+2+3)/3

##### What is the drawback of doing target encoding and how to deal with the issue ? 

The major drawback of target encoding is that in case the number of data points belonging to a specific category is very less in number, then in that case we will suffer from the problem of overfitting because the encoding will become too specific to the current data and with the small change in the data we will get different encoding affecting the model performance.

So to deal with this we use the concept of smoothing where other than the category mean we also incorporate the global mean

$$Encoded Value=(n×Category Mean)+(Global Mean×Smooth Factor)​/n+Smooth Factor$$
