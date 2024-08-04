This page is dedicated towards understanding the ways to identify and dealing with the missing values and outliers. The resources I have used will be mentioned in the toggle button below.

Tags : [[Data Processing]]


### [What do you mean by missing values, how represented and what could be the reasons behind introduction of missing values ?](#) 

Missing value means the absence of data and they are represented by **NaN** keyword when we load the data using pandas into a data frame. There could be 3 main reasons behind introduction of missing values

1. Data entry error
2. Some sort of error in the measurement tool
3. Due to some preprocessing technique: Let say we are trying to apply some custom mathematical transformation on some feature as preprocessing step and incase we would not be careful about the complete domain of that function and how that will map to the range then there are chances that we might get missing values introduced in our dataset.
4. **Data management** : Generally for the industry level projects the data is collected from various sources and during the merging and storing of data in some data warehouse if data engineer is not cautious about the right approach then missing values could get introduced.


### [Harm of not dealing with missing values](#)

1. Machine learning or deep learning algorithms can't work with the data having missing values
2. Presence of missing values affects our statistical power of analysis because no matter how big our data is, it will most of times be considered as sample data only and if in the sample data itself if there would be missing values then our inference about the population will also get hampered
### [Types of missing values and custom ways to deal with each type?](#) 

1. MCAR : Missing completely at random means the data is missing is completely at random and there is no underlying pattern between missing data and data present in the dataset. **`Solution`** : Univariate Imputation could be less expensive but multivariate imputation can be used as well.

		![[Pasted image 20240630101242.png|400]]

2. MAR : Missing at random means the data is missing at random but there is some pattern or we can say association with the data present. **`Solution`** : Multivariate could be beneficial

		![[Pasted image 20240630101258.png|400]]

3. MNAR : Missing not at  random means the data is missing not at random and the data got removed consciously or intentionally. **`Solution`** : Use multivariate imputation 

		![[Pasted image 20240630101312.png|400]]

### [What are the broader ways to deal with missing values ?](#) 

- Removing the rows or tuples having some missing value
- Imputing the missing value ( Univariate or Multivariate )
	- Univariate imputation : In this type of technique for filling the missing values in some feature we use non null values of that feature only.
	- Multivariate imputation : In this type of technique in order to fill missing value in some feature we utilize the values of other features and train a ML model to identify the pattern that could be used to fill missing values.
### [When to use CCA technique and what is the drawback of using this ?](#) 

CCA which stands for complete case analysis is a technique which is used to remove the missing values from our dataset. The way this technique works is that it removes all those tuples from our dataset where a attribute value is missing.

1. The percentage of missing values in a column must be less than 5% as more than that CCA will make our dataset thin.
2. When we deploy our model then we need to make sure that there are no missing value, because if there will be a missing value it will be removed and the model will not be able to make predictions.

### [What are various imputation techniques and when to use which one ?](#) 

- Use univariate imputation like (Mean, Median and Mode imputation) when percentage of missing values is less than 5%

- Use multivariate techniques like (KNN imputer, MICE, MissForest)  when percentage of missing values is exceeds 5%
	- **MICE**: Uses simpler models like [[Linear Regression]] or logistic regression for imputation and produces multiple imputed datasets.
	- **MissForest (MICE with Random Forest)**: Uses [[Random Forest]] for imputation, capturing more complex relationships, and iteratively refines imputations until they stabilize.


### [What are the ways to identify missing values](#)

- Using **`isnull().sum()`** method to get count of all missing values or **`isna()`**
- Use visualization plots such as bar plot and matrix plot → Gives information that data is not missing at random
    ![[Matrix Plot.png|450]]
    
    This is an example of matrix plot for visualizing the missing values
