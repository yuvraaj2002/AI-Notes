This page is dedicated towards understanding the concept of confidence interval in the inferential statistics and the resource used for this topic is basically the course video of CampusX. 

Tags : [[Mathematics]],

Here is the [Notebook](https://drive.google.com/file/d/1nskWHtR1ePmrje76k71gdUc2-fcVWvMH/view) Pdf of the class and this is Youtube video about [Mastering Statistics - Vol 3](https://youtube.com/playlist?list=PLnVYEpTNGNtXVA7cR_H85j5Lxw8JOoX1z&si=xCyqwdsM5fibJBVe) 


- What is the difference between sample and population ?
    
    Population is the complete data in which we are interested in to study about, but generally since it is not feasible to have access to the complete data so we take a subset of this data which is representative of the complete data and this subset of population is actually called sample
    
- What is the difference between parameter and estimate ?
    
    Parameter is a descriptive measure of a population data whereas the estimate is the value calculated from sample data that serves as an approximation for population parameter.
    
- What do you mean by inferential statistics ?
    
    Inferential statistics is a type of statistics which revolves around estimating the value of  unknown population parameter using the sample data and some statistical technique. Now there could be couple of examples ⬇️
    
     1. Using the sample data and linear regression when we try to estimate the relationship of population data then it comes under inferential statistics
     2. Using the sample data and Z or t procedure when we try to estimate the value of unknown population parameter then it comes under inferential statistics.
    
- What do you mean by point estimate and how to calculate, with example?
    
    Point estimate is a single value estimation of unknown population parameter using sample data and some statistical measure and it actually serves as the best guess.
    
    ### Example 👦🏻
    
    Let say we want to find the average height of all the college going student in all across India , now for solving this one way would be to collect the data of all the students and then calculating the average or the other method would be to take the sample data and then calculate the average height from that sample.
    
    Now once we will calculate our `sample_mean` this will serve as the point estimate for our unknown population mean.
    
- What is the drawback of point estimating the population parameter and how to solve this ?
    
    The major drawback of point estimate is that it is **very much sensitive to the sample data**, so rather than providing the point estimate it is always recommended to provide 2 things ⬇️
    
    1. `Standard error` of sample statistics to provide information about the variability of sample statistic across different samples
    2. `Confidence value` → representing how confident we are that unknown population parameter value will lie within this range only.

- What do you mean by confidence interval ?
    
    Confidence interval is a very robust technique for estimating the unknown population  parameter by providing a interval of values along with certain confidence value. By using this technique the drawback of point estimate can be tackled which was that point estimate was having a very high variability.
    
- For some unknown population parameter if we have confidence interval of (45,70) with 95% it can be inferred ?
    
    It basically means that if we would take repeated samples from the population data and make a confidence interval for each of the sample then 95% of the times we will be able to capture the true population parameter value. It is about the long term success and not the probability 
    




    There are techniques which are used to find out the confidence interval and these are ⬇️
    1. Z procedure
    2. T procedure

- Mention the techniques which we can use to find the confidence interval of statistic ?
    
    There are techniques which are used to find out the confidence interval and these are ⬇️
    
    1. Z procedure
    2. T procedure

- What is margin of error and how does confidence level affects ?
    
    Margin of error is a numerical value which represents what would be the variability around the point estimate for the required confidence level.
    
    - For high confidence level leads to larger critical value and due to this we see high  margin of error → Less precision
    - For low confidence level leads to larger critical value we would see less margin of error → More precision

- How much confidence level is considered to be good
    
    Generally 95% of confidence level is considered to be good, because 95% confidence level  provides us a good balance between the precision and reliable. Otherwise there is always a tradeoff between reliability of estimate and preciseness of the estimation, because high confidence level will give us less reliability and low preciseness but a small confidence interval will give us more reliability and high preciseness.
    
- Explain the Z procedure for finding out the confidence interval ?
    
    Z procedure is used for finding the confidence interval but it is used in those scenarios where the sample size is large enough and population standard deviation is known.
    
    ### Mathematical formula and procedure
    
    - Step 1 → Calculate the point estimate by using the sample data
    - Step 2 → For the given confidence level find the z `value` and multiply it with Population $SD/√n$ → margin of error
    - Step 3 → Add and subtract margin of error from the point estimate to get a confidence interval.

- What are the various factors which affects the confidence interval in z procedure and talk about their affect ?
    
    - Confidence level → More confidence level means larger margin of error leading larger confidence interval to less precision
    - Sample standard deviation → More sample standard deviation means more margin of error, leading to larger confidence interval leading to less precision
    - Sample size → Larger sample size means smaller margin of error, leading to smaller confidence interval and leading to more precision

- Explain what is T procedure, when do we use it and how to use this to find the confidence interval ?
    
    T procedure is one the approach which is used for finding the confidence interval in case the sample size if not large enough and the population standard deviation is not known.
    
    ### Steps used for finding the confidence interval
    
    - Calculating the point estimate using the sample data
    - For the given confidence level find the `t value` critical value and multiply it with `Sample SD/√n` → margin of error
    - Add and subtract this margin of error from the point estimate to get the confidence interval

    Now from the t distribution for the given degree of freedom we will look for t statistic value for selected confidence level. (In practical terms we find the level of significance and then find the value)
    
- What are the various factors which affects the confidence interval in t procedure ?
    
    - Confidence level → More confidence level means larger margin of error leading larger confidence interval to less precision
    - Sample standard deviation → More sample standard deviation means more margin of error, leading to larger confidence interval leading to less precision
    - Sample size → Larger sample size means smaller margin of error, leading to smaller confidence interval and leading to more precision.

- What is the relation between confidence level, level of significance and the types of error ? 
    - Since confidence level and the significance level are inverse proportional to each other so high confidence level mean smaller level of significance 
    - Since significance level is the probability of rejecting null hypothesis even though it is true, so with high confidence level Type 1 error decrease but Type 2 error increase