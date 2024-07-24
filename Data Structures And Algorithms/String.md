This page is dedicated towards understanding the problems related to strings in Data structures and algorithms and here I will be mentioning most commonly asked interview questions along with their solutions.


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

###### [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)

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

###### [Longest Substring without repeating characteres](https://leetcode.com/problems/longest-substring-without-repeating-characters/)