This page is dedicated towards understanding the concept of bernoulli distribution in statistics and the resources used for this topic are the course videos of CampusX.

##### What do you mean by bernoulli distribution and examples ? 

Bernoulli distribution is basically a discrete probability distribution which is used to model binary outcomes of some random experiment ,this outcome is either success or failure. Now since we deal with discrete random variable thus the probability distribution function is called Probability mass function which is given by

$$P(X = x) = p^x q^{1-x}$$

1. Tossing a coin for only once will follow bernoulli distribution
2. Rolling a dice and finding the probability of getting even number or not
 
##### What is the parameter associated with this distribution ? 

The only parameter associated with this distribution function is p which is basically the probability of getting a success. For example: If we are given a fair coin and asked about what will be probability of getting heads then p = 0.5, but in case of coin being not fair this p value would not 0.5 as either it will be less or more.

##### What would be the mean and variance of this distribution ? 


##### Explain a situation where using a Bernoulli distribution would not be appropriate.

- In case there are more than 2 outcomes of some random experiment
- The random variable is not discrete in nature

##### How would you test if a given dataset follows a Bernoulli distribution?

- Check if the random variable is having only 2 possible outcomes
- Use [[Chi Square Test]] goodness of fit test to compare the observed distribution and theoretical distribution

##### How would you estimate the parameter p of a Bernoulli distribution from sample data?

We use [[Maximum Likelihood Estimation]] to find the value of p which maximizes the likelihood function ( that means we find that value of p which maximizes the justification of the given output )


