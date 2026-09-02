def sort_rotate(arr: list)-> bool:
    count = 0
    n = len(arr)
    if n==1:
        return True 
    for i in range(n):
        if arr[i] > arr[(i+1)%n]:
            count+=1
    if count<=1:
        return True
    else:
        return False

if __name__ == "__main__":
    ar = [3,4,5,1,2]
    res = sort_rotate(ar)
    print(res)