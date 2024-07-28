This page is dedicated towards understanding the concept of PCA algorithm in machine learning and all the resources that I will be using for understanding be linked below

- [CampusX PCA](https://www.youtube.com/watch?v=iRbsBi5W0-c&pp=ygUXUENBIGluIG1hY2hpbmUgbGVhcm5pbmc%3D)
- [Krish Naik Video](https://www.youtube.com/watch?v=H99JRtDDnvk&pp=ygUXUENBIGluIG1hY2hpbmUgbGVhcm5pbmc%3D)

Before actually moving on to understanding that how this algorithm works we need to be aware about the fact that why we even need this algorithm at the first place and for that we need to be aware about the problem which we face with high dimensional data called, "Curse of dimensionality"

### What do you mean by Curse of dimensionality and what are the ways to deal with it ? 

Curse of dimensionality is basically a problem where after an optimal number of input features or dimensionality of input data the performance of machine learning algorithms starts degrading and the reason is with the increase in dimensionality the model becomes more complex and tends to overfit, similarly for the distance based algorithms such as KNN, the performance of distance metrics gets affected because in higher dimensions the data points tends to converge.

There are only 2 ways using which we can actually deal with the issue of curse of dimensionality and these are 

1. Selecting the subset of most important features (Feature selection)
2. Creating new features from existing features ( Feature extraction )

### What do you mean by PCA and give short summary of how it works 

PCA stands for principal component analysis and it is an unsupervised machine learning technique which is used for doing the feature extraction or dimensionality reduction. The working of the PCA can be explained in couple of steps :

1. First of all the PCA takes the original feature space and transform it into new feature space, where in that new transformed feature space, the features will be called principal components
2. After that the PCA analyze the spread of data across each of the principal components and orders the principal components by the spread.
3. Finally based on how much dimensionality reduction we want, the subset of principal components are selected.


### What are the fundamental concepts about which we need to be aware about for understanding the working of PCA ? 

- Variance
- Covariance
- Matrix as linear transformation
- Vector projection
- Eigen values and vectors


### Why do we try to maximize the spread of the data across the principal component and which measure do we use for finding out the spread of data ? 

By maximizing the spread of data across principal components we try to make sure that maximum amount of information could be retained even after doing the dimensionality reduction and for measuring the spread we use variance.

### Why we don't use MAD over variance in PCA ? 

To measure spread we use variance where `spread is not equal to variance` instead the variance is proportional to spread and we chose variance over Mean absolute deviation (that is actually equivalent to spread) because MAD is not differentiable thus we will not be able to use any kind of optimization algorithm on top of it.

