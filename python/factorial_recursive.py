def findFactorial(num):
    if num == 1:
        return 1
    else:
        return num * findFactorial(num-1)

print(findFactorial(5))