# Problem: check if an array is rotated or not
# Approach: Find the smallest element of the array, check if both left side and right side are increasing order or not
#           Also have to make sure last element is smaller than the element before lowestIndex since [2,3,1,4,5] is not rotated

# Reverse an array, it has nothing to do with problem. I just create it for fun


def reverseArr(arr, low, high):
    while low < high:
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp
        low += 1
        high -= 1


def isRotated(arr):
    lowIndex = 0
    # Find the index of the smallest element
    for i in range(len(arr)):
        if arr[i] < arr[lowIndex]:
            lowIndex = i
    # If given arr is sorted, it is not count as rotated
    sorted = True
    for i in range(len(arr)-2):
        if arr[i] > arr[i+1]:
            sorted = False
            break
    if sorted:
        return False
    # Compare last element with element before lowest index
    if arr[len(arr)-1] > arr[lowIndex-1]:
        return False

    left, right = True, True
    # Check if before lowest is sorted
    for i in range(1, lowIndex):
        if arr[i] < arr[i-1]:
            left = False
            break
    # Check if after lowest is sorted
    for i in range(lowIndex+1, len(arr)):
        if arr[i] < arr[i-1]:
            right = False
            break
    return (left and right)


############### TEST ###############
# testArr = [1, 2, 3]
# print(isRotated(testArr))
# print(testArr)
