This page is actually dedicated towards understanding the concept of Lasso regression and everything related to this algorithm. In this page we will take a look at the code as well.

##### Remaining questions

- [ ] Affect of multicollinearity
- [ ] Meaning of sparsity

### [What do you mean by lasso regression and when do we get this ?](#) 

Lasso regression is basically a specific variant of linear regression which is achieved after applying L1 regularization. Basically the overall idea is that in the cost function of the linear regression we add a penalty term which is basically the product of lambda and the sum of absolute values of model coefficients. $L = MSE + ƛ|coeff|$ Other than this addition of the penalty term everything works just like linear regression algorithm.

### [What happens to model coefficients after adding penalty term and what happens for very large value of lambda ? ](#)

With the increase in the value of lambda the values of model coefficients start approaching towards 0 and for very _**large value the model coefficient can either become 0,**_ which was not the case for ridge regression because of quadratic term in penalty term. Higher coefficients get affected more due to change in lambda value as compared to coefficients with smaller value.

![[Lasso_Reg.png|400]](https://github.com/yuvraaj2002/AI-Notes/blob/master/Machine%20Learning/Images/Lasso_Reg.png)

### [How does lambda affects the bias and variance](#) 

For high value of lambda model coefficients start decreasing and some coefficient even become 0 which lead to reduction in predictive power of the model which means (Bias increase and variance decrease) whereas for smaller value of lambda, bias is low and variance is high

### [When to use lasso regression ? ](#)

Lasso regression must be used only when we are not sure about the final set of features that must be utilized for model training, so in that case we use the lasso regression as it do implicit feature selection. Also Lasso regression is useful when you have high-dimensional data and want to identify the most important predictors by eliminating irrelevant features

### [Why does lasso regression leads to sparsity ?](#) 

In lasso regression due to nature of L1 Norm, basically for very high value of lambda the value of model parameters start approaching towards 0 and some even become 0. Now if some model coefficient will become 0 it would mean that feature is not useful for predicting the target feature and the feature space will become sparse in absence of such feature.


### [Affect of scaling, outliers](#) 

- Sensitivity to outliers : Basically when outliers exist in our data then the features generally tends to have high coefficient values but in ridge regression since due to addition of L2 regularization penalty term the model coefficients decrease little bit and due to this the affect of outliers on the overall performance of the model is comparatively less as compared to linear regression without any regularization.

- Sensitivity to scaling Scaling is always beneficial because for finding the optimal values of model coefficients we use the Gradient descent algorithm, and the gradient descent algorithm converges faster in case our data is properly scaled.

### [Python Program](#)

```python
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import optuna

# Generate some sample data
np.random.seed(0)
X = np.random.randn(100, 10)
y = X @ np.random.randn(10) + np.random.randn(100)
  

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Define the objective function for hyperparameter optimization
def objective(trial):
    alpha = trial.suggest_loguniform('alpha', 1e-4, 1e1)
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    y_pred = lasso.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return mse

# Perform hyperparameter optimization
study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=100)

# Train the final model with the best hyperparameters
best_alpha = study.best_params['alpha']
lasso = Lasso(alpha=best_alpha)
lasso.fit(X_train, y_train)

# Predict the target values for the test set
y_pred = lasso.predict(X_test)
  
# Calculate the mean squared error of the predictions
mse = mean_squared_error(y_test, y_pred)

print(f"Best Alpha: {best_alpha}")
print(f"Mean Squared Error: {mse}")
print(f"Coefficients: {lasso.coef_}")
```
