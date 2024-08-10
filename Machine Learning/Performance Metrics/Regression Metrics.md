This page is actually dedicated towards understanding the concept of regression metrics in machine learning and the main resource used for this topic are the course video of CampusX.

### [What do you mean by regression metrics and name them](#)

Regression metrics are basically statistical measures which we used to evaluate the performance of a machine learning model trying to solve a regression problem. The used ones are

1. Mean absolute error
2. Mean squared error
3. Root mean squared error
4. R2 Score
5. Adjusted R2 Score

### [Explain MAE and its drawback ?](#) 

MAE stands for Mean absolute error and it used to calculate the average absolute error. The major drawback is that this function is not differentiable at 0 because of which we can't use it as loss function or in the scenarios where we want to use some optimization algorithm such as [[Gradient Descent]].

```python
def mean_abs_error(y_test,y_pred):
	error = 0
    for y_test,y_pred in zip(y_test,y_pred):
    	# Doing the sum of the absolute error
        error = error + np.abs(y_test-y_pred)
        return error/len(y_test)
```

- Other than this advantage is that the units of this metrics are same as that of the original target variable.

### [Explain MSE and its drawback ?](#) 

MSE stands for means squared error and it is actually used to calculate average squared error and the good thing about this thing this metric is that it is differentiable at all the points thus we can use it as loss function and use it with iterative optimization algorithms.

The main drawback is that the units of MSE are squared of the units of the output variable and also it is very much sensitive to outliers.

### [Explain RMSE and its drawback ?](#) 

RMSE stands for Root mean squared error and it is a regression metrics where we calculate the square root of the mean squared error and by using this root the sensitivity to outliers gets somewhat neutralized and the units become same as that of the target variable.

### [Explain R2 Score and how it is different from and its value interpretation ?](#)  

R2 Score is a different metric as compared to other metrics because all other metrics are contextual in nature whereas this metric is context free and instead it gives us numerical value ranging between -1 to 1, and this single numerical value gives us a general understanding of how well our model is actually performing. Mathematically it is ration of Sum of squared error of regression line to Mean line and this ratio is then subtracted from 1.

$$ R^2 Score = (1-SSE_r)/SSE_m $$

- If model is fitting data well then the ratio value will be small and $R^2$ Score will be close to 1
- If model is performing similar to mean line then R2 Score will be 0
- But if we have fitted completely wrong model then we could also get negative score

### [What are the other names for R2 Score ?](#)

- Goodness of fit
- Coefficient of determinant

### [Drawback of R2 Score and how to solve this ?](#) 

The major drawback associated with R2 score is that R2 score either remains same or tends to increase with the introduction of new features irrespective of whether the features are relevant or not. Now the things would have been great if because of the irrelevant features our R2 score would have decreased. So this same thing is implemented in the advance version of R2 score which is called adjusted R2 score.

R2 score increase because the complexity of the model increases and it starts capturing the noise as well and starts moving towards overfitting (low bias and high variance)

![[Pasted image 20240719180337.png]]

