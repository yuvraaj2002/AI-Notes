This notion page is dedicated towards understanding the concept of central limit theorem and the main resource I have used for this concept is the video of [CampusX](https://www.youtube.com/live/-WmJDYBor7c?si=TEF7HVgtnqndHU8O) and 3Blue1Brown [But what is the Central Limit Theorem?](https://youtu.be/zeJD6dqJ5lo?si=2rD6KvWyzaPkM-n3)

Tags : [[Mathematics]]

Before moving on to the concept of central limit theorem we actually need to be aware about what is sampling distribution, because CLT theorem is somehow related to it.

- What do you mean by sampling distribution ?
    
    Sampling distribution is simply distribution of sample statistic values, where every value is a statistical measure used for summarizing its corresponding sample data.
    
	![[Pasted image 20240629143346.png|500]]
	Sample size must be same for all the samples and same statistical measures should be used

- What are the uses of sampling distributions ?

	Sampling distribution gives us valuable information about the variability of sample statistics. When this variability is high, it highlights the importance of focusing on confidence intervals rather than point estimates to make more accurate and reliable inferences about the population.

- Define central limit theorem
    
    Central limit theorem is a crucial theorem in the field of inferential statistics and it states that  the distribution of means (Sampling distribution) of large enough independent samples will always approach normal distribution irrespective of distributions of the samples.
	![[Pasted image 20240629144636.png]]

- What is the practical use of central limit theorem ?
    
    The central limit theorem can be used to make inferences about the population by using the sample. To better understand this let us assume that we want to find the average income of Indian male working individuals.
    
    One way would be to have access to all the population data and then calculate the average but this method is not feasible so we will be using the central limit theorem here to make inference about the unknown population parameter.
    
    ### Steps we will follow to find the average income of Indian working male
    
    - Collect multiple large enough diverse samples from the overall population data
    - Calculate means of the such samples and plot the sampling distribution
    - By relying the on CLT we will get a normal distribution and we will calculate the mean of this sampling distribution and this will be our estimated average salary of Indian working professional.
    - Now since the point estimate is never trust worthy so we will provide a confidence interval and for that we will have to calculate standard error associated with the sampling distribution.
    - After that based on given confidence level we can provide a confidence interval 

	![[Pasted image 20240629145154.png]]

- Can you tell the usage of central limit theorem in the field of machine learning ?

	Central limit theorem is actually used to evaluate the model performance and here is the step by step explanation of the steps.
	
	- **Step 1**: Perform k-fold cross-validation on your dataset. This involves splitting your dataset into k folds, training your model on k−1 folds, and testing it on the remaining fold. Repeat this process k times, each time using a different fold for testing.
	
	- **Step 2**: For each fold, compute the performance metric (e.g., accuracy, precision, recall). This gives you k performance metric values.

	- **Step 3**: Calculate the mean of these k performance metric values. This gives you a single mean performance metric for this round of cross-validation.

	- **Step 4**: Repeat the entire cross-validation procedure multiple times (e.g., 30 or 50 times). Each time, randomly shuffle your dataset before performing k-fold CV to ensure different splits. This gives you a new set of performance metric values each time.

	- **Step 6**: Plot the distribution of these 50 mean accuracy values. According to the CLT, this distribution of means will approximate a normal distribution if the number of repetitions is sufficiently large.
	
	The spread of this distribution gives you an idea of the variability in your model's performance metric. A wider spread indicates more variability.

Here is the python program to understand all the above bullet points

```
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

# Generate a dummy dataset
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Initialize the model
model = RandomForestClassifier()

  
# Parameters
k = 5  # number of folds
num_repeats = 50  # number of repetitions

# Store mean accuracy values
mean_accuracy_values = []
  
for _ in range(num_repeats):

    # Shuffle the dataset
    indices = np.random.permutation(len(X))
    X, y = X[indices], y[indices]
    
    # Perform k-fold cross-validation
    kf = KFold(n_splits=k)
    accuracy_values = []

    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        # Train the model
        model.fit(X_train, y_train)

        # Test the model
        y_pred = model.predict(X_test)

        # Compute the performance metric
        accuracy = accuracy_score(y_test, y_pred)
        accuracy_values.append(accuracy)

    # Calculate the mean accuracy for this round of cross-validation
    mean_accuracy = np.mean(accuracy_values)
    mean_accuracy_values.append(mean_accuracy)

  

# Plot the distribution of mean accuracy values
plt.hist(mean_accuracy_values, bins=10, edgecolor='k', alpha=0.7)
plt.title('Distribution of Mean Accuracy Values')
plt.xlabel('Mean Accuracy')
plt.ylabel('Frequency')
plt.show()
```


![[output.png|350]]

