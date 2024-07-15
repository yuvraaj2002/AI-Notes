This page is dedicated towards understanding the T test in the hypothesis testing and the main resource used for this topic was the course video of CampusX.

##### When do we use T test and what are conditions ? 

The t-test is a hypothesis test based on the Student's t-distribution and it is used in various scenarios, such as determining if there is a significant difference between a sample mean and a hypothesized population mean when the population standard deviation is unknown, or determining if there is a difference between the means of two independent groups.

- Sample size must be large enough with atleast 30 samples
- Sample must be derived form population following a normal distribution
- Population standard deviation must be unknown

##### T test is based on which distribution ?

T test is based on student t distribution which is simply a continuous probability distribution having a shape similar to that of normal distribution but its shape is very much sensitive to value of degree of freedom. $df = n-1$, where n is number of samples

- For high degree of freedom the shape will become similar to the standard normal distribution, where the tail become lighter and peak become heavier representing smaller variability in the sample mean estimates about population.
- For smaller degree of freedom the shape will move away from standard normal distribution with heavier tails representing high variability in the sample mean estimates  about population.

##### What is the mathematical formula for t test and affects of each value on t value? 

![[Pasted image 20240712072527.png|500]]

In case of 2 mean test for the t test the degree freedom total = degree of freedom 1 + degree of freedom 2
##### Where do we use T test in machine learning ? 

There are 2 main ways using which we can use the T test in machine learning and these 2 are for model performance evaluation and for feature selection

1. Using 2 sample t-test we can actually compare the performance of two machine learning models on the same dataset, such as comparing accuracy, precision, recall, or F1-score using cross validation. If the means of both model performance values will differ then it would mean that one model is outperforming some other model.
2. It can be used for doing feature selection in binary classification problem where we Conduct a t-test to determine if a numerical feature is significantly different between two classes or not.

##### Python Code implementation

```python
import numpy as np  
from scipy import stats  
  
# Sample performance metrics for two models  
model1_performance = np.array([0.85, 0.87, 0.84, 0.86, 0.88])  
model2_performance = np.array([0.80, 0.82, 0.81, 0.83, 0.79])  
  
# Perform 2-sample t-test  
t_stat, p_value = stats.ttest_ind(model1_performance, model2_performance)  
  
print(f"T-statistic: {t_stat}")  
print(f"P-value: {p_value}")  
  
# Interpret the result  
alpha = 0.05  
if p_value < alpha:  
    print("Reject the null hypothesis: There is a significant difference between the two models' performance.")  
else:  
    print("Fail to reject the null hypothesis: There is no significant difference between the two models' performance.")
```
