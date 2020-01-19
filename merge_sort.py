# Merge Sort devides a list into 2 halves, recursively sorts each half and merges the sorted halves into one to creat ea sorted list
def mergeSort(arr, low, high):
    if (low < high):
        mid = (low + high) // 2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)

        merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    arr1 = arr[low:mid+1]
    arr2 = arr[mid+1:high+1]
    i, k = 0, 0
    while (i < len(arr1)) and (k < len(arr2)):
        if arr1[i] < arr2[k]:
            arr[low+i+k] = arr1[i]
            i += 1
        else:
            arr[low+i+k] = arr2[k]
            k += 1

    if i == len(arr1):
        arr[low+i+k:high+1] = arr2[k:]
    elif k == len(arr2):
        arr[low+i+k:high+1] = arr1[i:]


############### TEST ###############
arr = [36, 2, 27, 30, 36, 0]
mergeSort(arr, 0, 5)
print(arr)
