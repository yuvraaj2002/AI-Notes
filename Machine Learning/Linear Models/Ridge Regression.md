This page is actually dedicated towards understanding the concept of Lasso regression and everything related to this algorithm. In this page we will take a look at the code as well.
##### Remaining questions

- [ ] Affect of multicollinearity
- [ ] Meaning of sparsity

### What do you mean by ridge regression and when do we get this ?

Ridge regression is basically a variant of linear regression which we receive after applying L2 regularization on it. Basically the core idea is that in the cost function of the linear regression we add a penalty term to the cost function of linear regression and this penalty term is basically the product of lambda and squared sum of model coefficients. $L = MSE+ƛ(slope_i^2)$. Also other than this addition of the penalty term everything works just like linear regression algorithm.

### What happens to model coefficients after adding penalty term and what happens for very large value of lambda ?

With the increase in lambda value the values of model coefficients starts converging towards 0 and with this the model’s bias increase and variance decrease (Overfitting problem gets solved to some extent). With any high value of lambda the values of parameter will never become 0, and this is because of quadratic term in the penalty term added to cost function of linear regression.

Other than this Higher coefficients get affected more due to change in lambda value as compared to coefficients with smaller value because of quadratic term in penalty term.

![[Ridge_Reg.png]]

### How does lambda affects the bias and variance

As the value of lambda increases the (Bias increase and variance decrease) whereas as the value of lambda decrease bias decrease and variance increase

### When to use ridge regression ?

Ridge regression is used in those kind of scenarios where we are already aware about the features that we will be using for the model training and we only want to deal with the issue of overfitting only.

### Affect of scaling, outliers

- Sensitivity to outliers : Basically when outliers exist in our data then the features generally tends to have high coefficient values but in ridge regression since due to addition of L2 regularization penalty term the model coefficients decrease little bit and due to this the affect of outliers on the overall performance of the model is comparatively less as compared to linear regression without any regularization.

- Sensitivity to scaling : Scaling is always beneficial because for finding the optimal values of model coefficients we use the Gradient descent algorithm, and the gradient descent algorithm converges faster in case our data is properly scaled.

### Program Code

```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import optuna
from tqdm import tqdm

# Generate some sample data
np.random.seed(0)
X = np.random.randn(100, 10)
y = X @ np.random.randn(10) + np.random.randn(100)

  
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

  
# Define the objective function for hyperparameter optimization
def objective(trial):
    alpha = trial.suggest_loguniform('alpha', 1e-4, 1e1)
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train, y_train)
    y_pred = ridge.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return mse
  
# Perform hyperparameter optimization
study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=100)

# Train the final model with the best hyperparameters
best_alpha = study.best_params['alpha']
ridge = Ridge(alpha=best_alpha)
ridge.fit(X_train, y_train)
  
# Predict the target values for the test set
y_pred = ridge.predict(X_test)
  
# Calculate the mean squared error of the predictions
mse = mean_squared_error(y_test, y_pred)

print(f"Best Alpha: {best_alpha}")
print(f"Mean Squared Error: {mse}")
print(f"Coefficients: {ridge.coef_}")
```



