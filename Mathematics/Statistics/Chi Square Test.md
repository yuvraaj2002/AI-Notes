This page is dedicated towards understanding the concept of the Chi Square test and also how it is used in the field of machine learning. The main resource used for this topic are the course videos of CampusX. But otherwise any resource used will be mentioned below.

- [CampusX class notebook](https://drive.google.com/file/d/1nmxMlse95CE0it612u55s9hudL2Xef4K/view) 

##### Talk about what is chi square distribution and its shape analysis

In order to truly grasp the concept of hypothesis test associated with chi square distribution we must first be aware about what is chi square distribution and its characteristics.

Chi square distribution is a continuous distribution which we get after adding the square of independent samples taken from population following a normal distribution. Also in the context of this distribution the degrees of freedom is actually = Number of categories - 1 and as these degrees of freedom increases the shape of distribution starts approaching towards standard normal distribution.    

![Chi-Square Distribution Shape|450][Mathematics/Chi_Square_Distribution_Shape.png]

- Mean of this distribution is K
- Variance of this distribution is 2K
 
##### What are the various tests which are conduced using chi square distribution

There are 2 tests which we can conduct by utilizing the chi square distribution and these tests are goodness of fit test and test for independence. Both of these tests are used for different usecases which are explained below.

##### Is Chi Square test parametric or non parametric ? 

Chi square test is non parametric because while conducting this test we do not make any kind of assumption about the underlying the data which we will be using, just like we used to do in Z or T test (like in Z test we assume that the sample is taken from the population following a normal distribution). Now because of this absence of any kind of assumption about the data the chi square is non parametric. In fact our assumption (that whether the observed distribution matches theoretical distribution) is itself which needs to be tested.

##### Explain goodness of fit test with all steps and how conducted with help of some example ?

Goodness of fit is basically a statistical hypothesis test which is used to determine that whether the observed distribution of single categorical variable matches expected theoretical distribution or not. But before conducting this test we need to make sure that 2 conditions are satisfied 

1. The variable must be categorical in nature
2. The expected frequency of each category must be atleast 5

![[Pasted image 20240712103337.png]]

Once both of these conditions are satisfied next we will move on to conducting the test which can be summarized via the following steps 

1. Setting up null and alternative hypothesis
2. Calculating the Chi square value using the expected distribution  and observed distribution
3. Calculate degrees of freedom = Categories and by using the distribution corresponding to degree of freedom, find the p value
4. Compare the p value with level of significance and reject or accept the null hypothesis

To better understand this let us assume that dice and we want to test whether the dice is fair or not so for testing this we can use the goodness of fit test. Now if the dice will be fair then it will follow a multinomial distribution which is more generalized version of binomial distribution. And let say we are rolling a dice 60 times and got the results as 

- 1: 8 times
- 2: 12 times
- 3: 9 times
- 4: 11 times
- 5: 10 times
- 6: 10 times

1. Setting up null and alternative hypothesis : The observed distribution is same as expected multinomial distribution implying (The dice is fair dice)
2. The expected values for all the categories will be $60*1/6 = 10$
3. Now we will calculate the chi square test statistic value $χ^2=(8−10)^2​/10+(12−10)^2​/10+(9−10)^2​/10+(11−10)^2/10​+(10−10)^2/10​+(10−10)^2/10 = 1​$
4. Degree of freedom = Number of categories - 1 and that is 6 - 1 = 5
5. For the given level of significance let say 0.05 we will calculate the p value and that will be around 11.07
6. Now since the p value > test statistic value so we will not reject the null hypothesis and our assumption that the dice is following a multinomial distribution will be true (Dice is fair)



##### Why we even care about finding the distribution of variable

Once we understand the underlying distribution of a categorical variable, we can derive more significant insights. For example, knowing the distribution allows us to calculate metrics such as the mean or variance, which can then be used to provide more data-driven solutions to various queries.

##### What are the ways using which we can use goodness of fit test in Machine learning

- Goodness of fit test can be used for evaluation of our model trying to solve a classification problem, basically we will test our model prediction distribution with the actual values distribution and if both the distribution will match based on level of significance and p value then we can infer that our model is performing well.
- Goodness of fit test can also be used for making data driven decision, basically once we will be aware about the distribution of the feature then we will further be able to derive some useful information from that distribution characteristics such as mean and variance which will further help in making data driven decisions.


##### Explain test for independence with steps involved

Test for independence is basically a hypothesis test which is based on chi square distribution and it is used to determine whether there is some relation between 2 categorical variables or not. This test is used for doing feature selection and comes under the Filter based [[Feature Selection]] approach, where if there is not relation between some categorical variable with target variable then we simply remove it.

Just like the goodness of fit test this test is also have 2 main assumptions and these are that the variables must be categorical in nature and also the expected value of each category must be atleast 5

1. Setting up the null and alternative hypothesis which in this case would be null → there is no association between categorical variables and alternative → there exist an association
2. Build a contingency table that summarizes the information of interaction between 2 variables
3. Calculate the Chi square value and the degree of freedom, where degree of freedom → Number of rows - 1 + Number of columns - 1 of contingency table
4. By using the chi square distribution for the calculated degree of freedom and level of significance we need to calculate the p value
5. Analyze the p value and level of significance and decide whether to reject or accept null hypothesis

