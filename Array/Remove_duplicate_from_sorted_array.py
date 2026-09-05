"""
Remove Duplicates Sorted Array

You are given a sorted array arr[] containing positive integers. Your task is to remove all duplicate elements from this array such that each element appears only once. Return an array containing these distinct elements in the same order as they appeared.
Examples :

Input: arr[] = [2, 2, 2, 2, 2]
Output: [2]
Explanation: After removing all the duplicates only one instance of 2 will remain i.e. [2] so modified array will contains 2 at first position and you should return array containing [2] after modifying the array.

Input: arr[] = [1, 2, 4]
Output: [1, 2, 4]
Explation:  As the array does not contain any duplicates so you should return [1, 2, 4].

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 106

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

def remove_duplicate(arr):
    if arr is None:
        return []
    k_pos=1
    for i in range(1, len(arr)):
        if arr[i] != arr[k_pos-1]:
            arr[k_pos] = arr[i]
            k_pos+=1
    return arr[:k_pos] # if you want to return the unique array elements
    #return k_pos      # if you want to return only number of unique elements.

if __name__ == "__main__":
    ar = [0,0,0,1,1,4,5,5]
    res = remove_duplicate(ar)
    print(res)

# note if we perform this in the unsorted array then there are 2 type of solution - 
# 1. use set to store unique element but in this case space complexity will become O(n)
# 2. sort the array and then use similar method as above in this space complexity remains same O(1)