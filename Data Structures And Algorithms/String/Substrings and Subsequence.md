### [Find the longest palindromic substring](https://leetcode.com/problems/longest-palindromic-substring/description/)

There are couple of approaches with which we can actually solve this problem so let us discuss each of the approach sequentially.
##### Approach 1 (Generating all substrings)




- Generate all the possible substrings
- Out of all the substrings the ones which are of length 2 
	- Compare 0 and size-1 index character 
		- If same then update the ans string variable 
- For substring of length more than 3 make a function call and if it returned true
	- Update ans (If length is more than ans length)

Time complexity $O(n^2) + O(n) ~= O(n^2)$ and space complexity O(1)
```cpp
class Solution {
public:
    bool is_palindrome(string check) 
    {
        int start = 0;
        int end = check.length() - 1;
        while (start < end) {
            if (check[start] != check[end]) {
                return false;
            } else {
                start++;
                end--;
            }
        }
        return true;
    }

    string longestPalindrome(string s) 
    {
        // Initial configuration
        vector<string> substrings;
        string ans = s.substr(0, 1); // Start with the first character

        // Generating all possible substrings
        for (int i = 0; i < s.length(); i++) 
        {
            string substr = "";
            for (int j = i; j < s.length(); j++) 
            {
                substr += s[j];
                if (substr.length() > 1) 
                {
                    // Reducing search space by focusing on only substring length > 2
                    if (substr.length() == 2) 
                    {
                        if(substr[0] == substr[1]) 
                        {
                            // Yes palindrome but update if longer
                            if(substr.length() > ans.length())
                            {
                                ans = substr;
                            }
                        }
                    } 
                    else 
                    {
                        if(is_palindrome(substr))
                        {
                            if(substr.length() > ans.length())
                            {
                                ans = substr;
                            }
                        }
                    }
                }
            }
        }
        return ans;
    }
};
```


### [Implement substring search algorithms like KMP or Rabin-Karp](#)


### [Find the longest common substring between two strings](https://www.geeksforgeeks.org/problems/longest-common-substring1452/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card)

##### Approach 1 (Generating all substrings)

- Generate all possible substrings from both the given strings 
- Compare and find the matching substring
- Update the length variable if current substring length is greater

Time complexity $3*O(n^2) ~= O(n^2)$ and space complexity $O(n+m)$

```cpp
class Solution{
public:
    int longestCommonSubstr (string S1, string S2, int n, int m)
    {
        // Generating all possible substrings
        vector<string> substrings1;
        vector<string> substrings2;
        
        // Generating all possible substrings for S1
        for (int i = 0; i < S1.length(); i++) 
        {
            string substr = "";
            for (int j = i; j < S1.length(); j++) 
            {
                substr += S1[j];
                substrings1.push_back(substr);
            }
        }
        
        // Generating all possible substrings for S2
        for (int i = 0; i < S2.length(); i++) 
        {
            string substr = "";
            for (int j = i; j < S2.length(); j++) 
            {
                substr += S2[j];
                substrings2.push_back(substr);
            }
        }
        
        // Searching the common longest substring
        int length = 0;
        for(auto &it: substrings1)
        {
            for(auto &jt : substrings2)
            {
                if(it == jt)
                {
                    length = max(length, static_cast<int>(it.length()));
                }
            }
        }
        return length;
    }
};
```


- [Find the longest common prefix among a set of strings](#)
- [Find the length of the longest substring without repeating characters](#)
-  [Find the length of the longest substring that contains at most K distinct characters](#)
- [Find the minimum window in a string which contains all characters of another string](#)

- [Generate the nth term in the count-and-say sequence](#)
- [Generate all permutations of a given string](#)