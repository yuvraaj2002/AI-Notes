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

![[Pasted image 20240714163843.png]]


### [Explain the working of DIANA ?](#)

![[Pasted image 20240714165027.png]]



### [What is the stopping criterion for AGNES and DIANA ?](#) 

- AGNES
	- Until we don't get a big parent cluster keep on merging the clusters based on their similarity 
	- Until we haven't reached the specified number of clusters
- DIANA
	- Until we don't get individual data points keep on fragmenting the clusters
	- Until we haven't reached the specified number of clusters



- What are the types of linkages used in agglomerative clustering?
    
    There are 3 types of agglomerative clustering ⬇️
    
    1. _**Single linkage**_ : In this during the updation of the distance matrix we only consider minimum distance between all possible pairs of data points from clusters
    2. _**Average linkage**_: In this during the updation of distance matrix we take the average distance of all possible pair of points from the clusters
    3. _**Complete linkage**_ : In this during the updation of distance matrix we only consider the maximum distance out of all possible pair of data points from the clusters.
- Explain agglomerative hierarchical clustering
    
    ### Basic idea 💡
    
    Agglomerative hierarchical clustering uses a bottom up clustering approach, where initially all the data points are considered to be clusters and after that recursively similar clusters are merged to create a big cluster, this process is repeated until we get one big cluster or up-to a point defined by stopping criterion.
    
    ### Algorithm 👨🏾‍💻
    
    1. Create a distance matrix of n*n size where n→ Number of data points
    2. Select most similar(closest) pair of clusters and merge them
    3. Update the distance matrix based on the type of agglomerative clustering
    4. Repeat steps 2 and 3 until we get one big cluster or until stopping criterion is not reached
    
    ### Example
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/835648c2-8c9d-4d6e-9e3d-29811c262637/Untitled.jpeg)
    
    [Euclidean Distance Calculator](https://www.omnicalculator.com/math/euclidean-distance)
    
- Stopping criterion
    
    The stopping criterion for agglomerative hierarchical clustering can be determined based on either the number of clusters or a threshold distance/similarity.
    
    1. Number of Clusters: One common stopping criterion is to specify the desired number of clusters to be formed. The algorithm stops when the number of clusters reaches the specified value. This approach is useful when we have prior knowledge about the number of clusters in the dataset.
    2. Threshold Distance/Similarity: Another stopping criterion is to specify a threshold distance or similarity value, below which clusters will not be merged. This approach is useful when we do not have prior knowledge about the number of clusters in the dataset. The algorithm continues to merge clusters until the distance or similarity between them exceeds the specified threshold.
- Talk about CURE and Chameleon
    
    - CURE
        
        CURE stands for clustering using representatives and it is specifically designed to handle **large datasets with non-spherical and unevenly sized clusters**. It overcomes the limitations of centroid-based algorithms like K-means, which can struggle with these types of cluster shapes.
        
        ### Key features
        
        - **Representative Points:** Instead of relying on a single centroid per cluster, CURE uses a set of representative points to capture the diversity and extent of each cluster.
        - **Shrinking and Merging:** Representative points are iteratively shrunk towards the cluster center and merged based on their proximity, progressively refining the cluster representation.
        
        ### Working
        
        1. **Initial Partitioning:** CURE starts by performing a single-link hierarchical clustering on the data, forming initial hierarchy of clusters.
        2. **Representative Selection:** Within each cluster, a fixed number of well-scattered points are chosen as representative points.
        3. **Shrinking and Merging:** Representative points are shrunk towards the cluster center by a pre-defined factor, effectively pulling them closer to the core of the cluster.
    - Chameleon