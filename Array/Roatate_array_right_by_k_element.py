"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

# Solution 1 Right rotate  : time complexity - O(n) , Space complexity - O(1) - Best 
# First reverse entire array, 
# Then reverse first K elements in array,
# Then reverse last K elements in array.
def rotate_right_array(arr, k):
    n = len(arr)
    k %= n

    def reverse(left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

    return arr


if __name__ == "__main__":
    ar = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    res = rotate_right_array(ar, k)
    print(res)

# Solution 2 Left rotate  : time complexity - O(n) , Space complexity - O(1) - Best 
# , 
# reverse first K elements in array,
# Then reverse last K elements in array.
# Then reverse entire array

def rotate_left_array(arr, k):
    n = len(arr)
    k = k % n

    def reverse(left, right):
        while (left < right):
            arr[left], arr[right]= arr[right], arr[left]
            left+=1
            right-=1

    reverse(0, k-1)
    reverse(k, n-1)
    reverse(0, n-1)

    return arr

if __name__ == "__main__":
    ar = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    res = rotate_left_array(ar, k)
    print(res)