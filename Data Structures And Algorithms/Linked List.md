This page is dedicated towards understanding the problems related to strings in Data structures and algorithms and here I will be mentioning most commonly asked interview questions along with their solutions.

### [Reverse a Linked List](https://leetcode.com/problems/reverse-linked-list/)

- We will be using three pointers (current, next and previous) to keep track of the current node, next remaining linked list and previous on going list.
- We will initially start going over the linked list with the condition that while current is not null 
	- Move the `next` pointer to `current->next`
	- Connect the `current->next` to the `prev` pointer
	- Move `prev` to `curr` and `curr` to `next`

Time complexity O(n) and extra space complexity
```C++
class Solution {
public:
    ListNode* reverseList(ListNode* head) 
    {
        // Base condition
        if(head == NULL || head->next == NULL)
        {
            return head;
        }

        // Initial configuration
        ListNode *curr = head;
        ListNode *next = NULL;
        ListNode *prev = NULL;

        while(curr != NULL)
        {
            // Moving next to keep track of remaining list
            next = curr->next;

            // Breaking connection and connecting to the prev
            curr->next = prev;

            // Putting prev on current position
            prev = curr;

            // Moving the current further using next
            curr = next;
        }
        return prev;
    }
};
```

### [Detect a Cycle in a Linked List]()

To solve this problem we can have couple of approaches so we will discuss them one by one where the first approach will use O(n) time and space complexity and the second approach will further optimize to reduce the extra space to constant space complexity

##### Approach 1 (Set data structure)
- Initialize a set data structure to store the object pointers
- Start going over the nodes of linked list and if the current nodes exist in set then break the loop and return true
- Otherwise insert the node into the set data structure and move further
```cpp
class Solution {
public:
    bool hasCycle(ListNode *head) 
    {
        // Initial configurtion
        set<ListNode *> st;
        ListNode *temp = head;

        while(temp != NULL)
        {
            if(st.find(temp) != st.end())
            {
                // Cycle exist
                return true;
            }
            st.insert(temp);
            temp = temp->next;
        }
        return false;
    }
};
```

##### Approach 2 (Using fast and slow pointer)

- Move the slow pointer half the speed of the fast pointer and if there would be cycle then at some point the fast will coincide with the slow and that would mean the cycle exist
```cpp
class Solution {
public:
    bool hasCycle(ListNode *head) 
    {
        // Initial cofiguration
        ListNode *slow = head;
        ListNode *fast = head;
        while(fast != NULL && fast->next != NULL)
        {
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast)
            {
                // cycle exist
                return true;
            }
        }

        // Cycle doesn't exist
        return false;
    }
};
```

### [Merge Two Sorted Linked Lists]()


### [Remove N-th Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

- First find the length of the linked list and then calculate the number jumps we need to reach the node (just before the note to be deleted)
- In case the jumps = 0 it means we need to remove the head so move the head to next and return head
- Otherwise make length-k-1 jumps from the head, remove next node and fix connection

Time complexity O(n) and extra space complexity O(1)
```cpp
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) 
    {
        // Finding the length of the linked list
        ListNode *findlen = head;
        int length = 0;
        while(findlen != NULL)
        {
            findlen = findlen->next;
            length++;
        }

        // Condition
        if(length == n)
        {
            head = head->next;
            return head;
        }

        int jumps = length-n-1;
        findlen = head;
        while(jumps > 0)
        {
            findlen = findlen->next;
            jumps--;
        }
        ListNode *remove = findlen->next;
        findlen->next = remove->next;
        delete(remove);
        return head;
    }
};
```


### [Find the Middle of a Linked List](https://leetcode.com/problems/middle-of-the-linked-list/submissions/1256522396/)

To solve this problem we can have couple of approaches so we will discuss them one by one where the first approach will use O(n) time and constant space complexity and the second approach will further optimize the time complexity.

##### Approach 1 (Finding middle via length)

- First find the length of the linked list by going over it for once 
- Then calculate the number of jumps we would need to reach middle
- Jumps = length/2
```cpp
class Solution {
public:
    /*
    Total nodes / 2 and its floor value will be jumps 
    */
    ListNode* middleNode(ListNode* head) 
    {
        // Initail configuration
        ListNode *temp = head;
        int count = 0;

        while(temp != NULL)
        {
            temp = temp->next;
            count++;
        }
        int jumps = count/2;
        temp = head;
        while(jumps > 0)
        {
            temp = temp->next;
            jumps--;
        }
        return temp;
    }
};
```

