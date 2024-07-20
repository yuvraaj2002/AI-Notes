This page is dedicated towards understanding the concept of confidence interval in the inferential statistics and the resource used for this topic is basically the course video of CampusX. 

Here is the [Notebook](https://drive.google.com/file/d/1nskWHtR1ePmrje76k71gdUc2-fcVWvMH/view) Pdf of the class and this is Youtube video about [Mastering Statistics - Vol 3](https://youtube.com/playlist?list=PLnVYEpTNGNtXVA7cR_H85j5Lxw8JOoX1z&si=xCyqwdsM5fibJBVe) 

##### What is the difference between sample, population, parameter and estimate ? 

- Sample : It is the subset of population data and it is used as an representative of the population data to either train some algorithm to figure out the intrinsic pattern and make some predictions using it or to make estimate about the unknown population data.
- Population: It is the complete data in which we are interested in to study about.
- Parameter is a descriptive measure of a population data 
- Estimate is the value calculated from sample data that serves as an approximation for population parameter.

##### What do you mean by inferential statistics and how it is different from descriptive statistics ? 

Inferential statistics is a type of statistics which deals with utilizing the sample data and some statistical technique or algorithm to either make estimates about the unknown population parameter, validate our assumption or study the relationship between variables or features in the sample data.

- Confidence interval
- Hypothesis testing
- Regression analysis

In case of descriptive statistics we are only focused towards providing the descriptive summary of the sample data by using some statistical measures such as mean, median, mode, variance , standard deviation etc.

##### What do you mean by point estimate, how to calculate and its drawback ? 

Point estimate is simply a single numerical value which we calculate by using the sample data and some statistical measure and acts as an estimate or approximation about the unknown population parameter.

Let say we want to find the average height of all the college going student in all across India , now for solving this one way would be to collect the data of all the students and then calculating the average or the other method would be to take the sample data and then calculate the average height from that sample. Now once we will calculate our `sample_mean` this will serve as the point estimate for our unknown population mean.

- The major drawback of point estimate is that it is very much sensitive to the sample data and with the small change in the sample data the point estimate will also change which is not a good thing.

##### How to solve the issue with point estimate ? 

In order to solve the drawback of point estimate that was variability due to change in data, we use concept of confidence interval where we rather than providing a single numerical value as an estimate about the unknown population parameter instead provides a interval with certain level of confidence that the unknown population will fall into.
##### What are the ways to find the confidence interval ? 

In order to find confidence interval we will be using the point estimate as a part of the entire process, basically for the given point estimate value we will calculate margin of error and after that we will add and subtract that margin of error from the point estimate to get the confidence interval.

Now based on our knowledge about the standard deviation of population data we have 2 techniques

1. Z procedure : Used when we are aware about the standard deviation of population data
2. T procedure : Used when we are not aware about the standard deviation of the population data.
##### Explain margin of error ? 

Margin of error is simply a numerical value that is used to represent the variability around the point estimate for the required confidence level. We get margin of error by multiplying the standard error and critical value for specified confidence level.

$$MOE = SE(pe) * CriticalValue_{ConfidenceLevel}$$


##### Explain Z procedure and factors affecting the confidence interval calculated using z procedure ? 

1. Calculate the point estimate
2. Calculate standard error by dividing standard deviation of population data by under root of sample size $SE = Sd(pe)/√n$
3. Calculate the critical value for specified confidence level and multiply this critical value with the standard error of point estimate
4. Add and subtract this margin of error from point estimate 


- Affect of Standard error / Population standard deviation : With higher standard deviation or standard error the margin of error will increase leading to greater confidence level 👉🏻 less reliable
- Affect of sample size : Greater sample size decrease standard error and margin of error leading to narrower confidence interval 👉🏻 more reliable
- Confidence value : With high confidence value the critical value will increase and the margin of error will also increase leading to broader confidence interval 👉🏻 less reliable

##### Explain T procedure and factors affecting the confidence interval calculated using z procedure ? 

Just like Z procedure T procedure is another technique which is used for finding the confidence interval but it is used in those kind of scenarios where we do not have access to the population standard deviation, so we use the sample standard deviation.

1. Calculate the point estimate
2. Calculate standard error by dividing standard deviation of sample data / sampling distribution by under root of sample size $SE = Sd(pe)/√n$
3. Calculate the critical value for specified confidence level and multiply this critical value with the standard error of point estimate
4. Add and subtract this margin of error from point estimate 


 - Affect of Standard error / Population standard deviation : With higher standard deviation or standard error the margin of error will increase leading to greater confidence level 👉🏻 less reliable
- Affect of sample size : Greater sample size decrease standard error and margin of error leading to narrower confidence interval 👉🏻 more reliable
- Confidence value : With high confidence value the critical value will increase and the margin of error will also increase leading to broader confidence interval 👉🏻 less reliable


##### For some unknown population parameter if we have confidence interval of (45,70) with 95% it can be inferred ?

It basically means that if we would take repeated samples from the population data and make a confidence interval for each of the sample then 95% of the times we will be able to capture the true population parameter value. It is about the long term success and not the probability 

