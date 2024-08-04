This page is dedicated towards understanding the concept of central tendency. The resource used for this topic are mentioned below.

[Notebook](https://drive.google.com/file/d/1da0Wj1KyUxLtGVnFcPTpgWvKQsWjZly-/view)

##### What do you mean by statistics and what are its types?

Statistics is basically a branch of mathematics which deals with collecting, summarizing and analyzing the data. There are basically 2 different type of statistics 

1. Descriptive statistics : Deals with summarizing the data
2. Inferential statistics : Deals with studying the relationship between variables and making the estimates about the data using the sample data and also validating our estimates.

##### What do you mean by measures of central tendency and name them ? 

Measures of central tendency are simply the statistical measures which are used to find the central value of the data and there are various measures of central tendency such as 

1. Mean : Arithmetic, Weighted, Trimmed, Harmonic
2. Median : To find the value which equally divides the data into 2 halves
3. Mode : To find the most frequently occurring element 

##### What is the major drawback of using the measures of central tendency ? 

The major drawback of central tendency is that it only gives us the central value but do not give us any information about the spread of the data. Now because of this if we will be provided with the 2 same central values of different data we will not be able to differentiate them. 

##### What do you mean by measures of dispersion and what is their need ? 

Measures of dispersion are simply the statistical measures which gives us information about the spread of the data and various measures of dispersion are :

1. Range : Difference between maximum and minimum value, but is highly sensitive to outliers
2. Variance : 
3. Standard Deviation : 
4. Inter quartile range
5. Mean absolute deviation
6. Coefficient of variation

##### Talk about the difference among variance and standard deviation in population and sample data


- What do you mean by range and its drawback
    
    Range is one the most simples measure of dispersion and it is used to calculate the difference between maximum and minimum value in the dataset.
    
    <aside> 🧴 The drawback is that it is actually affected by the outlier
    
    </aside>
    
- How do you define variance and how to calculate it for the sample and population data and its drawback ?
    
    Variance can simply be defined as the average of squared deviation of data points from the mean. The units of variance are square of original units.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/00b46b56-9b86-4e1e-8a63-0b062ee70302/Untitled.png)
    
    ### Drawbacks of using variance
    
    - The units are squared of original units
    - Variance is very much sensitive to outliers and give us overestimate of the spread incase outliers are present
- How do you define standard deviation and how to calculate it for the sample and population data
    
    Standard deviation is another measure of dispersion and it is simply the square root of the variance.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/25bd8777-1bd8-4da0-9981-f84db812ecd6/Untitled.png)
    
    ### Advantages of SD over variance
    
    - The units of SD are same as the original units
    - It is less sensitive to outliers
- What is the difference between standard deviation- variance, when to use which one?
    
    ### When to use Standard deviation
    
    Standard deviation should be used when we want to understand the spread of the data in the original with simple interpretation.
    
    Also using standard deviation is useful incase our data have some outliers in it.
    
    ### When to use variance
    
    Variance is specifically useful in case we want to conduct some statistical test such as One way or Two way ANOVA to understand the difference of variances amount group etc.
    
- What do you mean by MAD and what is the drawback ?
    
    As the name suggest MAD helps us to calculate the average of mean deviation of data points from the mean.
    
    Now drawback of this is that in machine learning we generally use some measure of dispersion as the loss/cost function but since MAD is not differentiable at all points thus we can’t use it as differentiable function during the optimization process.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/0fb41f73-d734-4143-b23f-9f7c0243a416/Untitled.png)
    
- What is coefficient of variation and how is it different from other set of measures of dispersion ?
    
    Coefficient of variation is another statistical measure used to understand the spread and this measure is actually free of the units and is simply defined as the ratio of (standard deviation to mean) *100
    
    <aside> 🧴 It gives us information of variability of dataset relative to the mean.
    
    </aside>
    
    CV = (σ/μ) ×100% 
    
    ### Interpretation
    
    - A **low CV** indicates that the data points are close to the mean, suggesting low relative variability.
    - A **high CV** indicates greater dispersion around the mean, suggesting high relative variability.
    
    ### Drawback
    
    1. When the mean of the data set is close to zero, the CV can become extremely large and may not provide meaningful information.
    2. CV is not defined for data sets with a mean of zero or for data sets with negative mean




Variance and standard deviation are both measures of dispersion that describe how spread out the values in a dataset are, but they have distinct differences and unique applications. 

### Differences between Variance and Standard Deviation

1. **Definition**:
   - **Variance**: Measures the average squared deviation of each data point from the mean.
   - **Standard Deviation**: Measures the average deviation of each data point from the mean but in the same units as the data.

2. **Formula**:
   - **Variance**: 
     - Population: \( \sigma^2 = \frac{\sum (x_i - \mu)^2}{N} \)
     - Sample: \( s^2 = \frac{\sum (x_i - \bar{x})^2}{n - 1} \)
   - **Standard Deviation**: 
     - Population: \( \sigma = \sqrt{\frac{\sum (x_i - \mu)^2}{N}} \)
     - Sample: \( s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n - 1}} \)

3. **Units**:
   - **Variance**: The units are the square of the original data units (e.g., if data is in meters, variance is in square meters).
   - **Standard Deviation**: The units are the same as the original data (e.g., if data is in meters, standard deviation is in meters).

4. **Interpretability**:
   - **Variance**: Less intuitive because it is in squared units.
   - **Standard Deviation**: More intuitive and directly comparable to the original data values.

### Why Both Exist and Their Unique Uses

1. **Variance**:
   - **Mathematical Convenience**: Variance is easier to work with mathematically, especially in statistical theory and inferential statistics. For example, in the context of the normal distribution, variance appears naturally in the formulation of many statistical tests and estimators.
   - **Summarizing Dispersion**: Variance is essential in various statistical formulas, including those for calculating the expected value of the squared deviation (e.g., in the calculation of the mean squared error in regression analysis).

2. **Standard Deviation**:
   - **Interpretability**: Since standard deviation is in the same units as the original data, it is easier to interpret and communicate. It provides a direct understanding of the average deviation of data points from the mean.
   - **Practical Usage**: Standard deviation is widely used in practical applications, such as finance (e.g., measuring volatility), quality control (e.g., process variation), and any field where understanding the actual magnitude of variation is crucial.

### Unique Aspects

- **Variance**: Unique in its role in theoretical statistics and its use in various statistical methods that require the squaring of deviations, such as in analysis of variance (ANOVA) and regression analysis. It is also a foundational concept in understanding the properties of different estimators and distributions.
- **Standard Deviation**: Unique in its practical application and intuitive understanding. It provides a clear measure of spread that is directly relatable to the original data, making it useful for comparing the variability of different datasets.

In summary, both variance and standard deviation are crucial in statistics, serving complementary roles. Variance is key in theoretical contexts and mathematical derivations, while standard deviation is preferred for practical interpretation and communication of data variability.