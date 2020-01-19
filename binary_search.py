from rotated_array import isRotated


def binSearch(arr, low, high, target):
    mid = (low + high) // 2
    if low > high:
        return -1
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binSearch(arr, low, mid-1, target)
    else:
        return binSearch(arr, mid+1, high, target)

# Find an integer in rotated array


def rotatedBinSearch(arr, target):
    if isRotated(arr):
        lowestIndex = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                lowestIndex = i
                break
        left = binSearch(arr, 0, lowestIndex-1, target)
        right = binSearch(arr, lowestIndex, len(arr)-1, target)

        if left != -1:
            return left
        elif right != -1:
            return right
        else:
            return -1


############### TEST ###############
# testArr = [5, 6, 7, 1, 2, 3]
# print(rotatedBinSearch(testArr, 8))
