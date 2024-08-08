This page is dedicated towards understanding the problems related to strings in Data structures and algorithms and here I will be mentioning most commonly asked interview questions related to substrings.

### [Count total palindromic substrings](https://www.naukri.com/code360/problems/palindromic-substrings_630404?topList=top-string-coding-interview-questions&problemListRedirection=true&difficulty%5B%5D=Medium&sort_entity=company_count&sort_order=DESC&leftPanelTabValue=PROBLEM)

###### [Approach 1](#)

- Generate all possible substrings
- During the process of creating them, count substrings of length 1 and length 2 (But for length 2 substring check if it is palindrome or not)
- For other substrings store them in the vector and after wards iterate over them, check them and increment the variable keeping track of count.


```cpp
bool check_palindrome(string st)
{
    int start = 0;
    int end = st.length()-1;

    while(start < end)
    {
        if(st[start] == st[end])
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
int palindromicSubstrings(string input)
{
    // Vector to store all possibe substrings
    vector<string> substrings;
    int ans = 0;

    // Generating all possible substrings
    for(int i=0;i<input.length();i++)
    {
        string substring = "";
        for(int j=i;j<input.length();j++)
        {
            substring = substring + input[j];
            if(substring.length() == 1)
            {
                ans++;
            }
            else if(substring.length() == 2)
            {
                // Compare the first and last index characters
                if(substring[0] == substring[1])
                {
                    ans++;
                }
            }
            else
            {
                substrings.push_back(substring);
            }
        }
    }

    // GOing over the vector
    for(auto it: substrings)
    {
        if(check_palindrome(it) == true)
        {
            ans++;
        }
    }
    return ans;
}
```



### [Find longest palindromic substring](https://www.naukri.com/code360/problems/longest-palindromic-substring_758900?topList=top-string-coding-interview-questions&problemListRedirection=true&difficulty%5B%5D=Medium&sort_entity=company_count&sort_order=DESC)

###### [Approach 1](#)

- Generate all possible substrings 
- Check if the substring is palindrome or not
- If yes then update the ans string


```cpp
bool check_palindrome(string st)
{
    int start = 0;
    int end = st.length()-1;

    while(start < end)
    {
        if(st[start] == st[end])
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

string longestPalinSubstring(string str) 
{
    string ans = "";

    // Generating all possible substrings
    for(int i=0;i<str.length();i++)
    {
        string substring = "";
        for(int j=i;j<str.length();j++)
        {
            substring = substring + str[j];
            if(substring.length() == 1)
            {
                if(substring.length() > ans.length())
                {
                    ans = substring;
                }
            }
            else if(substring.length() == 2)
            {
                // Compare the first and last index characters
                if(substring[0] == substring[1])
                {
                    if(substring.length() > ans.length())
                    {
                        ans = substring;
                    }
                }
            }
            else
            {
                if(check_palindrome(substring) == true)
                {
                    if(substring.length() > ans.length())
                    {
                        ans = substring;
                    }
                }
            }
        }
    }
    return ans;
}
```


### [Find longest substring without repeating characters](https://www.naukri.com/code360/problems/longest-substring-without-repeating-characters_758894?topList=top-string-coding-interview-questions&problemListRedirection=true&difficulty%5B%5D=Medium&sort_entity=company_count&sort_order=DESC)

###### [Approach 1](#)

- Generate all possible substrings 
- Check if the substring is palindrome or not
- If yes then update the ans string

```cpp
#include <bits/stdc++.h> 
int lengthOfLongestSubstring(string &s) 
{
     int ans = 1;

    // Generating all possible substrings
    for(int i=0; i<s.length(); i++)
    {
        string substring = "";
        for(int j=i; j<s.length(); j++)
        {
            substring = substring + s[j];
            if(substring.length() == 1)
            {
                ans = max(ans, (int)substring.length());
            }
            else if(substring.length() == 2)
            {
                // Compare the first and last index characters
                if(substring[0] != substring[1])
                {
                    ans = max(ans, (int)substring.length());
                }
                else
                {
                    break;
                }
            }
            else
            {
                bool found = true;
                // Sorting the substring
                sort(substring.begin(), substring.end());

                // Iterating over the substring
                for(int k=0; k<substring.length()-1; k++)
                {
                    if(substring[k] == substring[k+1])
                    {
                        // Substring contains the repeating characters
                        break;
                    }
                }
                if(found)
                {
                    ans = max(ans, (int)substring.length());
                }
                else
                {
                    break;
                }
            }
        }
    }
    return ans;
}
```


### [Find longest substring with k distinct characters](https://www.naukri.com/code360/problems/distinct-characters_2221410?topList=top-string-coding-interview-questions&problemListRedirection=true&difficulty[]=Medium&sort_entity=company_count&sort_order=DESC)


