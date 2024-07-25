This page is dedicated towards the code and understanding of all the different types of traversals in tree data structure and to be more precise there are 4 different types of traversals.

1. Inorder
2. Preorder
3. Postorder
4. Level order

Now the thing is (Inorder, Preorder and Postorder) traversals can be done either in recursive, iterative manner. In addition to this Morris order traversal also exist which is sort of an extension or optimization on top of current traversals.

### Inorder, Preorder and Postorder (Recursive)

- In case of Inorder traversal we first visit the left subtree, then current node and finally the right subtree
- In case preorder we first visit the current node, then left subtree and finally right subtree
- In case of postorder traversal we first visit the left subtree, then right subtree and finally the current node

Problem link to practice the Inorder traversal [LeetCode Inorder traersasl](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)
Time complexity is O(n) and extra space complexity is O(1)
```cpp
void inorder(TreeNode *root,vector<int> &ans)
    {
        // Base condition
        if(root == NULL)
        {
            return;
        }

        // Making left function call
        inorder(root->left,ans);

        // Storing the value
        ans.push_back(root->val);

        // Making right function call
        inorder(root->right,ans);
    }

#################################################################################

void preorder(TreeNode *root,vector<int> &ans)
    {
        // Base condition
        if(root == NULL)
        {
            return;
        }
        
	    // Storing the value
        ans.push_back(root->val);

        // Making left function call
        preorder(root->left,ans);

        // Making right function call
        preorder(root->right,ans);
    }

#################################################################################

void postorder(TreeNode *root,vector<int> &ans)
    {
        // Base condition
        if(root == NULL)
        {
            return;
        }

        // Making left function call
        postorder(root->left,ans);

        // Making right function call
        postorder(root->right,ans);

		// Storing the value
        ans.push_back(root->val);
    }
```


