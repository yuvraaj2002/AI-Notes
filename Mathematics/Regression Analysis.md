This page is dedicated towards understanding the concept of regression analysis in the context of machine learning and the resources used for this topic are the videos of the CampusX

- [Session on Regression Analysis.pdf](https://drive.google.com/file/d/1iBcf8Ma5Ueqc0ZIvQeFFltKSVWqBKYoX/view)

[[Linear Regression]]
[[Measure of Dispersion]]


##### What is the difference between Prediction, Inference ?

- Prediction is all about utilizing the past historical data and some statistical algorithm to estimate the relationship in the data and then utilizing that relationship to make future prediction. Using for problems statement such as Medical X-ray disease classification
- Inference is all about studying the relationship between variables in the data and gaining insights about why we got a specific output. Example: Home Price prediction, Loan eligibility problem

##### What is the difference between white box and black box model ? 

- Black box model : It is a type of mathematical model which is very much good at prediction but not good at inference. Example: Neural networks
- White box model : It is a type of mathematical model which is not very good at prediction but very good for inference. Example: Linear regression, Decision tree

##### What do you mean by regression analysis and what is the need of doing this ? 

Regression analysis is a technique which comes under inferential statistics and it is actually used to study the relationship between the variables, to determine the strength of relationship and also to determine whether the relationship is statistically significant or not.

##### What do you mean by statistical inference problems and why machine learning problems are called SIP ? 

Statistical inference problems are those type of problems where we utilize the sample data and some statistical algorithm to make some estimation about the population data.

Every machine learning problem is called statistical inference problem because irrespective of the size of the data we will always be dealing with the sample data only and when we use some algorithm then our main concern is to estimate the relationship that exist in population data. Now because of this estimation about population by using sample data we call ML problems to be statistical inference problems.

##### Why we can't find the true population relationship ? 

Basically in the true population relationship, other than the relation between the independent features and dependent feature, some **hidden variance** also exists which can’t be captured mathematically and due to this it is impossible to estimate the true population. Give example of mood of the interviewer

##### How statistics is related to machine learning ? 

In regression analysis statistics is almost used for all the tasks, to be more precise statistics is used to actually ⬇️

- To determine if the coefficients are statistically significant or not
- How strong is the overall relationship between input and output data.
- What is the standard error of coefficients
- What would be the confidence interval of coefficients for given level of confidence




![[Regression Analysis Chart.png]]


##### What metrics do we use to determine the strength of relationship between variables 

To determine the strength of relationship between independent and dependent variable we use the R2 score and Adjusted R2 score.

- R2 score gives us numerical value ranging between -1 to 1 that gives us a generalized understanding of how well our model is capturing relationship.
- To cover the drawback of R2 score which was that it tends to increase with increase in number of features we use the Adjusted r2 score which tends to decrease in case of addition of some unnecessary features.

##### What metrics do we use to determine whether the regression coefficients are statistically significant or not ? 

To determine whether the regression coefficients are statistically significant or not we conduct [[F Test]] test for overall significance and also calculate p value for the f statistic value.

##### Since the coefficients from single sample will be point estimates so how do we find the confidence interval ? 

##### What is the use of Omnibus, Durbin Watson and Jarque Bera ? 

All these are related to determine the assumptions of [[Linear Regression]]




- What does it mean “To determine if the coefficients are statistically significant or not” and how to check so?
    
    By this statement we basically mean that we want to determine that whether the relationship between this features and the target variable is likely due to chance, or is there a real effect.
    
    <aside> 💡 We can use F test for overall significance to determine if the coefficients are statistically significant or not
    
    </aside>
    

In order to truly understand the F test we need to be aware about some fundamental terms

- What do you mean by TSS, RSS and ESS
    
    - TSS stands for Total sum of squares and it is actually used to represent the overall variance in the data
    - ESS stands for explained sum of squares and it is used to represent the variance explained or captured by the algorithm.
    - RSS stands for residual sum of squares and it is used to represent the uncaptured or unexplained variance in the data even after model fitting
    
    <aside> 🚤 TSS = ESS + RSS
    
    </aside>
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/ebc46c17-d9ec-4ddc-be0e-e1c37ab246fe/Untitled.png)
    
- How would you define degree of freedom ?
    
- What are the various steps which are involved in conducting the f test ?
    
    - Step 1 : Setting up the null and alternative hypothesis, where the null hypothesis would be that there is no linear relationship and all model coefficients except intercept are 0, but alternative hypothesis would be that atleast one coefficient is not zero
    - Step 2 : Fitting the linear regression model and getting the predictions
    - Step 3: Calculating the TSS, RSS and ESS along with the corresponding degree of freedom
    - Step 4: Decide level of significance and calculate the f statistic value which is calculated by dividing the `RSS/df` and `ESS/df`
    - Step 5: Based on calculated f statistic value calculate the p value and compare it with the level of significance and reject or accept null hypothesis
- What is the basic assumption of f test
    
    Normality of residuals
    
- What do you mean by R2 score, what is the use of it and what is the drawback associated?
    
    R2 score is one of the crucial regression metrics which gives us a numerical value ranging between 0 to 1 representing the goodness of fit of the model. Where all the other regression coefficients are contextual, this metric is not contextual and gives us a general idea of how well our model fitted the data. R2 score in short gives us the **proportion of variance explained by the model.**
    
    $$ R^2 Score = (1-SSR)/SST $$
    
    <aside> 💡 In terms of variance we can say that SSR means Sum of squared regressions that is explained variance and SST means sum of squared that is total variance $R^2$ score = 1 being a perfect fit and 0 being a poor fit.
    
    </aside>
    

---

- How do we find whether an individual variable is important or its importance ?
    
    In order to determine whether some individual feature is important or not we can use the t test. Where the t test starts with the following assumptions
    
    - Null hypothesis → Regression coefficients are 0 which means they are not important for predicting output
    - Alternative hypothesis → Regression coefficients are not 0 which means they are important for the prediction of output
    
    After doing so we simply calculate the t statistic value and corresponding p value. Now based on the values we can derive following conclusions
    
    - If p value for regression coefficient is very small than LOS then it means we have strong evidence against the null hypothesis and so we will reject the null hypothesis stating this coefficient is not important. Also the more small will be the p value it would represent its importance for predicting target variable
    - If p value is greater than the level of significance then we will accept the null hypothesis stating current feature is not important at all
- Steps for conducting t test ?
    
    1. Set null and alternative hypothesis test
    2. Find standard error of coefficients
    3. Calculate the t statistic by formula `(Coff_value - 0)/SE(Coff)`
    4. After that calculate the value p value by dividing the t statistic / degree of freedom
    5. Finally analyze p value and the level of significance
- Why do we find the confidence interval for the coefficients and what are the steps involved in finding so ?
    
    ### Why do we find the confidence interval
    
    In machine learning no matter how big the data is, we will always be dealing with the sample data only, and since the regression coefficients are sensitive to the sample data and they might change with change in data (variance), so as a data scientist we rather than only replying on the single coefficient values we find the interval with certain level of confidence and by analyzing confidence intervals, we gain a more better understanding of our regression model.
    
    ### How to find the confidence interval
    
    To find the confidence interval we use the t procedure and there are couple of steps which we need to follow to get the confidence interval. These steps are ⬇️
    
    `Step 1` → Finding the standard error of coefficients → Means finding the standard deviation of the sampling distribution of coefficients
    
    `Step 2` → Calculating the t statistic value and finding the margin of error by multiplying the t value with the standard error
    
    `Step 3` → Add and subtract the margin of error from the coefficient estimate to define the upper and lower bounds of the confidence interval.