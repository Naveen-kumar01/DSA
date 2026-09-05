"""
Move all Zeros to End of Array

Given an array of integers arr[], move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.

Examples: 

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.

Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.

Input: arr[] = [0, 0]
Output: [0, 0]
Explanation: No change in array as there are all 0s.
"""

def move_zeroes(arr):
    non_zero = 0
    for i in range(len(arr)):
        if arr[i] !=0:
            arr[non_zero], arr[i] = arr[i], arr[non_zero]
            non_zero+=1
    return arr

if __name__ == "__main__":
    ar = [1, 2, 0, 4, 3, 0, 5, 0]
    res = move_zeroes(ar)
    print(res)