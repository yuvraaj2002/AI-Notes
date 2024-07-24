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
### [Remove N-th Node From End of List]()
### [Find the Middle of a Linked List]()
### [Intersection of Two Linked Lists]()
### [Remove Duplicates from Sorted List]()
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
### [Flatten a Multilevel Doubly Linked List]()
### [Convert Sorted List to Binary Search Tree]()
