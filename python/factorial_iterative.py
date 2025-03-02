def findFactorial(num):
    fact = 1
    while num >= 1:
        fact  *= num
        num -= 1
    return fact

print(findFactorial(5))