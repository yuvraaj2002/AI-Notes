This page is dedicated towards understanding the concept of Partition based clustering and all the notes are mentioned below and I will also be adding the links to the resources that I have been using to understand this topic.

##### What do you mean by partition based clustering and what are the algorithms which uses this approach ? 

Partition or centroid based clustering is a clustering technique where we assign the clusters to data points based on their similarity/[proximity](https://www.google.com/search?q=What+is+the+meaning+of+proximity+&sxsrf=APwXEdeNBt1hTEiKqoPrkWmzX3lZFFma6A%3A1684144359781&ei=5wBiZPSdL5Pn4-EPxPWP0Ak&ved=0ahUKEwi0rcLShvf-AhWT8zgGHcT6A5oQ4dUDCA8&uact=5&oq=What+is+the+meaning+of+proximity+&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIICAAQFhAeEA86CggAEEcQ1gQQsANKBAhBGABQ1mtYpm5gpHFoA3ABeACAAZgBiAGaApIBAzAuMpgBAKABAcgBCMABAQ&sclient=gws-wiz-serp) to centroid representing the cluster. The algorithms which use Partition based clustering approach are 

1. K-Means algorithm
2. K-Means++ algorithm
3. Fuzzy C means algorithm


##### Explain the working of KMeans algorithm ? 

1. First of all it initialize k centroid in the data points.
2. After that it calculates the Euclidian distance of every data points from each centroid and the data point which is closest to any of the centroid is assigned to that centroid
3. The same process is repeated until all the data point are assigned to some cluster and after that the centroids are adjusted by calculating the mean of data points within that cluster to get the new centroid for that cluster and the point to be noted is that the centroid of a cluster does not need to be an actual data point from the dataset. 
4. This same process of calculating the Euclidian distance and assigning centroid gets repeated until position of new centroid ≠ old centroid.

##### What is the meaning of K in KMeans and how to chose its value ? 

K is basically an hyper-parameter and it is used to define into how many clusters we want to divide our data. We can find the value of this K by using elbow method or Silhouette Score method which is also a metric for [[Evaluation of Clusters]].

##### Explain elbow method along with its drawback ? 

Elbow method is a technique which is used to find the value of k in the K-Means algorithm. The way this algorithm works is that for every value of K starting from generally from 2, we calculate the Inertia corresponding to that value of K. Inertia → Within cluster sum of squared error.

> To better understand this let us assume first of all we are choosing K =1 now for this we will calculate $Σ (Centroid - datapt)^2$. In similar way for K =2 we will calculate WSCC for both the cluster and then we will add both $Wscc = Wscc_1 + Wscc_2$

After that we simply plot the graph between the value of k and its corresponding value of inertia on the Y axis and look for the elbow point on the elbow curve, where elbow point is the point where the slope becomes somewhat flat. There are also 2 drawbacks associated with this method

1. It is not very much precise method
2. The interpretation from the graph between Inertia and Number of cluster is totally subjective and may vary from person to person.

##### Explain silhouette Score method 

Silhouette method is a more optimized technique that we can use for finding the value of k. Basically in this technique we simply plot a graph between Silhouette score and the value of K, where silhouette score is simply a numerical value representing Quality of a cluster. Silhouette score considers both the intra cluster distance (Cohesion) and Intercluster distance (Separation).

To get a good quality cluster the Separation (Inter cluster) distance needs to be maximized and the Cohesion (Intra cluster distance) needs to be minimized.

![[Pasted image 20240714143504.png]]

##### What is the Range of the Silhouette Score method

 - A score close to +1 indicates that the data point is well-clustered, with a high cohesion and good separation from neighboring clusters.
- A score close to 0 indicates that the data point lies near the boundary between clusters.
- A score close to -1 indicates that the data point may have been assigned to the wrong cluster.

##### What are the drawbacks of using KMeans ? 

1. It is sensitive to initialization of centroids
2. We need to be aware about value of K prior implementing the algorithm to form cluster, thus extra computation is needed to first get the right value of K
3. It gives us good results only if internally the clusters are spherical in nature.

##### Talk about the problem of initialization of KMeans and  how its solved ? 

Major drawback of traditional K means clustering algorithm is the sensitivity to the initialization of K centroids and the thing is that if the initially all the centroids will be present closer to each other then we might get suboptimal results or it would take longer to converge to the global minima. So in order to solve this problem we use a advance version of this algorithm which we call as KMeans++ algorithm.
  



##### Code to find value of K using elbow and silhouette Score method

``` python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Loading the data
df = sns.load_dataset('iris')

# We will remove species (Target variable) and we will only consider first 3 features
df = df.iloc[:,:4]
df.head(5)

# Empty list to store inertia
silhouette_sc = []
inertia = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i,random_state=0,n_init=10,init='k-means++')
    kmeans.fit(df)
    inertia.append(kmeans.inertia_)
    
fig,ax = plt.subplots(figsize=(5,3))

plt.plot(range(1, 11), inertia)
plt.title('Elbow Graph')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()


# Empty list to score silhouette score
silhouette_sc = []
for i in range(2,11):
    kmeans = KMeans(n_clusters = i,random_state=0,n_init=10,init='k-means++')
    kmeans.fit(df)
    labels = kmeans.predict(df)
    silhouette_avg = silhouette_score(df, labels)
    silhouette_sc.append(silhouette_avg)
    
fig,ax = plt.subplots(figsize=(5,3))

plt.plot(range(2, 11), silhouette_sc)
plt.title('Silhouette graph')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

# Let's create an object of KMeans class
kmeans = KMeans(n_clusters =2 ,random_state=0,n_init=10,init='k-means++')
kmeans.fit(df)

# Making predictions
clusters = kmeans.predict(df)
```