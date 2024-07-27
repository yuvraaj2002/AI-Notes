In stacking we have similar configuration as that of the voting but here the only difference is that at the end we add another model called “meta model” which is used to not only perform aggregate operation but also assign importance to each base model based on how correct that model is for most of the times.

During prediction phase the query point is provided to all base models and we get the output from each of the base model and then the aggregation operation is performed based on the importance of each base model.

![[Pasted image 20240702135239.png]]

```python
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
  
# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the base models
base_models = [
    ('knn', KNeighborsClassifier(n_neighbors=3)),
    ('svc', SVC(kernel='linear', probability=True))
]

# Define the meta-model
meta_model = LogisticRegression()

# Create the stacking classifier
stacking_clf = StackingClassifier(estimators=base_models, final_estimator=meta_model)

# Train the stacking classifier
stacking_clf.fit(X_train, y_train)

# Make predictions
y_pred = stacking_clf.predict(X_test)

  
# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy of stacking classifier: {accuracy:.2f}')
```

Just like we looked at the classification now let us take a look at the regression


```python
from sklearn.ensemble import StackingRegressor
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Load the iris dataset (using only the first two features for simplicity)
X, y = iris.data[:, :2], iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the base models
base_models_reg = [
    ('ridge', Ridge(alpha=1.0)),
    ('tree', DecisionTreeRegressor(max_depth=3))
]

# Define the meta-model
meta_model_reg = Ridge(alpha=1.0)

# Create the stacking regressor
stacking_reg = StackingRegressor(estimators=base_models_reg, final_estimator=meta_model_reg)

# Train the stacking regressor
stacking_reg.fit(X_train, y_train)

# Make predictions
y_pred_reg = stacking_reg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred_reg)
print(f'Mean Squared Error of stacking regressor: {mse:.2f}')
```


