Tags : [[Unsupervised Learning]]

- [Introduction about the ]

```
int find_value(vector<int> values,int count,int k)
{
	// Marking function call for the next value
	find_value(values,count+1,)
	return -1;
}
```


##### If we already had the partition and hierarchical clustering then why do we even density based clustering ? 

In order to truly understand that why we are even using the density based clustering we need to be aware about what were the drawbacks of using the KMeans and hierarchy based clustering

1. In case of KMeans clustering it makes an assumption that all the clusters are spherical in nature and are of same size so in order to get a good cluster cluster we need to be aware about how many number of clusters we need to form i.e. some extra computation is needed before implementing this algorithm.
2. Hierarchical clustering do not have any such kind of assumptions about the data but it is also a drawback that this algorithm is very computationally expensive.

##### What is the core idea behind the density based clustering and what are the algorithms used for this ? 

Density-based clustering is a type of clustering that focuses on identifying regions of high density and low density. Regions with a density above a specified threshold are considered clusters, while regions with a density below this threshold are considered noise or outliers. The algorithms used for this are 

- DBSCAN
- OPTICS

##### Is DBSCAN parametric or non parametric algorithm ? 

DBSCAN algorithm do not make any kind of assumption about the underlying data with which it will deal with and because of that this algorithm is called non parametric in nature whereas if we will talk about Kmeans algorithm it makes an assumption that the clusters are spherical in nature and thus it is called parametric.

##### What are the various hyper parameters associated with DBSCAN ? 

In DBSCAN there are basically 2 hyper parameters which are associated and help us to identify the  core point, border point and noise point. 

1. Epsilon : This is used to specify the radius of the data point 
2. Min point : This is used to specify the minimum number of data points that must exist within the epsilon of the data point to consider it as the core point.



##### What is the concept of density reachability and why it is used ?

Density reachability is the concept used in density based clustering and this concept is actually used to identify if there exist a connection between core point and non core point.

Basically if a data point is not a core point ,then the algorithm checks if that point can be reached through some sequence of core points or not. If such a sequence exists, the point is considered density-reachable from a core point and is classified as a border point. On the other hand, if there doesn't exist such a sequence which connect the core point with non core point then, we say the point is not density-reachable and is typically classified as a noise point. 


##### What is the difference between core point, border point and noise point

There are 2 concepts which the algorithm used to identify a data point to be core, border or noise point and these are 

1. Using the hyper parameter (Epsilon and MinPts)
2. Using density reachability

- Core point: A point is considered to be core point if it contains atleast MinPts data points with the epsilon.
- Border point : A point which is not a core point but is density reachable from the core point is called Border point. Other that this we can also say it is like if the data point do have the minPts within the Epsilon then we call it border point because it will be density reachable from the core point.
- Noise point: A non core point which is not density reachable from the core point is called noise point

##### Explain the working of the DBSCAN ? 

##### Talk about the affect of hyper parameters on the algorithm performance

When we talk about the hyper parameters then we mostly talk about the epsilon and the MinPts and both have their own affect on the clustering let us understand both of these

1. Increase in value of Epsilon: With the increase in the value of epsilon the number of core points and the border points would increase and it simply means that we will get clusters of large size, now the drawback of this is that there is a possibility that the smaller clusters get merged into larger clusters.
2. Decrease in value of Epsilon : With the decrease in the value of epsilon the number of core points and the border points would decrease and because of that the number of high density clusters will decrease because of which we will experience more noise in the data.

1. With the increase in MinPts the ideally the number of core and border points should increase and due to this increase the overall area of dense region should also increase. This actually leads to formation of large clusters and the number of noise points decrease.
2. With the decrease in MinPts the ideally the number of core and border points should also decrease and due to this decrease the overall area of dense region should also decrease. This actually leads to formation of small clusters. But choosing a small value of MinPts could also lead to extra fragmentation of cluster which actually might not be useful.

##### How to find the correct value of Epsilon and MinPts ?


- Understanding OPTICS
    
    # **Introducing OPTICS: an Extension of DBSCAN**
    
    The inability to detect clusters of varying density represents a significant limitation of DBSCAN. This disadvantage stems from the fact that DBSCAN uses one constant distance value (ε) together with one density threshold (_minPoints_) to determine whether a point is in a dense neighborhood. In this way, the DBSCAN algorithm actually assumes that the densities of different clusters are equal. However, many real-world datasets share the common property that their internal cluster structure cannot be characterized by global density parameters.
    
    It did not take long for influential scientists to identify this deficiency and propose a suitable solution. In 1999, three years after the DBSCAN algorithm was published, some of its authors developed OPTICS as a particular form of DBSCAN extension. [2] The main difference between DBSCAN and OPTICS is that OPTICS generates a hierarchical clustering result for a variable neighborhood radius.
    
    # **Understanding OPTICS**
    
    OPTICS (‘Ordering Points To Identify Clustering Structure’) is an augmented ordering algorithm which means that instead of assigning cluster memberships, it stores the order in which the points are processed. OPTICS requires the same ε and _minPoints_ hyperparameters as DBSCAN, but with one important difference – the ε parameter is theoretically unnecessary. Explicitly setting the value of this parameter is only used for the practical purpose of reducing the algorithm’s runtime complexity. In the following examples, we will assume that the epsilon parameter is set to a very large value (i.e. ), as this is the case in many implementations of the OPTICS algorithm.
    
    In addition to the concepts mentioned above of the DBSCAN algorithm, OPTICS introduces two more terms, namely:
    
    - **Core distance** – the minimum distance required for a data point _p_ to be considered as a core point. If the _p_ is not a core point, then its core distance is undefined.
    - **Reachability distance** – the reachability distance of point _q_ with respect to another point _p_ is the smallest distance such that _q_ is directly reachable from _p_ if _p_ is a core point. This distance cannot be smaller than the core distance of point _p_, since for smaller distances there are no points that are directly reachable from point _p_. If _p_ is not a core point, then the reachability distance of point _q_ with respect to point _p_ is undefined.