##### Approach 2 (Using tortoise hare approach)
- In this approach we simply initialize 2 pointers generally called slow and fast pointer with head of linked list.
- After doing so we the fast pointer moves twice the speed of the slow pointer and once the condition `while(fast!= null and fast->next != null` becomes false we return the slow pointer.
```cpp
Node *fast = head;
Node *slow = head;
while(fast != NULL && fast->next != NULL)
{
	slow = slow->next;
	fast = fast->next->next;
}
return slow;
```

### [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/1288072848/)

To solve this problem we can have couple of approaches so we will discuss them one by one where the first approach will use O(n) time and space complexity and the second approach will further optimize to reduce the extra space to constant space complexity

##### Approach 1 (Using set)
- Go over the first linked list and store the nodes into the set
- Go over the second linked list and for node which already exist in the set is the node where the intersection is actually happening
```cpp
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) 
    {
        // Initial configuration
        unordered_set<ListNode *> st;

        // Going over the list1 and storing the nodes
        ListNode *temp1 = headA;
        while(temp1 != NULL)
        {
            st.insert(temp1);
            temp1 = temp1->next;
        }

        // Setup for the second linked list
        ListNode *temp2 = headB;
        while(temp2 != NULL)
        {
            if(st.find(temp2) != st.end())
            {
                return temp2;
            }
            temp2 = temp2->next;
        }
        return NULL;
    }
};
```

##### Approach 2 (Using 2 pointers)


### [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/1048901040/)

- Traverse the linked list with the condition that while current node is not null
- If the condition is satisfied then check whether the next node value is same as the current node value and if so then remove the next node and fix the connection
- Otherwise move the pointer to next node
- Note that after removing the node we will not move to next node because there is a possibility that the new connection will have the same scenario

Time complexity O(n) and extra space complexity O(1)
```cpp
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) 
    {
        // Base condition
        if(head == NULL)
        {
            return head;
        }

        ListNode *find = head;
        while(find->next != NULL)
        {
            if(find->val == find->next->val)
            {
                ListNode *remove = find->next;
                find->next = remove->next;
                delete(remove);
            }
            else
            {
                find = find->next;
            }
        }
        return head;
    }
};
```
### [Add Two Numbers Represented by Linked Lists]()
### [Copy List with Random Pointer]()
### [Swap Nodes in Pairs]()
### [Rotate List]()
### [Reverse Nodes in k-Group]()
### [Sort a Linked List]()
### [Merge k Sorted Lists]()
### [Delete Node in a Linked List]()
### [Partition List]()
### [Linked List Cycle II (Find the node where the cycle begins)]()
### [Palindrome Linked List]()

To solve this problem we will be utilizing various concepts such as finding the middle of linked list, then reversing linked list and also 2 pointers
- Find the middle of the linked list ( but node before the actual middle)
- Reverse the linked list from the current found node->next and break the connection
- Use 2 pointers to to compare the node values

Time Complexity O(n + n + n) ~ O(n) and extra space complexity O(1)
```cpp
class Solution {
public:
    ListNode* reverseList(ListNode* head) 
    {
        // Initial configuration
        ListNode *curr = head;
        ListNode *next = head;
        ListNode *prev = NULL;

        while(curr != NULL)
        {
            // Storing the remainig list in next pointer
            next = curr->next;

            // Connecting the curr to prev
            curr->next = prev;

            // Moving prev to curr and curr to next
            prev = curr;
            curr = next;
        }
        return prev;
    }

    bool isPalindrome(ListNode* head) 
    {
        // Step 1: Finding node before middle
        // Initail configuration
        ListNode *vslow = head;
        ListNode *slow = head;
        ListNode *fast = head;

        while(fast != NULL && fast->next != NULL)
        {
            vslow = slow;
            slow = slow->next;
            fast = fast->next->next;
        }

        // Calling the function to reverse linked list
        vslow->next = NULL;
        ListNode *head2 = reverseList(slow);
        ListNode *head1 = head;

        // Comparing the node values
        while(head1 != NULL && head2 != NULL)
        {
            if(head1->val != head2->val)
            {
                // Not a palindrome
                return false;
            }
            head1 = head1->next;
            head2 = head2->next;
        }
        // Yes it is palindrome
        return true;;
    }
};
```
### [Flatten a Multilevel Doubly Linked List]()
### [Convert Sorted List to Binary Search Tree]()
