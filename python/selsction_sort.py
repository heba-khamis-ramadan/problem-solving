def findSmallest(arr: list[int]):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index

def selectionSort(arr: list[int]):
    new_arr = []
    copied_arr = list(arr)
    for i in range(len(copied_arr)):
        smallest = findSmallest(copied_arr)
        new_arr.append(copied_arr.pop(smallest))
    
    return new_arr


print(findSmallest([5,11,8,3,9]))
print(selectionSort([5,11,8,3,9]))