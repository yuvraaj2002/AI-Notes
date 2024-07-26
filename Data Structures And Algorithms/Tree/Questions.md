
### [Find the maximum depth of a binary tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

In the problem statement the depth refers to number of nodes across the longest root-leaf path
- Standing at current node get left and right depth
- Return 1 + maximum(left, right)
- Bottom up approach will be used
- Depth of the leaf node will be 1

Time complexity O(n) and extra space complexity O(1)
```cpp
class Solution {
public:
    int maxDepth(TreeNode* root) 
    {
        // Base conditions
        if(root == NULL)
        {
            return 0;
        }
        
        // Getting access to left and right depths
        int left = maxDepth(root->left);
        int right = maxDepth(root->right);
        return 1 + max(left,right);
    }
};
```
### [Check if a binary tree is balanced](https://leetcode.com/problems/balanced-binary-tree/description/)

- Standing at the current node we need to have access to the left and right depths/heights
- If the absolute difference between left and right subtree is more than 1 then we will return -1
- Otherwise we will return 1 + max(left, right) : As the depth of the current node
- Also from left or right function calls if we will get -1 then we will simply return -1 without doing anything

Time complexity O(n) and extra space complexity O(1)
```cpp
class Solution {
public:
    int solve(TreeNode *root)
    {
        // Base condition
        if(root == NULL)
        {
            return 0;
        }

        // GEtting the left and right height
        int left = solve(root->left);
        if(left == -1)
        {
            return -1;
        }

        int right = solve(root->right);
        if(right == -1)
        {
            return -1;
        }

        // Checking the height balanced for current node
        if(abs(left-right) > 1)
        {
            return -1;
        }
        return 1 + max(left,right);
    }
    bool isBalanced(TreeNode* root) 
    {
        // Base condition
        if(root == NULL)
        {
            return true;
        }    

        // Making function call 
        int ans = solve(root);
        if(ans == -1)
        {
            return false;
        }
        return true;
    }
};
```

### [Check if a binary tree is a binary search tree (BST)](#)

There are couple of approaches which we can use to detect whether a binary tree is actually binary search tree or not, so let us discuss each of the approach

##### Approach 1 (Using Inorder)
- Perform inorder traversal and get the values stored in the vector
- Check if the values are sorted in ascending order or not

Time complexity O(n) + O(n) ~ O(n) and extra space complexity O(n)
```cpp
class Solution {
public:
    void inorder_traversal(TreeNode *root,vector<int> &values)
    {
        // Base condition
        if(root == NULL)
        {
            return;
        }

        // Making left function call, accessing root and making right function call
        inorder_traversal(root->left,values);
        values.push_back(root->val);
        inorder_traversal(root->right,values);
    }
    bool isValidBST(TreeNode* root) 
    {
        // Initial configuration
        vector<int> values;
        TreeNode *temp = root;

        // Making function call to get the values
        inorder_traversal(temp,values);

        // Checking if the values are arranged in sorted manner or not
        for(int i=0;i<values.size()-1;)
        {
            if(values[i] < values[i+1])
            {
                i++;
            }
            else
            {
                return false;
            }
        }
        return true;
    }
};
```

##### Approach 2 (Using the ranges)

- The idea is that standing at current node we will check if it is within the range or not.
- If it is within the range then we can make the left and right function calls
- For the left function calls the current node value will act like the upper limit
- For right function call current node value will act like lower limit

Time complexity O(n)  and extra space complexity O(1)
```cpp
class Solution {
public:
    bool check(TreeNode *root,long min_range,long max_range)
    {
        // Base condition
        if(root == NULL)
        {
            return true;
        }

        // Checking the range of current node value
        if(root->val > min_range && root->val < max_range)
        {
            if(check(root->left,min_range,root->val) == false)
            {
                return false;
            }
            if(check(root->right,root->val,max_range) == false)
            {
                return false;
            }
            return true;
        }
        else
        {
            return false;
        }
    }
    bool isValidBST(TreeNode* root) 
    {
        // Initial configuration
        long min_range = LONG_MIN;
        long max_range = LONG_MAX;
        return check(root,min_range,max_range);
    }
};
```

### [Find the lowest common ancestor (LCA) of two nodes in a binary tree](#)

### [Find the diameter of a binary tree](https://leetcode.com/problems/diameter-of-binary-tree/)

- Standing at current node we need to have access to the left and right node counts
- Add the left + right to get the diameter at current node and use it for updating the maximum diameter
- Finally return 1 + maximum (left, right)

