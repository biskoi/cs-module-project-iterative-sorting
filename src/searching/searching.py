def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] is target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    lower_bound = 0
    middle = (len(arr) // 2) - 1
    upper_bound = len(arr) - 1
    
    found = False

    while lower_bound <= upper_bound and not found:
        middle = (lower_bound + upper_bound) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            lower_bound = middle
        elif arr[middle] > target:
            upper_bound = middle

    return -1  # not found

arr1 = [1, 2, 3, 4, 5, 6]

print(linear_search(arr1, 4))