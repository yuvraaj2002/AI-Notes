This page is dedicated towards understanding the concept of hierarchical clustering in AI and the resources used for this topic are the course videos of CampusX. But the other resources which I will be using I will add them here in the future.

### [If we have K-Means clustering then what is the need of hierarchical clustering algorithm?](#)

There are 2 main concerns associated with KMeans clustering algorithm because of which can think about considering the hierarchical clustering.

1. KMeans algorithm is very much sensitive to the value of K and in order to use this algorithm we first need to find the value of K thus some extra computation is involved.
2. Also the Kmeans algorithm makes an assumption that the centroids are spherical in nature and are also of the similar size so incase if the assumptions are violated then we will not get good results and generally in the real world the clusters are not spherical in nature.

### [What is the idea behind hierarchical clustering ?](#) 

The core idea behind hierarchical clustering algorithm is that it do not make any assumption about the shape and size of clusters and thus it is very much flexible and create the clusters either 
- By merging the clusters into big cluster based on their similarity or proximity (Bottom up approach)
- By fragmenting the parent cluster into child clusters (Top to bottom approach)

### [What do you mean by dendrogram and what’s the use of it?](#)

Dendrogram is simply a tree like structure which is used to visually represent the hierarchy of clusters formed by clustering algorithm. In dendrogram every node is simply a cluster which is formed by merging other similar clusters.

### [What are the various hierarchical clustering approaches and algorithm](#)

In hierarchical clustering there are 2 main approaches which are being used and that is bottom up or top to bottom approach and for each of the approach we use different algorithm

1. Bottom up (Agglomerative Nesting)
2. Top to Bottom (Divisive Analysis)

### [Explain the working of AGNES and also talk about types of linkage ?](#)

AGNES stands for Agglomerative nesting and it is a bottom to up approach where we initially start with the individual data points considered as clusters and after that we simply merge the clusters based on their proximity or similarity with each other. Now in order to truly understand this let us assume that there are 4 data points.

1. Initially all the data points (4 in this case ) will be considered as individual clusters
2. After that we will build a distance matrix out of it
3. Then we will select the pair which is having smallest distance between them and merge them
4. In order to merge them we can use either of the linkage type 
5. After that we will update the distance matrix and the same process will be repeated until we don't get big final parent cluster or the stopping criterion.

### [Types of Linkage](#)

- Single linkage : The minimum distance between pair of points from 2 clusters, in simple terms out of all the pairs of points from 2 clusters the pair having minimum distance will be used for linking the clusters
- Complete linkage : The maximum distance between pair of points from 2 clusters.
- Average Linkage : The average distance between all the pair of points from 2 clusters.
- Centroid linkage : The centroids are used for linking the clusters

![[Unsupervised Learning/images/Types of Linkage.png]]


### [Explain the working of DIANA ?](#)

![[Unsupervised Learning/images/DIANA Working.png]]



### [What is the stopping criterion for AGNES and DIANA ?](#) 

- AGNES
	- Until we don't get a big parent cluster keep on merging the clusters based on their similarity 
	- Until we haven't reached the specified number of clusters
- DIANA
	- Until we don't get individual data points keep on fragmenting the clusters
	- Until we haven't reached the specified number of clusters

Other than this we can also consider the `Silhouette Score` as the main guiding force for understanding what should be appropriate number of clusters.