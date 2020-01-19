# Problem: Get the most frequent integer in an array
# Approach: Sort the list and count the frequency of each key number
# Time complexity: n*log(n) + n = O(n*log(n))  ; quicksort + linear

from quick_sort import quickSort


def mostFrequent(arr):
    quickSort(arr, 0, len(arr))
    frequency = 1
    freqCheck = 1
    value = arr[0]

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            freqCheck += 1
        else:
            if freqCheck >= frequency:
                frequency = freqCheck
                value = arr[i-1]
                freqCheck = 1

    return [value, frequency]

# Print out every element that appears once


def occurOnce(arr):
    quickSort(arr, 0, len(arr))
    frequency = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            frequency += 1
        else:
            if frequency == 1:
                print(arr[i-1])
            else:
                frequency = 1
            if i == (len(arr) - 1):
                print(arr[i])

############### TEST ###############
# testArr = [1, 2, 3, 4, 4, 5, 6]
# quickSort(testArr, 0, len(testArr))
# print(testArr)
# print(mostFrequent(testArr))
# occurOnce(testArr)
