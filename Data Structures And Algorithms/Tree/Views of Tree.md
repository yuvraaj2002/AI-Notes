When we talk about tree data structure then there are around 4 different types of views which we come across, these are top, bottom, left and right view. So in this page we will talk about all such types of views along with code and time complexity.

### [Top view of tree](https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1)

- Inorder → **`Not work`**
- Preorder → **`Will work`**
- Postorder → **`Not work`**
- Level order → **`Will work`**

##### Approach Using the preorder

- In this approach we will use the preorder traversal and for every node and its given line index we will store key value pair in the map data structure but if and only if the current node is first coming node for the given line.
- Other than this we will implement the preorder as it is and finally iterate over all the values of ordered map data structure and push the key→ **value in the vector.**

##### Approach using level order

- Simply perform the level order traversal and keep track of the nodes visited for every line index, in short we need to make sure that for every line index the first coming nodes needs to be considered.
- To keep track of first coming node we will be using map data structure

Time complexity O(n) + O(nlog(n)) + O(n) ~ O(nlog(n)) and extra space complexity O(n)
```cpp
class Solution
{
    public:
    //Function to return a list of nodes visible from the top view
    vector<int> topView(Node *root)
    {
        vector<int> ans;
        if(root == NULL)
        {
            return ans;
        }
        queue<pair<Node *,int>> q;
        map<int,int> mp;
        
        // Initial configuration
        q.push({root,0});
        
        while(!q.empty())
        {
            Node *curr = q.front().first;
            int line = q.front().second;
            q.pop();
            
            // Check if node is unique for the given line
            if(mp.find(line) == mp.end())
            {
                mp[line] = curr->data;
            }
            
            if(curr->left != NULL)
            {
                q.push({curr->left,line-1});
            }
            if(curr->right != NULL)
            {
                q.push({curr->right,line+1});
            }
        }
        
        // Push items from map to vector
        for(auto it: mp)
        {
            ans.push_back(it.second);
        }
        return ans;
    }
};
```

### [Bottom view of tree](https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card)

##### Approach (Using Level Order)

- This will be very much similar to that of the top view but the only difference is that we will make sure that rather than focusing on first coming node for the given line index we will always keep on updating the value for the key (line)
- In this we will be able to capture the last coming node for the given line

Time complexity O(n) + O(nlog(n)) + O(n) ~ O(nlog(n)) and extra space complexity O(n)
```cpp
class Solution {
  public:
    
    vector <int> bottomView(Node *root) 
    {
        vector<int> ans;
        if(root == NULL)
        {
            return ans;
        }
        queue<pair<Node *,int>> q;
        map<int,int> mp;
        
        // Initial configuration
        q.push({root,0});
        
        while(!q.empty())
        {
            Node *curr = q.front().first;
            int line = q.front().second;
            q.pop();
            
            // Always updating (last coming for given line)
            mp[line] = curr->data;
            
            if(curr->left != NULL)
            {
                q.push({curr->left,line-1});
            }
            if(curr->right != NULL)
            {
                q.push({curr->right,line+1});
            }
        }
        
        // Push items from map to vector
        for(auto it: mp)
        {
            ans.push_back(it.second);
        }
        return ans;
    }
};
```

### [Left view of tree](https://www.geeksforgeeks.org/problems/left-view-of-binary-tree/1)

- Perform the level order traversal
- Store the first node for the given level

Time complexity O(n) and extra space complexity O(1)
```cpp
vector<int> leftView(Node *root)
{
   // Initial coniguration
   queue<Node *> q;
   vector<int> ans;
   if(root == NULL)
   {
       return ans;
   }
   
   q.push(root);
   while(!q.empty())
   {
       // To keep track of first node of level via index we iterate over level nodes using loop
       int q_size = q.size();
       for(int i=0;i<q_size;i++)
       {
           Node *curr = q.front();
           q.pop();
           
           if(i == 0)
           {
               ans.push_back(curr->data);
           }
           if(curr->left != NULL)
           {
               q.push(curr->left);
           }
           if(curr->right != NULL)
           {
               q.push(curr->right);
           }
       }
   }
   return ans;
}
```
### [Right view of tree]()

- Perform the level order traversal
- Store the last node for the given level

Time complexity O(n) and extra space complexity O(1)
```cpp
class Solution {
public:
    /* Right view : Last node of the current stage */
    vector<int> rightSideView(TreeNode* root) 
    {
        // Base condition
        if(root == NULL)
        {
            return {};
        }

        // Initial configuration
        queue<TreeNode *> q;
        vector<int> values;
        q.push(root);

        // Performing breadth first traversal
        while(!q.empty())
        {
            // Getting the size of the queue level
            int size = q.size();

            // Iterating over the node values (Store connection and store last node)
            for(int i=0;i<size;i++)
            {
                // Taking node out from queue
                TreeNode *curr = q.front();
                q.pop();

                // Storing condition
                if(i == size-1)
                {
                    // Store this node value as right view
                    values.push_back(curr->val);
                }

                if(curr->left != NULL)
                {
                    q.push(curr->left);
                }
                if(curr->right != NULL)
                {
                    q.push(curr->right);
                }
            }
        }
        return values;
    }
};
```