# Take an array, swap 2 elements at index pos1 and pos2
def swap(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]

# Recursively sort the left and right part of the pivot


def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)

# Return the right position for the pivot


def partition(arr, low, high):
    # lowerNum increments for the numbers of element smaller than the pivot (low)
    lowerNum = low

    for i in range(low+1, high+1):
        if arr[i] < arr[low]:
            lowerNum += 1
            swap(arr, i, lowerNum)
    swap(arr, low, lowerNum)
    return lowerNum
