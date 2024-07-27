This page is actually dedicated towards understanding the concept of random forest in machine learning. The main resource used for this topic are the course videos of CampusX. 

- [Session 1 (Introduction to Random Forest](https://drive.google.com/file/d/1EK3u-hyEiK0wMMsy07fI0Dn-jwOicbEU/view)
- [Session 2 (Hyper parameters of Random forest, OOB score and ERT)](https://drive.google.com/file/d/1sV_PG8PNCzXNvN73cvSxw3NDiwh1Y7bc/view)

Now we will take a look at all the possible interview questions which can come in the interview also we will take a look at the practical code of random forest classifier and regressor.

##### What do you mean by random forest ? 

Random forest is an machine learning technique where we create an ensemble of decision tree by using the bagging architecture from [[Ensemble Learning]] and due to this collection of decision tree we call this as forest, whereas the random comes from the fact that rather than using all the features at a particular node, random subset of features are used for splitting.

This randomness helps us to create de-correlated trees. By default, it samples $√n$ features (where n is the total number of features)

![[Pasted image 20240703123151.png|450]]

##### What is the difference between bagging and random forest ? 

1. In case of bagging we can use any machine learning algorithms as the base models but we need to make sure all the base models are of same type, whereas in case of Random forest all the base models needs to be decision trees only.
2. In bagging there is actually tree level row sampling which is being done, whereas random forest goes one level beyond and other than doing tree level row sampling it also do node level column sampling.

##### Why do we use the forest rather than using the Single tree and why random forest is actually robust to outliers ? 

Forest is always preferred over the decision tree because it is easy to attain low bias and low variance configuration which helps to deal with the problem of overfitting. Single tree means single decision tree and by default due to their stopping criterion decision tree is a low bias and high variance model, which means that with the small change in the data we will observer high variability in terms of model performance.

Now in case of random forest due to tree level row sampling and node level column sampling there is a lot of randomness involved and in all the variance of the complete system decreases, Also it is very much intuitive as let say we have the new data and if we will use this new data with single decision tree then we will observe high variance whereas if we will use this new data with random forest then due to bootstrap sampling and node level column sampling, the effect of new data on individual tree will be reduced leading to decrease in variance.

##### How random forest can be used as feature selection technique 

Random forest itself can't calculate the feature importance scores, instead the individual [[Decision Tree]] are used for calculating the feature importance score and we finally just average all the scores to get final feature importance scores.

![[Pasted image 20240719122412.png]]

##### What do you mean by OOB score and OOB error in random forest ? 

In order to truly understand what is OOB score and OOB error we first needs to be aware about what does OOB samples means.

OOB stands for Out of Bag samples, which are basically those samples which remained unutilized due to row level bootstrap sampling and node level column sampling. Now since these samples are unseen thus they are perfect for testing the performance of the algorithm. On average, about 37% remains as the OOB samples.

-  The OOB score is a measure of overall accuracy of the random forest and it is calculated by passing OOB samples to each of the DT, calculating the accuracies and then finally averaging them to get final accuracy. 
- OOB error is basically complement of the OOB score and it is a numerical value which tell use the error which our ensemble model is making on the OOB samples. OOB Error=1−OOB Score

##### What are the various hyper parameters associated with random forest ? 

![[Pasted image 20240702071859.png|550]]

- **n_estimators**: The number of trees in the forest. Increasing the number of trees generally improves performance, but also increases computational cost.
    
- **criterion**: The function to measure the quality of a split. Common options include "gini" (Gini impurity) for classification and "mse" (mean squared error) for regression.
    
- **max_depth**: The maximum depth of each tree. Limiting the depth can help prevent overfitting.
    
- **min_samples_split**: The minimum number of samples required to split an internal node. Higher values can prevent overfitting.
    
- **min_samples_leaf**: The minimum number of samples required to be at a leaf node. Higher values can prevent overfitting and create more generalized models.
    
- **min_weight_fraction_leaf**: The minimum weighted fraction of the sum total of weights (of all the input samples) required to be at a leaf node. It is used for handling unbalanced datasets.
    
- **max_features**: The number of features to consider when looking for the best split. Options include:
    
    - "auto" (default): sqrt(n_features) for classification, n_features for regression.
    - "sqrt": sqrt(n_features).
    - "log2": log2(n_features).
    - An integer value or a float (representing a fraction of the total number of features).
    
- **max_leaf_nodes**: Grow a tree with a maximum number of leaf nodes. If None, then unlimited number of leaf nodes.
    
- **min_impurity_decrease**: A node will be split if this split induces a decrease of the impurity greater than or equal to this value. This can help prevent overfitting.
    
- **bootstrap**: Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree.
    
- **oob_score**: Whether to use out-of-bag samples to estimate the generalization accuracy. Useful for evaluating model performance.
    
- **n_jobs**: The number of jobs to run in parallel for both fit and predict. -1 means using all processors.
    
- **random_state**: Controls the randomness of the bootstrapping of the samples and the sampling of the features. Provides reproducibility.
    
- **verbose**: Controls the verbosity when fitting and predicting.
    
- **warm_start**: When set to True, reuse the solution of the previous call to fit and add more estimators to the ensemble. Useful for large datasets where training can be done incrementally.
    
- **class_weight**: Weights associated with classes in the form {class_label: weight}. Useful for handling unbalanced datasets.
    
- **ccp_alpha**: Complexity parameter used for Minimal Cost-Complexity Pruning. The subtree with the largest cost complexity that is less than ccp_alpha will be chosen.
    
- **max_samples**: If bootstrap is True, this parameter controls the number of samples to draw from X to train each base estimator. If None (default), then draw X.shape[0] samples.


##### What do you mean by Extra trees ? 

Extra trees which are also called extremely randomized tree are is a modification of the Random
Forest algorithm that changes the way the splitting points are chosen. In case of traditional decision tree all the features the optimal split point is calculated and the point which gives us maximum reduction in impurity is chosen, but the thing is this process of finding the optimal split point is computationally expensive.

So in case of extra randomized tree for the features under consideration a split point is chosen completely at random and the best performing split point is chosen, this actually adds more layer of randomness and create more decorrelated trees.
 
Because of this difference, Extra Trees tend to have more branches (be deeper) than Random
Forests, and the splits are made more arbitrarily. This can sometimes lead to models that
perform better, especially on tasks where the data may not have clear optimal split points.
However, like all models, whether Extra Trees will outperform Random Forests (or any other
algorithm) depends on the specific dataset and task.