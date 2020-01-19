def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

# Insertion sort treats array input as 2 parts: sorted part on the left and unsorted on the right. We insert each on on the
# right to the correct order on the left


def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while (j > 0):
            if arr[j] < arr[j-1]:
                swap(arr, j, j-1)
            j -= 1
        # print(arr)


############### TEST ###############
a = [7, 9, 3, 18, 8]
insertionSort(a)
print(a)
