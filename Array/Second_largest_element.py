def second_largest(arr : list)-> int:
    largest =  -1
    second_largest = -1
    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i < largest:
            second_largest = i
    return second_largest

if __name__ == "__main__":
    r = [3,32,5,6,8,43,13,98, 82]
    sec = second_largest(r)
    print(sec)