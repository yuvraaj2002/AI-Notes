### [Find the Next greater element](https://leetcode.com/problems/next-greater-element-ii/description/)

To solve this problem there are couple of approaches and we will discuss each of the approach in the systematic manner. Similar to this there will be find next smaller element and for that we will be iterating from the start rather than back to keep track of smaller elements. Here is problem link for that as well [Next smaller element](https://www.interviewbit.com/problems/nearest-smaller-element/)

##### Approach 1 (Using 2 loops)

- Since it is given that the array is circular in nature so we can think of replicating the array to make it behave like circular array
- After that we will be using 2 loops to find the next greater element 
- Also note that once we will reach the index =  size or more than that, we will manipulate the index to get the value.

Time complexity $O(n^2)$ and extra space complexity O(1)
```cpp
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) 
    {
        // Initial configuration
        vector<int> ans(nums.size(), -1);

        for(int i=0;i<nums.size();i++)
        {
            int curr_value = nums[i];
            for(int j=i+1;j<2*nums.size();j++)
            {
                int value = nums[j%nums.size()];
                if(value > curr_value)
                {
                    ans[i] = value;
                    break;
                }
            }
        }
        return ans;
    }
};
```


##### Approach 2 (Using Stack)

- Start iterating from the back of the hypothetical double size array
- Till the time our current index is equal to size or more than that, we will be storing the values of this hypothetical array to utilize later
- Otherwise once we will come under original array index, we will be using the stack value to find the next greater element

Time complexity O(n) and extra space complexity O(n)
```cpp
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) 
    {
        int size = nums.size();
        int total_size = nums.size()*2;
        vector<int> ans(size);
        stack<int> st;
        
        for(int i = total_size-1; i >=0;i--)
        {
            int curr_value = nums[i%size];
            if(i >= nums.size())
            {
                // Storing hypothetical for usage later 
                st.push(curr_value);
            }
            else
            {
                // Clear the clutter
                while(!st.empty() && st.top()<= curr_value)
                {
                    st.pop();
                }
                if(st.empty())
                {
                    ans[i] = -1;
                }
                else
                {
                    ans[i] = st.top();
                }
                st.push(curr_value);
            }
        }
        return ans;
    }
};
```


### [Daily Temperature](https://leetcode.com/problems/daily-temperatures/description/)

- Initialize a stack of pair to store the index and value
- Start moving from the end because standing at current day we need to have access to all the future days and also in the most recent fashion
- Standing at current index if we found temperature warmer then find the difference in the indexes
```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) 
    {
        // Initial configuration
        stack<pair<int, int>> st;
        vector<int> ans(temperatures.size(), 0);
        
        // Going from the end
        for (int i = temperatures.size() - 1; i >= 0; i--)
        {
            int curr_temp = temperatures[i];
            
            // Filtering
            while (!st.empty() && st.top().first <= curr_temp)
            {
                st.pop();
            }
            
            if (!st.empty())
            {
                ans[i] = st.top().second - i;
            }
            
            st.push({curr_temp, i});
        }
        return ans;
    }
};
```


### [Trapping Rainwater](https://leetcode.com/problems/trapping-rain-water/description/)

- First and last elevation map will not store any water
- At current index find greatest than current elevation map on left and right
- If not found then it becomes itself only
- Out of 2 the smallest one (will be maximum) - current elevation map
- Here we have used the simple variable to find the next greater element on left and right but we can also use the stack data structure

Time complexity O(n) + O(n) ~ O(n) and extra space complexity O(2n) ~ O(n)
```cpp
class Solution {
public:
    int trap(vector<int>& height) 
    {
        // Initial configuration
        int total_volume = 0;
        int gl = INT_MIN;
        int gr = INT_MIN;
        vector<int> gl_value(height.size());
        vector<int> gr_value(height.size());

        // Finding the greatest element on the left
        for(int i=0;i<height.size();i++)
        {
            int curr_elevation_left  = height[i];
            int curr_elevation_right  = height[height.size()-1-i];

            // Doing the updation for greater on left and right
            gl_value[i] = max(gl,curr_elevation_left);
            gl = max(gl,curr_elevation_left);

            gr_value[height.size()-1-i] = max(gr,curr_elevation_right);
            gr = max(gr,curr_elevation_right);
        }

        // Iterating the elevation maps
        for(int i=0;i<height.size();i++)
        {
            int curr_elevation = height[i];
            int gleft = gl_value[i];
            int gright = gr_value[i];

            total_volume = total_volume + min(gleft,gright)-curr_elevation;
        }
        return total_volume;
    }
};
```