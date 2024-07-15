This page is dedicated towards understanding the concept of the Chi Square test and also how it is used in the field of machine learning. The main resource used for this topic are the course videos of CampusX. But otherwise any resource used will be mentioned below.

[[Feature Selection]]

- [CampusX class notebook](https://drive.google.com/file/d/1nmxMlse95CE0it612u55s9hudL2Xef4K/view) 🔖

##### Talk about what is chi square distribution and its shape analysis

In order to truly grasp the concept of hypothesis test associated with chi square distribution we must first be aware about what is chi square distribution and its characteristics.

Chi square distribution is a continuous distribution which we get after adding the square of values or independent samples coming form normal distribution. Also in the context of this distribution the degrees of freedom is actually = Number of categories - 1 and as these degrees of freedom increases the distribution starts becoming more and more similar to standard normal distribution.

- Mean of this distribution is K
- Variance of this distribution is 2K

##### What are the various tests which are conduced using chi square distribution

There are 2 tests which we can conduct by utilizing the chi square distribution and these tests are goodness of fit test and test for independence. Both of these tests are used for different usecases which are explained below.

##### Is Chi Square test parametric or non parametric ? 

Chi square test is non parametric because while conducting this test we do not make any kind of assumption about the underlying the data which we will be using, just like we used to do in Z or T test. Now because of this chi square is called non parametric. In fact our assumption (that whether the observed distribution matches theoretical distribution) is itself which needs to be tested.

##### Explain goodness of fit test with all steps and how conducted

Goodness of fit is basically a statistical hypothesis test which is used to determine that whether the observed distribution of single categorical variable matches expected theoretical distribution or not. But before conducting this test we need to make sure that 2 conditions are satisfied 

1. The variable must be categorical in nature
2. The observed frequency must be atleast 5

![[Pasted image 20240712103337.png]]

Once both of these conditions are satisfied next we will move on to conducting the test which can be summarized via the following steps 

1. Setting up null and alternative hypothesis
2. Calculating the Chi square value using the expected distribution  and observed distribution
3. Calculate degrees of freedom = Categories and by using the distribution corresponding to degree of freedom, find the p value
4. Compare the p value with level of significance and reject or accept the null hypothesis

##### Why we even care about finding the distribution of variable

Once we understand the underlying distribution of a categorical variable, we can derive more significant insights. For example, knowing the distribution allows us to calculate metrics such as the mean or variance, which can then be used to provide more data-driven solutions to various queries.

##### What are the ways using which we can use goodness of fit test in Machine learning

- Goodness of fit test can be used for evaluation of our model trying to solve a classification problem, basically we will test our model prediction distribution with the actual values distribution and if both the distribution will match based on level of significance and p value then we can infer that our model is performing well.
- Goodness of fit test can also be used for making data driven decision, basically once we will be aware about the distribution of the feature then we will further be able to derive some useful information from that distribution characteristics such as mean and variance which will further help in making data driven decisions.


##### Explain test for independence with steps involved



##### How and where do we use Chi Square test




[Goodness_of_fit.ipynb](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/c8111fe8-67c0-4c30-88a5-f600a0c8a2c0/Goodness_of_fit.ipynb)

- Define what is test for independence and why it is done and steps involved?
    
    Test for independence is basically a hypothesis test which is done to determine whether there is an association between 2 categorical variables or not.
    
    ### Steps involved in this test are ⬇️
    
    1. Setting up the null and alternative hypothesis which in this case would be null → there is no association between categorical variables and alternative → there exist an association
    2. Build a contingency table that summarizes the information of interaction between 2 variables
    3. Calculate the Chi square value and the degree of freedom, where degree of freedom → Number of rows - 1 + Number of columns - 1 of contingency table
    4. By using the chi square distribution for the calculated degree of freedom, we need to calculate the p value
    5. Analyze the p value and level of significance and decide whether to reject or accept null hypothesis
- What are assumptions of test for independence test
    
    - The observations must be independent from each other
    - Variable must be categorical in nature
    - Each category should have an expected frequency of at least 5
- Where can we use the test for independence test
    
    We can use it as feature selection technique given that both the feature and target variable is categorical in nature. By using test of independence we will get to know that whether there actually exist some relationship between these 2 variables or not and if there would be not then we will simply remove that independent feature.
    

[Test_For_Independence.ipynb](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/cac2bcd4-7b8f-4189-b88c-033b12a52d68/Test_For_Independence.ipynb)