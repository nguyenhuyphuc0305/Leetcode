# Problem: Get nth element of Fibbonaci
# Approach: Dynamic Programming (or Enhanced Recursive) : store the variable in the an array to eliminate extra calculation

import math
# Regular Recursive: Time complexity T(n) = T(n-1) + T(n-2) = .... -> exponential since we have to run so many fibbonaci function


def fibbonaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibbonaci(n-1) + fibbonaci(n-2)


# Dynamic Programming approach: by storing each step of iteration in an array, we avoid extra steps
fibbonArr = [0, 1]


def dynamicFibbo(n):
    # extend the array to have n length
    for _ in range(len(fibbonArr), n+1):
        fibbonArr.append(0)
    if n <= 1:
        return fibbonArr[n]
    else:
        if fibbonArr[n-1] == 0:
            fibbonArr[n-1] = dynamicFibbo(n-1)
        if fibbonArr[n-2] == 0:
            fibbonArr[n-2] = dynamicFibbo(n-2)
        fibbonArr[n] = fibbonArr[n-1] + fibbonArr[n-2]
    return fibbonArr[n]


############### TEST ###############
print(dynamicFibbo(8))
