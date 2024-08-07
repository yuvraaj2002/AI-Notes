
First of all we need to be aware about what does anagram actually means, so given 2 strings let say s1 and s2, if by arranging the characters of the string s2 we get s1 then we can say that both the strings are anagram of each other. For string to be called anagram of each other there are 2 conditions which must be met

1. The length must be same
2. The frequency count of characters must be same.

### [Check if 2 strings are anagram of each other](https://leetcode.com/problems/valid-anagram/description/)

###### [Approach 1](#)

Sort the strings and then compare them with each other.
Time complexity $O(n*log(n))$ 

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) 
    {
        // First condition
        if(t.length() != s.length())
        {
            return false;
        }

        // Inplace sorting
        sort(s.begin(),s.end());
        sort(t.begin(),t.end());
        if(s != t)
        {
            return false;
        }
        return true;
    }
};
```

###### [Approach 2](#)

- First make a check for the length of the strings and if not same then return false
- Use alphabets index vector to keep track of frequency count of the character in both the strings
- For the first string fill the frequency and for the second string decrement the frequency
- At the end if any index is not 0 then return false

Time complexity $O(n)$ and space complexity $O(26)$ 
```cpp
class Solution {
public:
    bool isAnagram(string s, string t) 
    {
        // First condition
        if(t.length() != s.length())
        {
            return false;
        }

        // Vector to store the frequency count
        vector<int> freq_count(26,0);

        // Iterating over the string s
        for(auto ch : s)
        {
            int index = ch-'a';
            freq_count[index]++;
        }

        // Now iterating over the t to decrement the count
        for(auto ch : t)
        {
            int index = ch-'a';
            freq_count[index]--;
        }

        // Checking if the vector is having all values to be 0 or not
        for(int i=0;i<26;i++)
        {
            if(freq_count[i] != 0)
            {
                return false;
            }
        }
        return true;
    }
};
```


### [Find all anagrams in the string](https://www.naukri.com/code360/problems/find-all-anagrams_975387?topList=top-string-coding-interview-questions&problemListRedirection=true&difficulty%5B%5D=Easy&sort_entity=company_count&sort_order=DESC&leftPanelTabValue=PROBLEM)

###### [Approach]

- Find all the substrings of the required length
- Check if the substring is anagram with given string or not
- If yes then store the starting index to be (index-substring length + 1)

Time complexity $O(n^2) *O(m*log(m))$ 
```cpp
vector<int> findAnagramsIndices(string str, string ptr, int n, int m)
{
    // Initial configuration
    vector<int> ans;
    string ptr_copy = ptr;
    sort(ptr_copy.begin(),ptr_copy.end());

    // Step 1 : Find substrings of length 3
    for(int i=0;i<str.length();i++)
    {
        string substring = "";
        for(int j=i;j<str.length();j++)
        {
            substring = substring + str[j];
            if(substring.length() == ptr_copy.length())
            {
                sort(substring.begin(),substring.end());
                if(substring == ptr_copy)
                {
                    ans.push_back(j-substring.length()+1);
                }
            }
            else if(substring.length() > ptr_copy.length())
            {
                break;
            }
        }
    }
    return ans;
}
```


### [Group anagrams together](https://www.naukri.com/code360/problems/group-anagrams-together_985354?leftPanelTabValue=PROBLEM)

###### [Approach 1](#)

```cpp
#include <bits/stdc++.h> 
vector<vector<string>> groupAnagramsTogether(vector<string> &strList) 
{
    vector<int> stored(strList.size(), -1);
    vector<vector<string>> ans;

    // Using 2 loops to iterate over the strings
    for (int i = 0; i < strList.size(); i++) 
    {
        if (stored[i] == -1) 
        {
            stored[i] = 1;
            vector<string> anagrams;
            anagrams.push_back(strList[i]);

            string parent_copy = strList[i];
            sort(parent_copy.begin(), parent_copy.end());

            for (int j = i + 1; j < strList.size(); j++)
            {  
                string child_copy = strList[j];
                sort(child_copy.begin(), child_copy.end());

                if (child_copy == parent_copy) 
                {
                    // Both are anagrams 
                    anagrams.push_back(strList[j]);
                    stored[j] = 1;
                }
            }
            ans.push_back(anagrams);
        }
    } 
    return ans;  
}
```