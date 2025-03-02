def quickSort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []
        for i in arr[1:]:
            if i <= pivot:
                less.append(i)
            if i > pivot:
                greater.append(i)
        return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([7, 2, 11, 1, 5]))

