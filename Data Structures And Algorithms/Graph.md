The best way to grasp and learn something is to divide the topic into smaller subtopics so we will also be using the same concept where rather than doing questions randomly we will be focusing on the important subtopics. And the various subtopics which we will consider in graph are 

1. Traversal
2. Breadth first search
3. Depth first search
4. Shortest path
5. Graph connectivity


### [Node to destination path](https://www.interviewbit.com/problems/path-in-directed-graph/)

- We will follow DFS so start from the given node and mark it as visited 
- Then go over all the unvisited connections
	- If current connection node is is unvisited and destination node then return true
	- Otherwise make a function call for that node connection
 - At the end for given node return false if  we didn't got true for this connections

Time complexity O(V+E) and extra space complexity is O(1) even though stack space in memory will be O(V)
```cpp
bool find(int node, vector<int> &visited, vector<int> adj[], int final_node) {
    // Marking current node as visited
    visited[node] = 1;

    // Going over the unvisited connections
    for(auto it: adj[node]) {
        if(visited[it] == -1) {
            if(it == final_node) {
                // Path found
                return true;
            } else {
                // Make function call
                if(find(it, visited, adj, final_node) == true) {
                    return true;
                }
            }
        }
    }

    // Went to all connections for current node but didn't find
    return false;
}

int Solution::solve(int A, vector<vector<int> > &B) {
    // Initial configuration
    vector<int> visited(A+1, -1);

    // Creating adjacency list
    vector<int> adj[A+1];
    for(auto it: B) {
        int n1 = it[0];
        int n2 = it[1];
        adj[n1].push_back(n2);
    }

    if(find(1, visited, adj, A) == true) {
        return 1;
    }
    return 0;
}

```


### 