Time complexity O(n) and extra space complexity O(1)
```cpp
class Solution {
public:
    int find_diameter(TreeNode *root,int &max_diameter)
    {
        // Base condition
        if(root == NULL)
        {
            return 0;
        }
        if(root->left == NULL && root->right == NULL)
        {
            return 1;
        }

        // Getting the count of edges on left and right
        int left = find_diameter(root->left,max_diameter);
        int right = find_diameter(root->right,max_diameter);

        // Updating the maximum diameter
        max_diameter = max(max_diameter,left+right);
        return 1 + max(left,right);
    }
    int diameterOfBinaryTree(TreeNode* root) 
    {
        // Base condition
        if(root->left == NULL && root->right == NULL)
        {
            return 0;
        }

        // Initial configuration
        int max_diameter = 0;
        int value = find_diameter(root,max_diameter);
        return max_diameter;
    }
};
```

### [Convert a sorted array to a balanced BST](#)
### [Convert a binary tree to a doubly linked list](#)
### [Serialize and deserialize a binary tree](#)
### [Check if two binary trees are identical](https://leetcode.com/problems/same-tree/description/)

##### Approach 1 (Using Inorder)

- Perform inorder traversals for both the trees 
- If the length of vector storing the inorder is not same then return false otherwise return true
- If the vector lengths are same then check if both are arranged in ascending order or not and have same value for same index or not, for this we can use index pointers

##### Approach 2 (Using Pointers)

- Simply perform the postorder traversal for both the trees parallelly
- If at some point both nodes are null then return true otherwise return false
- Then check for left subtree, right subtree
- So for if things are going great then check node values and return true or false respectively

Time complexity O(n) and extra space complexity O(1)
```cpp
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) 
    {
        // Base condition
        if(p == NULL && q == NULL)
        {
            return true;
        }
        if((p == NULL && q != NULL) || (p != NULL && q == NULL))
        {
            return false;
        }

        // Getting green flag from left and right 
        bool left = isSameTree(p->left,q->left);
        if(left == false)
        {
            return false;
        }
        bool right = isSameTree(p->right,q->right);
        if(right == false)
        {
            return false;
        }

        // COmparing the current node values
        if(p->val != q->val)
        {
            return false;
        }
        return true;
    }
};
```
### [Check if a binary tree is symmetric](https://leetcode.com/problems/symmetric-tree/description/)

- Apply inorder for both the subtrees but for the left subtree we will use correct inorder 
- For the right subtree we will be using the reverse inorder

Time complexity O(n) and extra space complexity O(1)
```cpp
class Solution {
public:
    bool check(TreeNode *root1,TreeNode *root2)
    {
        // Base condition
        if(root1 == NULL && root2 == NULL)
        {
            return true;
        }
        if((root1 == NULL && root2 != NULL) || (root1 != NULL && root2 == NULL))
        {
            return false;
        }

        // Performing the reverse inorder traversal
        if(check(root1->left,root2->right) == false)
        {
            return false;
        }

        // Comparing the current node values
        if(root1->val !=  root2->val)
        {
            return false;
        }

        if(check(root1->right,root2->left) == false)
        {
            return false;
        }

        // Everythinng working fine
        return true;
    }
    bool isSymmetric(TreeNode* root) 
    {
        // Base condition
        if(root->left == NULL && root->right == NULL)
        {
            return true;
        }
        return check(root->left,root->right);
    }
};
```
### [Find the kth smallest and largest element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)

##### Approach 1 (Using Inorder traversal)

- Perform the inorder traversal and store the vector values
- Make k-1 jumps from the starting of the vector to reach the required node

Time complexity O(n) + O(n) and extra space complexity O(n)

##### Approach 2 (Keeping track during traversal)

- We will perform inorder traversal 
- Whenever we will access a node we will increment the count try to match it with k
- If it matches then it means it is the required node so we will save it and return true

Time complexity O(n) and extra space complexity O(1)
```cpp
class Solution {
public:
    bool inorder(TreeNode *root,int &count,int k,int &ans)
    {
        // Base condition
        if(root == NULL)
        {
            return false;
        }

        // Making left function call if ans is not found
        bool left = inorder(root->left,count,k,ans);
        if(left == true)
        {
            return true;
        }
            
        // Incrementing the count
        count++;
        if(count == k)
        {
            ans = root->val;
            return true;
        }

        bool right = inorder(root->right,count,k,ans);
        if(right == true)
        {
            return true;
        }
        return false;
    }

    int kthSmallest(TreeNode* root, int k) 
    {
        // Initial configuration
        TreeNode *temp = root;
        int count = 0;
        int ans = -1;

        // Calling function to get the values
        bool completed = inorder(temp,count,k,ans);
        return ans;
    }
};
```

