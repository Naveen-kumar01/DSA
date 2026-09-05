# Linear search 

def Linear_Search(arr, element):
    if arr is None:
        return False
    for i in arr:
        if element == i:
            return True
    return False

if __name__ == "__main__":
    ar = [1,2,4,5,9,31]
    element = 4
    res = Linear_Search(ar, element)
    print(res)

# Binary Search 

def Binary_search(arr, element):
    left = 0
    right = len(arr)
    mid = (left + right )/2

    while(left < right):
        if arr[mid] == element:
            return mid       # returning the position
        if arr[mid] > element:
            left = mid+1
        if arr[mid] < element:
            right = mid-1
    return -1

if __name__ == "__main__":
    ar = [1,2,4,5,9,31]
    ele = 4
    res = Binary_search(ar, ele)
