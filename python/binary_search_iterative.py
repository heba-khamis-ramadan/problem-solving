def binarySearch(arr: list[int], target: int):
    low = 0
    high = len(arr)-1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 5
 
# Function call
result = binarySearch(arr, x)
print(result)   