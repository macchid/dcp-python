# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# Put all negative numbers to the left
def segregate(arr):
    print(arr)
    size = len(arr)
    j = 0
    for i in range(size):
        if arr[i] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return j


def find_missing_positive(arr):
    print(arr)
    for i in arr:
        print(i)
        if abs(i)-1 < len(arr) and abs(i) > 0:
            arr[abs(i)-1] = -abs(arr[abs(i) - 1])

    print(arr)
    for i, n in enumerate(arr):
        if n > 0:
            return i + 1

    return len(arr) + 1

def find_missing(arr):
    shift = segregate(arr)
    print(find_missing_positive(arr[shift:]))


find_missing([3,2,2,3,-1,1])