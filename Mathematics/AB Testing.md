This page is dedicated towards understanding the concept of A|B testing and the resources used for understanding this topic are mentioned below  

- [AB testing FreeCodeCamp Course](https://www.youtube.com/watch?v=KZe0C0Qq4p0)
- [PW skills blog](https://pwskills.com/blog/a-b-testing-in-data-science-using-python/)
- [CodeBasics](https://www.youtube.com/watch?v=eiIhTbFP0ls)

##### What is AB testing and the need of this ? 

AB testing which is a also called split testing is a statistical technique where we compare the 2 different versions of something to determine which one is better. It’s widely used in marketing, product development for data driven decision making.

![[AB testing banner.png|450]]

##### What do you mean by control group and experimental group ? 

- Control group is basically used as a reference group and is not exposed to any kind of experimental change
- Experimental group is exposed to the experimental change which needs to be tested.

##### Explain how A|B testing is conducted using some example

The best way we can actually learn something is if we can build some story around that topic and by implementing the same idea we will now take a look at an example through which we will get a real world idea of how do we perform the A|B testing in Data Science.

Problem Statement 🤔 : Let say we want to determine that whether changing the color button on ecommerce website from blue to green will increase the number of purchases or not. Now in order to conduct the A|B testing there are some steps which we need to follow and these are

1. **Objective**: Purchase increases or not ? 
2. **Hypothesis**: Changing the button color to green will not increase purchases. Basically [[Hypothesis Testing]] is being used
3. **Randomization**: Show the blue button (A) to 50% of visitors and the green button (B) to the other 50%.
- **Measurement**: Track the number of purchases from each group over a month.
- Statistical analysis: Here in this case since we need to compare the proportions of successes between two independent samples so we will be using 2 proportion Z test. and calculate z statistic and p value.
- Conclusion: If the p value will be smaller then LOS then we will reject or accept the null hypothesis.


##### Things to keep in mind while conducting AB testing ? 

- There must be no sampling bias, which means that the control and experimental groups must be form randomly
- There are enough samples, because there is always a possibility that if we would have elongated our data collection process from both the groups (control and experimental) we would have got different results

##### How AB testing can be used in Machine learning


**Model comparison** : When you have multiple machine learning models and want to determine which one performs better in a real-world scenario, A/B testing can be used.

**Example:**

- **Objective**: Compare two recommendation algorithms.
- **Hypothesis**: Algorithm B provides better recommendations than Algorithm A.
- **Randomization**: Randomly assign users to either Algorithm A or Algorithm B.
- **Measurement**: Track user engagement metrics (e.g., click-through rate, conversion rate) for each group.
- **Two-Proportion Z-Test**: If you are comparing proportions such as conversion rates or click-through rates between two groups (users exposed to Algorithm A vs. Algorithm B) or **Two-Sample T-Test**: If you are comparing continuous metrics such as average revenue per user or average session duration.
- **Analysis**: Use statistical tests to compare the metrics between the two groups.


**Feature Engineering** Evaluate the impact of new features added to a machine learning model.

**Example:**

- **Objective**: Assess the effect of adding a new feature to a predictive model.
- **Hypothesis**: The new feature improves the model's accuracy.
- **Randomization**: Split data into two groups—one with the new feature and one without.
- **Measurement**: Compare the model performance metrics (e.g., accuracy, precision, recall) for both groups.
- **Paired T-Test**: For comparing the performance of the same model before and after adding the new feature on the same dataset or using the same validation set.
- **Analysis**: Use A/B testing to determine if the new feature significantly improves performance.


##### Can we do such kind of testing on more than 2 versions of something ? 

Yes we can also do ABCD testing as well where we compare more than 2 versions of something but this type of testing is more complex and also when we have 2 options it becomes easy for us to either accept or reject something.