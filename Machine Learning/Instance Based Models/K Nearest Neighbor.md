This page is dedicated towards understanding both the KNN classifier and regressor and the main resources used for this topic are mentioned below.

- [KNN Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
- [KNN Regressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html)

### [What do you mean by KNN algorithm and talk about its types](#)

KNN is simply a short form for the K nearest neighbor and it is a distance based supervised machine learning algorithm that can be used to solve both classification and regression problem. There are 2 different variants of KNN algorithm ( KNN classifier and KNN regressor ). The internal working of both these algorithms is same like the initialization of K and finding the K nearest neighbors but the only difference is that

 - KNN classification_ predicts the class label based on the _majority count_ of the K nearest neighbors.
 - _KNN regression_ predicts the continuous value by taking the _mean (or weighted mean) of the target values_ of the K nearest neighbors.

### [Why KNN is called lazy learner ?](#)

KNN algorithm is called lazy learner because during the training phase this algorithm do not learn anything from the data and it only memorizes the data, whereas during the prediction phase itself it makes the prediction using the training data.

Whereas on the other hand other algorithms like logistic regression, SVM or decision tree algorithm learn the model parameter during the training phase and then use those model parameter values to make a prediction during prediction phase.

### [Is KNN parametric or Non parametric ?](#) 

KNN algorithm is called non parametric because it do not make any assumption regarding the distribution of data with which it will deal with and because of this it can easily be used with both linear and non linear data. Not only this since the number of parameters do not increase with the increase in number of data points so this is also the sign that the this algorithm is non parametric in nature.


### [How do we find the value of K, and why to consider odd value for classification](#)

K in KNN algorithm is simply a hyper-parameter which is used to specify how many nearest neighbors do we want to consider for making prediction.

1. Rule of Thumb: A commonly used rule of thumb is to set K as the square root of the total number of data points in the training set. This provides a good starting point and can be refined using other techniques mentioned above.
2. Using [[Cross Validation]]

### [What are the applications of KNN](#)

The various application of KNN algorithm are ⬇️

1. Outlier or anomaly detection
2. Recommendation systems
3. For multivariate imputation of missing values


### [What are all the hyper parameters associated with KNN](#)

-  Value of K
- Distance metric : Euclidian, Manhattan , Minowski
- Weights : Uniform, Weighted ( Inverse relation with the distance)
- Search Algorithm: Linear Search, KD tree, Ball Tree

### [Talk about bias variance tradeoff in KNN](#)

- With the smaller value of K the model will face the issue of overfitting which means low bias and high variance. It can be thought like the model listens to very minute details rather than looking at big picture.
- With larger value of K the model will suffer from underfitting which means high bias and low variance. It can be thought like the model listens to everything

### [What are the various optimization that can be done in KNN ?](#) 

- Scaling the features values [[Feature Scaling]]
- Removing the Outliers
- Using Space partitioning data structures such as KD tree and Ball tree to improve the search speed


### [Explain KD tree and Ball tree in KNN](#)

Both the KD tree and Ball tree are space partitioning data structures which divides the feature space in such a way that we don't need to go over the entire dataset to find the K nearest neighbors and improve the time complexity from $O(n)$ to $O(log(n))$

1. KD tree stands for K dimensional trees and here we divide the feature space into hyper cubes by creating a cut using the planes/hyperplane along the feature using the median. After doing so once the query point falls into one of the hyper cube, we then look for K nearest neighbors in that hyper cube only.

	![[KD Tree.png|200]]
2.  Ball Tree is another space-partitioning which create subspaces by using the hyperspheres, it basically creates a hierarchical structure of hyper spheres.

	![[Ball Tree.png|300]]

### [Explain the distance metrics used ?](#) 

- Euclidian distance : Helps us to find the straight line distance between 2 points and useful when data is numerical
- Manhattan distance : It is used when we cannot simply find the straight line distance between 2 points and for the distance calculation in term of mathematics we use the base and height. Also called taxi cab distance
- Minowski distance : Minkowski distance **incorporates** the components of both Euclidean and Manhattan distances

### [Talk about how curse of dimensionality affects KNN](#)

Curse of dimensionality is a phenomenon according to which after an optimal number of dimension of input data the performance of certain machine learning algorithms start degrading. Out of these algorithms KNN is also one of the major algorithm which suffers from this problem as the computation of KNN algorithm increases with increase in dimensions of data.

- In high-dimensional spaces, the distances between data points become less discriminative and most points tend to be at similar distances from each other, reducing the effectiveness of distance-based algorithms like KNN.
- The ratio of the distance to the nearest neighbor and the distance to the farthest neighbor approaches 1, making it hard to distinguish between near and far neighbors.

