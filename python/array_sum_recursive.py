def arraySum(arr):
    if len(arr) == 0:
        return 0
    else:
        n = arr.pop()
        return n + arraySum(arr)

print(arraySum([5, 4, 1]))