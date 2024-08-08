This page is dedicated towards understanding the problems related to strings in Data structures and algorithms and here I will be mentioning most commonly asked interview questions related to subsequences.

### [Find the longest common subsequence between 2 strings](https://www.naukri.com/code360/problems/longest-common-subsequence_1063255?topList=top-string-coding-interview-questions&problemListRedirection=true&difficulty%5B%5D=Medium&sort_entity=company_count&sort_order=DESC)

###### [Approach 1](#)

- Generate all the possible subsequences from the 2 strings
- Compare the subsequences and find the maximum length

Time Complexity $O(2^n) + O(2^m)$ and Space complexity $O(n+m)$

```cpp
#include <bits/stdc++.h>
using namespace std;

void find_subs(int index, string sub_string, string st, vector<string>& subseq) {
    
    // Base condition
    if (index == st.length()) 
    {
        if (sub_string.length() >= 1) 
        {
            subseq.push_back(sub_string);
        }
        return;
    }

    // Selecting current index character
    find_subs(index + 1, sub_string + st[index], st, subseq);

    // Ignoring the current index character
    find_subs(index + 1, sub_string, st, subseq);
}

int getLengthOfLCS(string& str1, string& str2) 
{
    // Initializing vectors to store the subsequences
    vector<string> subseq1;
    vector<string> subseq2;
    int length = 0;
    int index = 0;
    string sub_string = "";

    // Calling function to find the substrings
    find_subs(index, sub_string, str1, subseq1);
    find_subs(index, sub_string, str2, subseq2);

    // Finding the common substrings
    for (int i = 0; i < subseq1.size(); i++) 
    {
        for (int j = 0; j < subseq2.size(); j++) 
        {
            if (subseq1[i] == subseq2[j]) 
            {
                length = max(length, (int)subseq1[i].length());
                break;
            }
        }
    }
    return length;
}
```


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
- [Find the minimum window in a string which contains all characters of another string](#)

- [Generate the nth term in the count-and-say sequence](#)
- [Generate all permutations of a given string](#)