This page is dedicated towards understanding the concept of outliers in machine learning and the resources used for this topic are the course videos of CampusX.

[How to Detect and Remove Outliers | Outlier Detection And Removal](https://www.analyticsvidhya.com/blog/2021/05/feature-engineering-how-to-detect-and-remove-outliers-with-python-code/)


### [What do you mean by outliers, what could be the reason behind their presence ?](#) 

Outliers are simply the data point which behave or deviate significantly different from other set of data points in our dataset.

![[Outliers.png|250]]

There could be any reason behind presence of outliers in our dataset, but of the reasons can simply be summarized into 3 different points

1. Data entry errors: Mistakes or typos during data collection or input can lead to outliers. For example, entering a salary as "1000000" instead of "100000" would create an outlier for income level.
2. . Measurement Error → Some fault in the data collection device
3. Due to some preprocessing technique → For example let say we want to transform the current distribution to normal distribution and for doing so log transformation is one the mathematical transformation which we can use, but the thing to kept in mind is that log transformation needs to be specifically used only if the data is right skewed but if the data would be left skewed in that case using log transformation will make things even more worse

### [What is the difference between outliers and noise ?](#) 

Noise represent the data points whose deviation from the general set of data points in our dataset is very less on the other hand Outliers are those data points which have very extreme deviation from rest of data points in the dataset.

Let say that we have the dataset regarding the height of individuals and **most** of the **individuals** are having a **height from 160 to 170 cm**, but apart from this range we have **few individuals** having height of **172 or 175 cm** and also few individuals having ****height like **150 cm and 200 cm.**

- Noise → **172 or 175 cm**
- Outliers → **150 cm and 200 cm** ( representing the dwarf and giant individuals )


### [What is the harm of not dealing with outliers ?](#) 

There are various issues which could arise if we will not be mindful about how to deal with them and some of those issues are 

1. Performance of distance based algorithms (KNN for example) and other algorithms such as linear regression will get affected, but there are also some algorithms which are robust to outliers such as decision tree.
2. Outliers can affect model evaluation phase where we use [[Evaluation metrics]] as MSE, MSE and RMSE all are sensitive to outliers.
3. Outliers can give us over optimistic or over under optimistic results in case we will be using the LOOCV [[Cross Validation]] technique


### [What are the types of outliers ?](#) 

There are basically 3 different categorization of outliers and these 3 different categories are ⬇️

1. `Global outliers` : These are the type of data points which deviate significantly from the general set of data points in our dataset and the number of such data points is generally less. For example, a global outlier in a dataset of human heights might be someone who is over 7 feet tall.
2. `Contextual outliers` : These are set of data points which are  outliers in some specific context but once we will change the context they behave like normal data points. Example : A temperature of 35°C is normal during the summer (context: season) but would be an outlier during the winter.
3. `Collective outliers` :  These are groups of data points that collectively behave like outliers even though the individual data point might not be outlier. Example : A sudden spike in network traffic over a period could be a collective outlier indicating a potential security breach.

### [Could outliers be helpful in any case ?](#) 

Unique thing about outliers is that even though they hamper the performance of certain machine learning algorithms and affect the evaluation metrics results but they also provide us some important information about our dataset given that is not any data entry or data collection error.

Recently I was working on project which was regarding deciding the optimal pricing of Udemy courses based on certain features. During this project I was analyzing the subscriber count of the courses and I found that there were some group of courses which were having very high subscriber count and at first glance these data points seems to be outliers but after careful analysis I got to know that the courses were having high subscriber count due to their low price, specific instructor, and the domain of the course, so in this case outliers actually gave me hidden information.

### [What are the ways to deal with them ?](#)

There are 5 different techniques using which we can deal with outliers ⬇️

1. **Trimming**: Trimming outliers means removing them from the dataset. However, it's important to note that trimming can also lead to a lot of data loss in case there are a lot of outliers in our dataset.
2. **Capping or Winsorization**,: Capping, also known as **Winsorizing**, involves setting a limit or threshold value and them replacing any value lying outside of that threshold value with that threshold value. Capping helps in reducing the impact of outliers but if there are a lot of outliers than it may change the distribution of the feature. To find limits consider the distribution of the feature
3. **Discretization or Binning**: In this technique we convert a numerical feature to categorical feature by creating bins and by creating bins we force the outliers to behave like other set of data points in that bin.
4. **Treating them as missing values:** In this technique we consider outliers and missing values and treat them accordingly.
5. **Mathematical transformation**


### [What are the ways to identify outliers ?](#) 

There are 2 ways to identify outliers in dataset ⬇️

Before using statistical measure to identify outliers we need to be aware about the distribution of that feature. _If feature is normally or sort of normally distributed_ in that case we can actually use the [[Empirical Rule]] which states that 99.7% of data points will be lying in the range from `Mean +- 3SD`. Thus data points outside of this range can be considered as outliers.

In case _feature is skewed_ in that case we can use the upper and lower limit of that distribution to identify the outliers, but calculating the limits we need to find the 1st and 3rd quantile value. Basically we use the measures of [[Dispersion]]

###### [Using graphs and Plots](#)

1. Boxplot
2. Scatter plot
3. Histogram 


