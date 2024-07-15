
This page is dedicated towards understanding the concept of hypothesis testing and how it is actually used in the field of Artificial Intelligence. Basically the major source for understanding this topic were the course videos of CampusX.

- [Professor Leonard Statistics Lecture 8.2: An Introduction to Hypothesis Testing](https://www.youtube.com/watch?v=ev8cKdrdA4s&list=PL5102DFDC6790F3D0&index=24)
- [An Introduction to Hypothesis Testing](https://www.youtube.com/watch?v=tTeMYuS87oU&list=PLvxOuBpazmsNo893xlpXNfMzVpRBjDH67)
- [Google Colab Notebook](https://colab.research.google.com/drive/13Wplqc6-jSl9Px2JORVCpef0pe2tbfEn?usp=sharing)

##### What do you mean by hypothesis and the need to test it, with example? 

In the context of statistics hypothesis simply means making an assumption about the unknown population parameter and since we are making an assumption thus we need to validate that whether our assumption is right or wrong and for doing so we use the sample data and some statistical technique.

To better understand this let us assume that we want to find the average height of all the college going boys in some region, and in order to do so one way is to get the heights of all such boys and then finding the average of all the heights, but since method is not feasible so instead we make an assumption that the average height will be 160 cm and then we use the sample data (Single branch from each college) and some statistical technique to validate our assumption. 

##### What are the types of hypothesis ? 

- Null Hypothesis : It is a type of hypothesis which is assumed to be true until not proven false and it is denoted as $H_o$
- Alternative hypothesis : Any hypothesis which is contradictory to the null hypothesis we be called alternative hypothesis, denoted as $H_a, H_1$

***Failing to prove null hypothesis wrong or false doesn’t mean null hypothesis is right it just means we haven’t got enough evidence to support alternative hypothesis. As we are always dealing with the sample data only***

##### Fundamental terms (Significance level, Confidence, Critical region, P value)

Now in order to understand the various approaches which are being used for doing the hypothesis testing we need to be first aware about some fundamental concepts such as 

1. Significance level : Level of significance is a numerical value used to represent the probability of rejecting the null hypothesis even though it is true.
	- If LOS high → P(rejecting null hypothesis even though it is true is high)
	- If LOS low → P(rejecting null hypothesis even though it is true is low)

2. Confidence level : Confidence level just like significance level is a numerical value  used to represent the probability of accepting a null hypothesis even though it is wrong. It is basically inversely related to significance level and is calculated by $α = 1 - β$

3. Critical region : Critical region is simply a region under the distribution defined by nature of alternative hypothesis and the level of significance. Basically if test statistic value falls under this region then we simply reject the null hypothesis.

4. P value : It is a numerical value used to represent the likelihood of getting a sample as or more extreme than current sample at hand given the null hypothesis is true. Example: Let say that we are told that we are given a fair coin ( $P(H) = 0.5 =  P(T)$ ) and after generating a sample data of tossing a coin 100 times let say we got 70 heads, now in this case the likelihood of getting a sample more extreme will be less, on the other hand if we would have got 50 heads in that case p value would be high.
	- If p value is smaller than LOS then we reject the null hypothesis because a small p value means that the current sample is actually very rare in itself and casts doubt on the null hypothesis.

##### What are the major approaches being used for testing the hypothesis ? 

When we are doing the hypothesis testing then there are 2 different types of approaches which are being used and these are : 

1. Rejection region approach : If test statistic value falls under the rejection region defined by the level of significance then we simply reject the null hypothesis
2. P value approach : Compare the p value and LOS value and if p value < LOS then reject the null hypothesis

The major drawback of rejection region approach is that it do not give us information about with how much strength we are actually rejecting or accepting the null hypothesis.

##### Types of errors in Hypothesis testing and how they are affected by Significance level


Now since we are already aware about the fundamental concepts behind hypothesis testing so let us now move on to the specific tests which are being conducted.

- [[Z test]]
- [[T test]]
- [[Chi Square Test]]
- [[ANOVA test]]


