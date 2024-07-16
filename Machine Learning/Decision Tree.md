
This page is dedicated to everything related to the decision tree algorithm. In this notion page we will talk about what is decision tree, its working along with the code explanation.💫

- [Decision tree classifier](https://drive.google.com/file/d/1EaPkxw5I0KstZARjQMq_J8yOQYt82Hb0/view)
- [Decision tree regressor](https://drive.google.com/file/d/1yzsKHIMMeOztAK1Jcg5dy9OvVAJjMMun/view)
- [Pruning](https://drive.google.com/file/d/1yU-tkH1KMGu7pXHsHmPz5I94NNw7W2wj/view)
    

![[Pasted image 20240717052435.png]]

![[Pasted image 20240717052527.png]]


![[Pasted image 20240717052553.png]]
### Introduction and Prerequisite

- What do you mean by decision tree algorithm ?
    
    Decision tree is basically a supervised machine learning algorithm that can be used to solve  both classification and regression problems. In simple terms it can be defined as a giant nested if else conditions and visually it seems to be like a tree like data structure with nodes representing the decision making
    
    ![[Pasted image 20240703151853.png|500]]

- Is decision tree white box or black box model ?
    
    Decision tree is white box model because the output which we recieved can easily be interpreted and understood.

- Is decision tree parametric or non parametric algorithm ?
    
    It do not make any assumption about the underlying relationship of the data because of which it can be used with both the linear and non linear data.
    
    <aside> 💡 **Example**: LR algorithm makes assumption about the linearity of the data due to which it is called parametric algorithm.
    
    </aside>

- What are the various algorithms that can be used to create decision tree
    
    In order to form the decision tree there are multiple algorithms which can be used but one of  the most common one is CART which stands for Classification and regression trees, but other ones are ID3 or C4.5

- What is the basic difference between the algorithms used for creating decision tree ?

	### Cart algorithm
	- It can be used to solve both classification and regression problems
	- By using this algorithm any node have at most 2 child nodes only.
	- It uses the Gini impurity (classification) / Variance reduction (regression)
	
	### ID3 or C4.5
	 - Both are used to solve only classification  problems
	- By using this algorithm any node have more than 2 child nodes .
	- ID3 uses Gini Impurity and C4.5 uses the information gain.

- How decision tree decides which feature to use for doing splitting (Attribute selection)?
    
    Basically irrespective of the algorithm being used for creating decision tree, every algorithm uses some measure of impurity to find best quality split or we can say for selecting the best feature for doing splitting.
    
    - CART uses gini impurity as measure of impurity
    - ID3 uses the Information gain
    - C4.5 uses Gain Ratio (normalized Information Gain)
    
    The general flow is that we calculate the quality of split for every feature and the feature which gives us highest quality of split we use that feature for splitting the parent dataset into child dataset.
    
    <aside> 🧴 High quality of split means that the purity of child datasets increases than the parent dataset.
    
    </aside>

- What do you mean by entropy and what is the range of entropy?
    
    Entropy is a measure of impurity and it gives us information about the homogeneity of the dataset. To better understand this if we have 10 data points and 9 of them belong to certain class in that case the entropy of such dataset will be less. (Homogeneity if high)
    
    <aside> 🧴 Entropy is one of crucial measure used by CART for doing attribute selection
    
    </aside>
    
    ![p_i proportion of data points belonging to a class](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f2dfc2ad-5aaf-4feb-9d5e-1d0bc8d888e8/Untitled.png)
    
    p_i proportion of data points belonging to a class
    
    ### Range
    
    - For binary class `Min value = 0` and `Maximum value = 1`
    - For multi class `Min value = 0` and `Maximum value = log_2(n)` , n is number of classes

- What do you mean by Gini impurity, other name for it and what is the range?
    
    Similar to that of entropy, Gini impurity/index is also a measure of impurity of the an attribute. Mathematically it is defined as
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6feb00ac-a038-4c49-b2fd-86d50c4cf6aa/Untitled.png)
    
    ### Example to better understand ✏️
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/307baf5d-7d8e-4a48-8c31-d1813bf505bc/Untitled.png)
    
    ### Range of Gini impurity
    
    The Gini impurity ranges between **`0 to 0.5`**
    
    [Gini Impurity | Splitting Decision Tress with Gini Impurity](https://www.analyticsvidhya.com/blog/2021/03/how-to-select-best-split-in-decision-trees-gini-impurity/)

- Out of Gini and Entropy which one to use?
    
    The use measure of impurity is totally on us. Entropy is computationally more expensive than Gini impurity thus normally we use Gini impurity but we can also use entropy.

- What do you mean by information gain and out of entropy and gini impurity which one is being used ? 
    
    In decision trees, information gain refers to the amount of useful information gained by splitting a dataset based on a particular attribute. It is used for attribute selection
    
    Here's how information gain is calculated using entropy:
    
    1. **Entropy (Before Split)**: Calculate the entropy of the target variable (class labels) before making any splits. This represents the uncertainty in the dataset.
    2. **Entropy (After Split)**: Calculate the entropy of the target variable for each possible outcome of the attribute being considered for splitting. Weighted average of these entropies gives the entropy after the split.
    3. **Information Gain**: The information gain is then calculated as the difference between the entropy before the split and the entropy after the split. It measures the reduction in entropy (or uncertainty) achieved by splitting the dataset on a particular attribute.
    
    Mathematically, the formula for information gain using entropy can be expressed as:
    
    `Information Gain` = `Weight` * `Entropy(Before Split)` − `Weight` * `Entropy(After Split)`

- Dataset for regression and classification
    
    - Classification datasets
        
        |Degree_Type|Field|Average Grade|Job_Outcome|
        |---|---|---|---|
        |Undergraduate|Science|89|Employed|
        |Undergraduate|Arts|92|Unemployed|
        |Postgraduate|Science|95|Employed|
        |PhD|Science|85|Employed|
        |Postgraduate|Arts|98|Unemployed|
        |PhD|Arts|90|Employed|
        |Undergraduate|Science|88|Unemployed|
        |Postgraduate|Arts|93|Employed|
        |Undergraduate|Arts|94|Unemployed|
        |PhD|Science|86|Employed|
        
    - Regression datasets
        
        |Number of Bedrooms|Age of House (years)|Price (in $1000s)|
        |---|---|---|
        |3|10|300|
        |3|15|320|
        |4|10|350|
        |4|20|360|
        |3|30|400|
        |4|10|410|
        |5|5|450|
        |4|25|430|
        |5|20|480|
        |4|15|470|

- Calculations for decision tree classifier and regressor
    
    - Classifier
        
        - Sample dataset and calculation
            
            |Day|Temperature|Humidity|Wind|PlayTennis|
            |---|---|---|---|---|
            |1|Hot|High|Weak|No|
            |2|Hot|High|Strong|No|
            |3|Hot|High|Weak|Yes|
            |4|Mild|High|Weak|Yes|
            |5|Cool|Normal|Weak|Yes|
            |6|Cool|Normal|Strong|No|
            |7|Cool|Normal|Strong|Yes|
            |8|Mild|High|Weak|No|
            |9|Cool|Normal|Weak|Yes|
            |10|Mild|Normal|Weak|Yes|
            |11|Mild|Normal|Strong|Yes|
            |12|Mild|High|Strong|Yes|
            |13|Hot|Normal|Weak|Yes|
            |14|Mild|High|Strong|No|
            
            ![1000008856.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/73b66ff0-1074-4d46-9c21-e4347e506f83/1000008856.jpg)
            
        - Step 1 : Calculating the Gini impurity for all the attributes
            
            - For binary feature feature
                
                ![1000004574.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/1f73cb30-c40e-4a40-bd71-74f707914110/1000004574.jpg)
                
            - For multiple value feature
                
                ![1000004575.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/bc7b608b-81d2-4630-9c59-50df85ad61cd/1000004575.jpg)
                
            - For numerical feature
                
                For numerical feature we firsts sort the values and then create splits and do same thing just like we did for categorical feature.
                
                ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/c7ef1ff5-241e-40f6-b103-fb3d08b3f6dc/Untitled.png)
                
        - Step 2: Select the feature with minimum gini index and perform the split based on that feature
            
        - Step 3: Repeat the same process either upto stopping criterion or upto the point where our dataset is completely pure.
            
        
        <aside> 💡 When a feature has only same value across all samples in the dataset, it doesn't provide any discriminatory power for classification because it doesn't provide any variability to split the data. In such cases, it's common practice to exclude this feature from consideration when building a decision tree or any other machine learning model.
        
        </aside>
        
    - Regressor
        
        ![1000008862.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/f18c412d-2627-4e64-9abf-1bc83d728162/dd420e2a-93cc-436f-8dea-c3188005be95/1000008862.jpg)

- Why decision tree are so much prone to overfitting ?
    
    Decision tree are prone to overfitting because of their by default stopping criterion. Basically in case of classification is to continue doing splitting until the dataset at hand is not complete pure, similarly in case of regression the stopping criterion is to do the splitting until the variance is not 0.
    
    ### Illustration of overfitting in Classification and Regression
    ![[Pasted image 20240703155156.png]]

- How can we deal with the issue of overfitting in decision tree ?
    
    We can use a technique called Pruning to deal with the issue of overfitting.
    
    Basically in pruning as the name suggest we prune/remove the unnecessary nodes from the decision tree with which the model complexity reduces little bit and the problem of overfitting is also reduced.

- What are the different types of pruning ?
    
    There are 2 types of pruning and these are ⬇️
    
    1. Pre-Pruning : Pre-Pruning is also called early stopping because here in this technique instead of growing the decision tree to its complete depth we halts the tree construction in between based on some condition.
    2. Post Pruning : In this type of pruning we first of all grow the tree to its complete depth and then start removing the unnecessary nodes from the tree using Complexity parameter.

- What are the hyper-parameters via which we can do pre-pruning ?
    
    - `Maximum depth`: Used to define the maximum depth of the tree. Small value leads to underfitting and large value leads to overfitting
    - `Min_samples`: Used to define the minimum number of samples that needs to be considered for doing splitting. Small value : Overfitting and large value : Underfitting
    - `Min_samples_leaf`: Used to define minimum number of samples which must exist in the leaf node after splitting
    - `Minimum_impurity_decrease`: Used to define the minimum impurity decrease which must be there after doing splitting. _**Impurity_parent + Weighted sum of (child impurities) > threshold**_
    - `Maximum features and Maximum leafs`: Used to define the maximum number features to be considered and also the maximum number of leaf nodes that must be formed. For maximum features we can use sqrt(features) or log_2(features)

- What is major drawback of using decision trees?
    
    **Prone to Overfitting**: Decision trees are very much prone to overfitting if stopping criterion is not set properly.

- What is the drawback of doing the pre pruning ?
    
    By doing pre pruning we suffer from short sightedness which means we miss the scenario where in future some split could be far better than all the splits done so for minimizing the impurity or variance

- What is the drawback of doing the post pruning ?
    
    It is computationally expensive

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
