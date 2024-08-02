
Clustering metrics are used to evaluate the quality and effectiveness of clustering algorithms. These metrics can be broadly divided into two categories: internal metrics and external metrics.

### Internal Metrics

Internal metrics evaluate the clustering performance based on the intrinsic properties of the data and the resulting clusters. They do not require ground truth labels.

1. **Silhouette Score**:
    
    - Measures how similar a data point is to its own cluster (cohesion) compared to other clusters (separation).
    - The silhouette score ranges from -1 to 1, where a higher score indicates better clustering.
2. **Davies-Bouldin Index**:
    
    - Measures the average similarity ratio of each cluster with the cluster that is most similar to it.
    - Lower values indicate better clustering.
3. **Dunn Index**:
    
    - Ratio of the minimum inter-cluster distance to the maximum intra-cluster distance.
    - Higher values indicate better clustering.
4. **Within-Cluster Sum of Squares (WCSS)**:
    
    - Also known as inertia or SSE (Sum of Squared Errors).
    - Measures the total variance within each cluster. Lower values indicate better clustering.
5. **Calinski-Harabasz Index**:
    
    - Also known as the Variance Ratio Criterion.
    - Measures the ratio of the sum of between-cluster dispersion to the sum of within-cluster dispersion. Higher values indicate better clustering.

### External Metrics

External metrics evaluate the clustering performance based on a ground truth or known labels.

1. **Adjusted Rand Index (ARI)**:
    
    - Measures the similarity between the clustering result and the ground truth, adjusted for chance.
    - Ranges from -1 to 1, where 1 indicates perfect agreement and 0 indicates random clustering.
2. **Normalized Mutual Information (NMI)**:
    
    - Measures the amount of information shared between the clustering result and the ground truth.
    - Ranges from 0 to 1, where 1 indicates perfect agreement.
3. **Fowlkes-Mallows Index (FMI)**:
    
    - Measures the similarity between the clustering result and the ground truth based on the precision and recall of the pairs of points.
    - Ranges from 0 to 1, where 1 indicates perfect agreement.
4. **Homogeneity, Completeness, and V-Measure**:
    
    - Homogeneity: Measures whether all clusters contain only data points that are members of a single class.
    - Completeness: Measures whether all data points that are members of a given class are assigned to the same cluster.
    - V-Measure: Harmonic mean of homogeneity and completeness.
5. **Precision, Recall, and F1-Score**:
    
    - Precision: Measures the proportion of true positive pairs among all pairs assigned to the same cluster.
    - Recall: Measures the proportion of true positive pairs among all pairs that should be clustered together.
    - F1-Score: Harmonic mean of precision and recall.