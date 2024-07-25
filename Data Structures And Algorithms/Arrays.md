This page is dedicated towards understanding the problems related to strings in Data structures and algorithms and here I will be mentioning most commonly asked interview questions along with their solutions. Rather than doing questions randomly we will be focusing on the important subtopics. And the various subtopics which we will consider in array are 

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

### [Implement All Sorting algorithms](#)
### [Sort an array of 0s, 1s, and 2s](#)
### [Find duplicate elements in an array](https://leetcode.com/problems/find-the-duplicate-number/)

To solve this problem there are couple of approaches and we will discuss each of the approach in the systematic manner.

##### Approach 1 (Using set)
- Initialize set data structure
- Start going over the vector values
- If current value is unique and first time visited then push in the set otherwise break the loop

Time complexity is O(n) and space complexity is O(n)
```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) 
    {
        // Sort the values
        set<int> st;
        int ans = -1;

        for(int i=0;i<nums.size();i++)
        {
            if(st.find(nums[i]) != st.end())
            {
                ans = nums[i];
                break;
            }
            else
            {
                st.insert(nums[i]);
            }
        }
        return ans;
    }
};
```

##### Approach 2 (Using Sorting)
- Sort the vector 
- Start from index 0 and go till last index-1
- Check if current index value is same as next index value
	- If so then return this index value as repeating value
	- Otherwise move further

Time complexity is O(n) and space complexity is O(n)
```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) 
    {
        // Sort the values
        sort(nums.begin(),nums.end());
        int ans = -1;

        for(int i=0;i<nums.size()-1;i++)
        {
            if(nums[i] == nums[i+1])
            {
                ans = nums[i];
                break;
            }
        }
        return ans;
    }
};
```


### [Find the non-repeating element in an array where every other element appears twice](https://leetcode.com/problems/single-number-iii/)

- Initialize a map data structure and go over the vector and keep track of frequency count
- If the items frequency count is 1 then store it in the answer vector

Time complexity is O(n) and space complexity is O(n)
```cpp
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) 
    {
        vector<int> ans;
        unordered_map<int,int> mp;
        for(auto it: nums)
        {
            // Incrementing the frequency count
            mp[it]++;
        }

        // Going over the map
        for(auto it: mp)
        {
            if(it.second == 1)
            {
                ans.push_back(it.first);
            }
        }
        return ans;
    }
};
```
### [Find the pair with a given sum in a sorted array](https://leetcode.com/problems/two-sum/description/)

To solve this problem there are couple of approaches and we will discuss each of the approach in the systematic manner.

##### Approach 1 (Using 2 loops)

- Use one loop focusing on current item
- Use another inner loop to find the other value to form total sum =  target

Time Complexity $O(n^2)$ and Space complexity O(1)
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        vector<int> ans;
        for(int i =0 ; i <nums.size()-1;i++)
        {
            for(int j = i+1; j<nums.size();j++)
            {
                if(nums[i]+nums[j] == target)
                {
                    ans.push_back(i);
                    ans.push_back(j);
                }
            }
        }
        return ans;
    }
};
```

##### Approach 2 (Using Map)

- Initialize a map data structure
- Start going over the vector and compute value to find
- In case the value to find doesn't exist in the vector then store it in map data structure with value : index format
- If the value exist then check whether it is having different index then current value or not

Time Complexity O(n) and Space complexity O(n)
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        // Using map data structure
        map<int,int> mp;

        vector<int> ans;
        for(int i=0;i<nums.size();i++)
        {
            int value_to_find = target-nums[i];
            if(mp.find(value_to_find) != mp.end())
            {
                // Make sure we are not choosing same value twice
                if(i != mp[value_to_find]) 
                {
                    ans.push_back(i);
                    ans.push_back(mp[value_to_find]);
                    break;
                } 
            }
            else
            {
                mp[nums[i]] = i;
            }
        }
        return ans;
    }
};
```

##### Approach 3 (2 Pointers)

- Initialize 2 pointers called start and end
- Use condition that while start < end 
	- Check if the current sum = target (if so then return start and end value)
	- If current sum > target , then decrement end
	- If current sum < target, then increment start

