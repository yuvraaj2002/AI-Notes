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
