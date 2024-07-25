
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

### [Find the diameter of a binary tree](#)
### [Convert a sorted array to a balanced BST](#)
### [Convert a binary tree to a doubly linked list](#)
### [Serialize and deserialize a binary tree](#)
### [Check if two binary trees are identical](#)
### [Check if a binary tree is symmetric](#)
### [Find the kth smallest and largest element in a BST](#)

### [Find the maximum path sum in a binary tree](#)
### [Construct a binary tree from inorder and preorder traversal](#)
### [Construct a binary tree from inorder and postorder traversal](#)
### [Print the boundary nodes of a binary tree](#)
### [Check if a binary tree is a subtree of another binary tree](#)
### [Print all paths from root to leaf nodes](#)
### [Find the vertical order traversal of a binary tree](#)

### [Convert a binary tree to a sum tree](#)
### [Check if a binary tree has a path sum equal to a given sum](#)
### [Check if a binary tree is height-balanced](#)
### [Flatten a binary tree to a linked list in-place](#)