### [Find the maximum path sum in a binary tree](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)

- Standing at current node have access to left and right path sums
- Update the maximum path sum
- Return current node + max(left, right)
- Since we need to find the maximum path sum so considering the negative values will never give us good result so we will neutralize them by 0

Time complexity O(n) and extra space complexity O(1)
```cpp
class Solution {
public:
    int solve(TreeNode *root,int &maxps)
    {
        // Base conditions
        if(root == NULL)
        {
            return 0;
        }

        // Getting access to left and right subtree sum
        int left_sum = max(0,solve(root->left,maxps));
        int right_sum = max(0,solve(root->right,maxps));

        // Find the current sum and updating maxps
        maxps = max(maxps,root->val + left_sum + right_sum);
        return root->val + max(left_sum,right_sum);
    }
    int maxPathSum(TreeNode* root) 
    {
        int maxps = INT_MIN;
        int temp = solve(root,maxps);
        return maxps;
    }
};
```
### [Construct a binary tree from inorder and preorder traversal](#)
### [Construct a binary tree from inorder and postorder traversal](#)
### [Print the boundary nodes of a binary tree](#)
### [Check if a binary tree is a subtree of another binary tree](#)
### [Print all paths from root to leaf nodes](https://leetcode.com/problems/binary-tree-paths/description/)

- Standing at the current node if the string is empty then simply convert current integer value to string and add it in the path, otherwise if string is not empty then add in specific format
- Make left and right function calls accordingly
- For base conditions if the current node is null then simply return back
- If current node is leaf node, then again check emptiness and add accordingly, finally return the substring from 0 to length-2 index , where 0 is inclusive and other      value is exclusive

Time complexity O(n) and extra space complexity O(1)
```cpp
class Solution {
public:
    void solve(TreeNode *root,string current_path,vector<string> &ans)
    {
        // Base condition
        if(root == NULL)
        {
            return;
        }
        if(root->left == NULL && root->right == NULL)
        {
            if(current_path.empty())
            {
                // First node in path
                current_path = current_path + to_string(root->val);
            }
            else
            {
                current_path = current_path + "->"+ to_string(root->val);
            }

            ans.push_back(current_path);
            current_path = current_path.substr(0, current_path.length() - 2);
        }

        // Considering current node in the path
        if(current_path.empty())
        {
            // First node in path
            current_path = current_path + to_string(root->val);
        }
        else
        {
            current_path = current_path + "->" + to_string(root->val);
        }
        

        // Making left and right function calls
        solve(root->left,current_path,ans);
        solve(root->right,current_path,ans);

        // Removing current node from the path
        current_path = current_path.substr(0, current_path.length() - 2);
    }
    vector<string> binaryTreePaths(TreeNode* root) 
    {
        vector<string> ans;
        string current_path = "";
        solve(root,current_path,ans);
        return ans;
    }
};
```
### [Find the vertical order traversal of a binary tree](#)

### [Convert a binary tree to a sum tree](#)
### [Check if a binary tree has a path sum equal to a given sum](https://leetcode.com/problems/path-sum/description/)

- Standing at the current node subtract the node value from the target sum as the sign of accepting the current value of the path
- Then make left and right function calls
- At any given point if the current node is null then return false
- Otherwise if the current node is leaf node then, then accept current node value and check for following conditions
	- Is target sum = 0 , if yes then return true, Otherwise return false
	- Irrespective whether we get true or false we need to restore the value so we will add the current node value
- Point to consider is that even though we might get target sum to be negative at one point, still we will not stop because in the tree negative values also exist.

Time Complexity O(n) and extra space complexity O(1)
```cpp
class Solution {
public:

    bool hasPathSum(TreeNode* root, int targetSum) 
    {
        // Base condition
        if(root == NULL)
        {
            return false;
        }
        if(root->left == NULL && root->right == NULL)
        {
            targetSum = targetSum-root->val;
            if(targetSum == 0)
            {
                // Restoring the value and returning true
                targetSum = targetSum+root->val;
                return true;
            }
            targetSum = targetSum+root->val;
            return false;
        }

        // Considering the current node value
        targetSum = targetSum-root->val;

        // Making left call
        bool left = hasPathSum(root->left,targetSum);
        if(left == true)
        {
            return true;
        }

        // Making right function call
        bool right = hasPathSum(root->right,targetSum);
        if(right == true)
        {
            return true;
        }

        targetSum = targetSum+root->val;
        return false;
    }
};
```
### [Check if a binary tree is height-balanced](#)
### [Flatten a binary tree to a linked list in-place](#)
