
Elastic net regression is basically a middle ground of both ridge and lasso regression and it is used in those kind of scenarios where we are not sure whether to apply ridge or lasso. In elastic net regression in the cost function of linear regression we add 2 penalty terms (Ridge Penalty term and Lasso penalty term)

→ Now since there are 2 penalty terms so we as data scientists need to adjust the importance and we can do so by using **l1_ratio parameter** 0 <= l1_ratio <= 1

`l1_ratio = 0` the penalty is an L2 penalty
`l1_ratio = 1` the penalty is an L1 penalty

Just like in Linear regression in Elastic net regression as well we use the [[Gradient Descent]] algorithm.
```python
import numpy as np
from sklearn.linear_model import ElasticNet
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
    l1_ratio = trial.suggest_uniform('l1_ratio', 0, 1)
    elastic_net = ElasticNet(alpha=alpha, l1_ratio=l1_ratio)
    elastic_net.fit(X_train, y_train)
    y_pred = elastic_net.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return mse

# Perform hyperparameter optimization
study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=100)
  
# Train the final model with the best hyperparameters
best_alpha = study.best_params['alpha']
best_l1_ratio = study.best_params['l1_ratio']
elastic_net = ElasticNet(alpha=best_alpha, l1_ratio=best_l1_ratio)
elastic_net.fit(X_train, y_train)
  

# Predict the target values for the test set
y_pred = elastic_net.predict(X_test)

# Calculate the mean squared error of the predictions
mse = mean_squared_error(y_test, y_pred)
  
print(f"Best Alpha: {best_alpha}")
print(f"Best L1 Ratio: {best_l1_ratio}")
print(f"Mean Squared Error: {mse}")
print(f"Coefficients: {elastic_net.coef_}")
```