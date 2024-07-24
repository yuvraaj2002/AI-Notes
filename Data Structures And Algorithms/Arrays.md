This page is dedicated towards understanding the problems related to strings in Data structures and algorithms and here I will be mentioning most commonly asked interview questions along with their solutions.

### [Find the first and last occurrence of a given element in a sorted array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/)
- Go over the vector linearly and when we will encounter the target element for the first time we will store its index as both first and last occurrence and then reverse the Boolean flag which we initialized at the start.
- After that everytime we will encounter the value again we will only update the second occurrence index value

Time complexity is O(n) and space complexity is ~ O(1)
```cpp
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) 
    {
        // Initial configuraion
        vector<int> ans(2);
        ans[0] = -1;
        ans[1] = -1;
        bool first_time = true;

        // Going over array linearly
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i] == target)
            {
                if(first_time == true)
                {
                    // First and last occurence
                    ans[0] = i;
                    ans[1] = i;
                    first_time = false;
                }
                else
                {
                    // Second time occurence (Will get updated again and again)
                    ans[1] = i;
                }
            }
        }
        return ans;
    }
};
```

### [Implement bubble sort, selection sort, and insertion sort](#)
### [Sort an array of 0s, 1s, and 2s](#)
### [Find duplicate elements in an array](#)
### [Find the first repeating element in an array](#)
### [Find the non-repeating element in an array where every other element appears twice](#)
### [Find the pair with a given sum in a sorted array](#)
### [Find the triplet with a given sum in an array](#)
### [Remove duplicates from a sorted array](#)
### [Find the maximum sum subarray of size k](#)
### [Find the longest substring without repeating characters](#)
### [Find the smallest subarray with a sum greater than or equal to a given value](#)
### [Compute the prefix sum array](#)
### [Find the sum of elements in a subarray using the prefix sum array](#)
### [Find the largest sum contiguous subarray (Kadane’s algorithm)](#)
### [Find all possible subarrays or subsequences of an array](#)
### [Check if a given array is a subsequence of another array](#)
### [Rotate an array to the right by k steps](#)
### [Rearrange an array such that all negative numbers appear before all positive numbers](#)
### [Move all zeroes in an array to the end while maintaining the order of non-zero elements](#)
### [Rotate a matrix 90 degrees clockwise](#)
### [Find the diagonal sum of a matrix](#)
### [Find the maximum sum submatrix](#)