Time Complexity O(n) and Space complexity O(1)
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        // Initial configuration
        int start = 0;
        int end = nums.size()-1;
        vector<int> ans(2);

        // Sorting 
        sort(nums.begin(),nums.end());

        while(start < end)
        {
            int curr_sum = nums[start] + nums[end];
            if(curr_sum == target)
            {
                ans[0] = start;
                ans[1] = end;
                break;
            }
            else
            {
                if(curr_sum > target)
                {
                    end--;
                }
                else
                {
                    start++;
                }
            }
        }
        return ans;
    }
};
```

### [Find the triplet with a given sum in an array](https://www.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card)

To solve this problem there are couple of approaches and we will discuss each of the approach in the systematic manner.
##### Approach 1 (Using 3 loops)
- Use first loop to select the first value
- Use the second and third nested loops to go over the internal values
- If the sum = target then stop the loops and return true else continue

Time complexity $O(n^3)$ and space complexity O(1)
```cpp
class Solution {
  public:

    // Should return true if there exists a triplet in the
    // array arr[] which sums to x. Otherwise false
    bool find3Numbers(int arr[], int n, int x) 
    {
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                for(int k=j+1;k<n;k++)
                {
                    if(arr[i] + arr[j] + arr[k] == x)
                    {
                        return true;
                    }
                }
            }
        }
        return false;
    }
};
```
### [Remove duplicates from a sorted array](#)


### [Find the maximum sum subarray of size k](https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1)

- Initialize 2 pointers head and tail
- Expand the window to the required length and add up the values
- Then move the window to the right by adding new item and removing old item

Time Complexity O(n) and space complexity O(1)
```cpp
class Solution{   
public:
    long maximumSumSubarray(int K, vector<int> &Arr , int N)
    {
        // code here 
        int head = 0;
        int tail = 0;
        long max_sum = LONG_MIN; 
        long curr_sum = 0;
        
        
        // Expanding the window
        while ((head - tail + 1) <= K) 
        {
            curr_sum = curr_sum + Arr[head];
            
            if ((head - tail + 1) == K) 
            {
                break;
            } 
            else 
            {
                head++;
            }
        }
        
        // We have the window at hand
        max_sum = max(max_sum, curr_sum);
        
        // Moving right
        while (head < N - 1) 
        {
            // Adding new item
            head++;
            curr_sum = curr_sum + Arr[head];
            
            // Removing old item
            curr_sum = curr_sum - Arr[tail];
            tail++;
            
            // Updating the maximum sum
            max_sum = max(max_sum, curr_sum);
        }
        return max_sum;
    }
};
```
### [Find the longest substring without repeating characters](#)
### [Find the smallest subarray with a sum greater than or equal to a given value](https://leetcode.com/problems/minimum-size-subarray-sum/)

##### Approach 1 (Generating all the possible subarrays using 2 loops)

- Generate all the possible subarrays using 2 loops
- If the subarray sum >= target then find the length using (j-i)+1
- Update the ans variable that is storing the length of the subarray

Time complexity $O(n^2)$ and space complexity O(1)
```cpp
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) 
    {
        // Initial configuration
        int ans = INT_MAX;;

        for(int i=0;i<nums.size();i++)
        {
            int sub_sum = 0;
            for(int j=i;j<nums.size();j++)
            {
                sub_sum = sub_sum + nums[j];
                if(sub_sum >= target)
                {
                    int length = (j-i)+1;
                    ans = min(ans,length);
                    break;
                }
            }
        }
        if(ans == INT_MAX)
        {
            return 0;
        }
        return ans;
    }
};
```

##### Approach 2 (Using the 2 pointers)

```Cpp
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        // Initial configuration
        int ans = INT_MAX;
        int head = 0;
        int tail = 0;
        int sub_sum = 0;

        while (tail < nums.size()) 
        {
            // Adding item to the current sum
            sub_sum += nums[tail];

            // Minimize window if the current sum is greater than or equal to the target
            while (sub_sum >= target) 
            {
                ans = min(ans, (tail - head) + 1);
                sub_sum -= nums[head];
                head++;
            }
            
            // Move the tail pointer to the right
            tail++;
        }
        
        return (ans == INT_MAX) ? 0 : ans;
    }
};

```


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
