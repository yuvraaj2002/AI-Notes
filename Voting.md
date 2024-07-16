This page is actually dedicated towards understanding the concept of Voting in ensemble learning architectures in machine learning. This page will not only have the theory but also the python programs.

##### What is Voting in Ensemble learning ? 

Voting ensemble is basically a type of ensemble learning architecture where we use different machine learning models as base models and provide same data to each of them during training.

Finally during the prediction stage the query point is provided as input to all base models and outputs from each of the model is finally aggregated and based on the type of problem we are solving like classification or regression we either do the majority count or calculate the average of all models.

![[Pasted image 20240702135149.png]]

##### What is the difference between hard voting and soft voting

- Hard voting: In this type of voting every model gives a class prediction and the final class for the query point is deduced by using the concept of majority count.
- Soft voting: In this type of voting every model rather than giving a class as output, gives class probabilities, and the class which will be having highest average probability will be considered the final output for the query point.
	- Classifier A: [0.7, 0.3] (70% confidence for Class 1, 30% for Class 2)
	- Classifier B: [0.4, 0.6] (40% confidence for Class 1, 60% for Class 2)
	- Classifier C: [0.8, 0.2] (80% confidence for Class 1, 20% for Class 2)
	- Final : Max ( (0.7 + 0.4 + 0.8) / 3) , (0.3 + 0.6 + 0.2) / 3 )

![[Pasted image 20240703101209.png|550]]

```python
from sklearn.datasets import fetch_covtype
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score

# Load dataset
data = fetch_covtype()
X, y = data.data, data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
  
# Create the individual models
log_clf = LogisticRegression(max_iter=1000)
knn_clf = KNeighborsClassifier()

# Create the voting classifier (soft)
voting_clf_soft = VotingClassifier(
    estimators=[('lr', log_clf), ('knn', knn_clf)],
    voting='soft'
)

# Create the voting classifier (hard)
voting_clf_hard = VotingClassifier(
    estimators=[('lr', log_clf), ('knn', knn_clf)],
    voting='hard'
)
  
# Train the voting classifier
voting_clf_soft.fit(X_train, y_train)
voting_clf_hard.fit(X_train, y_train)
  
# Evaluate the voting classifier
y_pred_soft = voting_clf_soft.predict(X_test)
y_pred_hard = voting_clf_hard.predict(X_test)
  
f1_score_soft = f1_score(y_test, y_pred_soft, average='weighted')
f1_score_hard = f1_score(y_test, y_pred_hard, average='weighted')
  
print(f'Voting Classifier F1 Score (soft): {f1_score_soft}')
print(f'Voting Classifier F1 Score (hard): {f1_score_hard}')
```

Just like for the above example for classification let us take a look at voting regressor

```python
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor  # Add this import

# Load dataset
data = fetch_california_housing()
X, y = data.data, data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create the individual models
lin_reg = LinearRegression()
knn_reg = KNeighborsRegressor()  # Ensure this is defined

# Create the voting regressor
voting_reg = VotingRegressor(
    estimators=[('lr', lin_reg), ('knn', knn_reg)]
)

# Train the voting regressor
voting_reg.fit(X_train, y_train)

# Evaluate the voting regressor
y_pred = voting_reg.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Voting Regressor Mean Squared Error: {mse}')
```

