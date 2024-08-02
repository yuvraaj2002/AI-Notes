
This page is dedicated to everything related to the decision tree algorithm. In this notion page we will talk about what is decision tree, its working along with the code explanation.💫

- [Decision tree classifier](https://drive.google.com/file/d/1EaPkxw5I0KstZARjQMq_J8yOQYt82Hb0/view)
- [Decision tree regressor](https://drive.google.com/file/d/1yzsKHIMMeOztAK1Jcg5dy9OvVAJjMMun/view)
- [Pruning](https://drive.google.com/file/d/1yU-tkH1KMGu7pXHsHmPz5I94NNw7W2wj/view)
- [Gini Impurity | Splitting Decision Tress with Gini Impurity](https://www.analyticsvidhya.com/blog/2021/03/how-to-select-best-split-in-decision-trees-gini-impurity/)



### [What do you mean by decision tree and tell whether it is white or black box model?](#)

Decision tree is an supervised machine learning algorithm which can be used to solve both classification and regression problems, from the big picture we can simply consider the decision tree to be a giant nested if else condition which visually seems to be a tree.

Talking about the black box and white box, the decision tree is pure white box model and is one of the algorithm which is best for the inference because it gives us the exact justification of why we got a particular output corresponding to a query point.

### [Whether decision tree is parametric or non parametric ? ](#)

Decision tree is non parametric in nature because it do not make any kind of assumption about the underlying data with which it will work with, not only this since the parameters of the algorithm increases with the increase in data so that is also the indication that the algorithm is non parametric in nature.

In the context of a decision tree, the model parameters are the components that define the structure and since with the increase in the data the structure generally varies so that's why we call decision tree to be non parametric

### [What are the various algorithms used for decision tree and tell the difference between them?](#) 

There are basically 3 different algorithms which we can use in order to build the decision tree and these 3 algorithms are 

1. CART
2. ID3 ( Iterative dichotomizer 3)
3. C4.5

The basic difference between these algorithms is that the CART algorithm creates a binary tree ( which means every node have atmost 2 child nodes only), whereas ID3 and C4.5 algorithm can create tree where the nodes can have 2 or more than 2 child nodes as well.

Other than this the difference lies in the splitting criteria being used, such as CART algorithm uses the Gini Impurity, ID3 uses the Information gain (with entropy) and C4.5 uses the Gain ratio.

### [Explain working of decision tree for classification ?](#) 

In scikit learn the Decision tree classifier uses the CART algorithm for creating the decision tree and this algorithm creates a binary tree by using the Gini impurity as the splitting criteria. The way this algorithm works is that for the given dataset it simply find the attribute which will give us highest quality of split ( that means it will lead to more pure dataset) and for finding such an attribute the CART algorithms uses the gini impurity.

Mathematically it is given as $G_i = 1− ∑ p_i ^2$, where $p_i$ represents the ratio of class instances among the total instances in the dataset. Also once we calculate the Gini impurity for the left and right child node we simply calculate the weighed sum of the gini impurities. 

$$G_{Total} = Points_{Left}/Points_{Total} * G_{Left} + Points_{Right}/Points_{Total} * G_{Right}$$

- Also note that the feature having More than 2 categories we use the One vs rest approach for calculating the overall gini impurity (Like this category data and remaining category data).
 
![[Gini Calculation MC.png]]

- For the category with numerical values we sort them first and then calculate the mean between every consecutive 2 values and use that mean value as the split point.

![[Gini Calculation Numerical.png]]


### [Out of Gini Impurity and Entropy which one should we use, also talk about the ranges](#) 

The choice between using the Gini Impurity $G_i = 1− ∑ p_i ^2$ and the Entropy $E_i = -P_i*Log_2(P_i)$ is completely based on the size and the complexity of the dataset.

Entropy is computationally more expansive than the Gini Impurity so it recommended to use
- Entropy for smaller and simpler datasets
- Gini for large and complex datasets.

- Range of Gini Impurity is from 0 to 0.5
- Range of Entropy is different based on number of classes
	- For binary classes it is from 0 to 1
	- For multiple classes it is from 0 to $Log_2(n)$



### [How does decision tree works for the regression problems](#)

In case of regression the work flow is almost same the only difference is that rather than using the Gini impurity as attribute selection criteria we focus on Variance and select that attribute-value for splitting which maximize the minimization of the variance in the dataset.

![[CART Regression.png]]

Here is the sample example of how to solve the problem for the feature having more than 2 categories and also for the feature with numerical values.

![[CART Regression OVR.png|400]]


### [Why are decision tree so prone to overfitting ?](#) 

Both the decision tree classifier and regressor are extremely prone to overfitting because of their default stopping criteria's,

- For the classification the default stopping criteria is to split until the dataset is not completely pure (that means until all data points don't belong to single class)
- For the regression the default stopping criteria is to split until the variance is not 0 

![[Pasted image 20240718173559.png]]

![[Pasted image 20240717052435.png]]

### [Talk about all the ways using which we can deal with the overfitting](#)

The only way we can actually deal with the problem of overfitting is to actually use [[Regularization]] and in the context of decision tree regularization is done via Pruning, where 

Pruning is simply a technique where we remove the extra nodes from the decision tree to decrease its predictive power leading neutralizing its low bias and high variance nature towards low bias and low variance nature. But in order to 2 pruning itself we have 2 different 

- Pre Pruning : Pre pruning is like the early stopping where we control the decision tree from growing by using the hyper parameters such as max_depth, min_samples, Minimum_impurity_decrease etc.
- Post Pruning : Post pruning is relatively more complex approach for dealing with overfitting and in this approach we don't put any kind of restriction on the growth of the decision tree and instead allows the tree to first grow to its complete depth and then remove the nodes from the tree which do not provide much predictive power.\

By doing pre pruning we suffer from short sightedness which means we miss the scenario where in future some split could be far better than all the splits done so for minimizing the impurity or variance and drawback of post pruning is that it is computationally expensive

```python
from sklearn.datasets import make_regression

# Generate a dummy dataset
X_dummy, y_dummy = make_regression(n_samples=100, n_features=2, noise=0.1, random_state=42)

# Function to visualize the effect of post-pruning using cost complexity pruning
def visualize_postpruning_effect(ccp_alpha_values):
    plt.figure(figsize=(20, 15))
    for i, ccp_alpha in enumerate(ccp_alpha_values):
        reg = DecisionTreeRegressor(ccp_alpha=ccp_alpha)
        reg.fit(X_dummy, y_dummy)
        plt.subplot(3, 3, i + 1)
        tree.plot_tree(reg, feature_names=['Feature1', 'Feature2'], filled=True)
        plt.title(f'ccp_alpha = {ccp_alpha}')
    plt.tight_layout()
    plt.show()

# List of ccp_alpha values to explore for post-pruning
ccp_alpha_values = [0.0,1,1.5]
visualize_postpruning_effect(ccp_alpha_values)
```

![[Pasted image 20240703160516.png]]


### [What are the various hyper parameters of the decision tree](#)

- `Maximum depth`: Used to define the maximum depth of the tree. Small value leads to underfitting and large value leads to overfitting
- `Min_samples`: Used to define the minimum number of samples that needs to be considered for doing splitting. Small value : Overfitting and large value : Underfitting
- `Min_samples_leaf`: Used to define minimum number of samples which must exist in the leaf node after splitting
- `Minimum_impurity_decrease`: Used to define the minimum impurity decrease which must be there after doing splitting. _**Impurity_parent + Weighted sum of (child impurities) > threshold**_
- `Maximum features and Maximum leafs`: Used to define the maximum number features to be considered and also the maximum number of leaf nodes that must be formed. For maximum features we can use sqrt(features) or log_2(features)


##### Talk about sensitivity to axis orientation

##### Talk about the time complexity 

##### Using decision tree to calculate the feature importance
[[Feature Selection]]
```python
# Function to calculate and plot feature importances
def plot_feature_importances(model, feature_names):
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
    plt.figure(figsize=(15, 10))
    plt.title("Feature importances")
    plt.bar(range(len(importances)), importances[indices], align="center")
    plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=90)
    plt.xlim([-1, len(importances)])
    plt.show()

  
# Generate a dummy dataset with many features
X_dummy, y_dummy = make_regression(n_samples=100, n_features=10, noise=0.1, random_state=42)

# Train a decision tree regressor
reg = DecisionTreeRegressor()
reg.fit(X_dummy, y_dummy)

# Plot feature importances
plot_feature_importances(reg, [f'Feature{i+1}' for i in range(X_dummy.shape[1])])
```
