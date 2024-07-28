This page is dedicated towards understanding the problems related to strings in Data structures and algorithms and here I will be mentioning most commonly asked interview questions along with their solutions.

### [Reverse a string](#)
### [Check if a given string is a palindrome](#)
### [Find the longest palindromic substring](#)
### [Check if two strings are anagrams of each other](#)
### [Perform basic string compression using the counts of repeated characters](#)
### [Find the first non-repeating character in a string](#)
### [Implement substring search algorithms like KMP or Rabin-Karp](#)
### [Implement the `atoi` function that converts a string to an integer](#)
### [Find the longest common substring between two strings](#)
### [Find the longest common prefix among a set of strings](#)
### [Group an array of strings such that all anagrams are grouped together](#)
### [Generate the nth term in the count-and-say sequence](#)
### [Generate all permutations of a given string](#)
### [Determine if a string can be segmented into a space-separated sequence of dictionary words](#)
### [Check if the parentheses in a string are valid and balanced](#)
### [Find the minimum number of operations required to convert one string to another](#)
### [Find the length of the longest substring without repeating characters](#)
### [Find the minimum window in a string which contains all characters of another string](#)
### [Convert a string into a zigzag pattern on a given number of rows](#)
### [Implement wildcard pattern matching with support for '?' and '*'](#)
### [Implement regular expression matching with support for '.' and '*'](#)
### [Multiply two non-negative integers represented as strings](#)
### [Implement the `strStr()` function that returns the index of the first occurrence of a substring](#)
### [Determine if a string can be made a palindrome by deleting at most one character](#)
### [Find the length of the longest substring that contains at most K distinct characters](#)











### [Write a program to reverse a string](https://leetcode.com/problems/reverse-string/)

- Initialize 2 pointers pointing at the start and end respectively 
- Until start and end are not pointing to same character index then swap the characters
- After swapping increment and decrement the 2 pointers respectively

Time Complexity O(n/2) ~ O(n) and extra space complexity O(1)
```C++
class Solution {
public:
    void reverseString(vector<char>& s) 
    {
        int start = 0;
        int end = s.size()-1;
        while(start < end)
        {
            // Swapping the characters
            char temp = s[start];
            s[start] = s[end];
            s[end] = temp;

            // Incrementing and decrementing
            start++;
            end--;
        }
    }
};
```

### [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)

- First parse the string and only add the non alphanumeric characters into temp string
- Then use 2 pointer approach to check if the characters are same or not

Time Complexity O(n + n/2) ~ O(n) and extra space complexity O(n)
```C++
class Solution {
public:
    bool isPalindrome(string s) 
    {
        // Initial configuration
        string check = "";
        for(int i=0;i<s.length();i++)
        {
            if((s[i] >= 'a'&& s[i] <= 'z') || (s[i] >= 'A'&& s[i] <= 'Z') || (s[i] >= '0' && s[i] <= '9'))
            {
                check = check + char(tolower(s[i]));
            }
            else
            {
                continue;
            }
        }

        // Using 2 pointers
        int start = 0;
        int end = check.length()-1;
        while(start < end)
        {
            if(check[start] == check[end])
            {
                start++;
                end--;
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

Further we can improve this by making sure that we are not storing the characters into the string and instead updating the pointers itself

```C++
Pending
```

### [Longest Substring without repeating characteres](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

