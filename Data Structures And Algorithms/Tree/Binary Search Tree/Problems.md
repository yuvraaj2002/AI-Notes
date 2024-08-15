
### [Find Minimum value in BST](https://www.geeksforgeeks.org/problems/minimum-element-in-bst/1)

- Standing at the current node in the tree
- Look for the left most leaf node in the tree
- If current node's left exist then move to that node, otherwise stop and return node value

Time Complexity O(n) and space complexity is O(1)

```python
#User function Template for python3

"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        
        # Find the left most child node
        while root.left is not None:
            root = root.left
            
        return root.data
```

### [Insert node in the binary search tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/description/)

- Standing at root node look for appropriate leaf node
- Check if current node value is smaller or greater than new value
- If new value is greater, look if right is null or not, if not move otherwise attach node
- Do the same for the left node as well

Time Complexity O(n) and space complexity is O(1)

```python
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        temp = root
        newnode = TreeNode(val)

        # Base condition
        if temp is None:
            temp = newnode
            return temp

        # Finding the appropriate leaf node
        while temp is not None:

            # Checking if value is smaller or greater than current node
            if val > temp.val:
                if temp.right is not None:
                    temp = temp.right
                else:
                    temp.right = newnode
                    break
            else:
                if temp.left is not None:
                    temp = temp.left
                else:
                    temp.left = newnode
                    break

        return root
```

### [Delete node from the binary search tree](https://leetcode.com/problems/delete-node-in-a-bst/)

- Standing at the current node in the tree, look for the parent node of the node to be removed.
- Create a function that takes the node to be removed and return the new connections
- New connection involves connecting the left child of node to be removed with the left most child of the right child.

Time Complexity O(n) and space complexity is O(1)

```python
class Solution:
    def build_connections(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Base conditions
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Storing the left and right children
        left_child = root.left
        right_child = root.right

        # Finding smallest value node of right_child
        temp = right_child
        while temp.left is not None:
            temp = temp.left

        temp.left = left_child
        return right_child

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # Base condition
        if root is None:
            return None

        if root.val == key:
            return self.build_connections(root)  # Use self.build_connections here

        # Finding the parent node of node to be removed
        find_node = root
        while find_node is not None:
            if find_node.left is not None:
                if find_node.left.val == key:
                    find_node.left = self.build_connections(find_node.left)
                    break
                else:
                    find_node = find_node.left

            elif find_node.right is not None:
                if find_node.right.val == key:
                    find_node.right = self.build_connections(find_node.right)  
                    break
                else:
                    find_node = find_node.right

        return root
```


### [Check if tree is BST or BT](https://leetcode.com/problems/validate-binary-search-tree/description/)


##### [Approach 1 (Using Inorder)](#)

- Perform Inorder traversal on the tree 
- Check if the values are arranged in ascending order or not

Time complexity O(2n) and space complexity O(n)

```python
class Solution:
    def inorder(self,values : List[int],root: Optional[TreeNode]) -> List[int]:

        # Base condition
        if root is None:
            return
        
        # Accessing the left subtree, current node and right subtree
        self.inorder(values,root.left)
        values.append(root.val)
        self.inorder(values,root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        values = []

        # Calling the function to get values
        self.inorder(values,root)

        # Iterating and checking if values are sorted or not
        for i in range(len(values)-1):
            if values[i] >= values[i+1]:
                return False

        return True
```

### [Find LCA for the binary search tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

- Standing at the current node if the root node lies in between the p and q node then return root
- Otherwise look for the direction in which we must actually move.

Time Complexity O(n) and space complexity O(1)

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Base conditions
        if (p.val < root.val and root.val < q.val) or (p.val > root.val and root.val > q.val):
            return root
        elif root == p or root == q:
            return root

        # Selecting which side to move
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return self.lowestCommonAncestor(root.left,p,q)
```