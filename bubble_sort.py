def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp


def BubbleSort(A):
    # i is like numbers of element that has been sorted from bottom up, starting from 0
    for i in range(len(A)):
        # j record the current index
        for j in range(len(A) - 1 - i):
            if A[j] > A[j+1]:
                swap(A, j, j+1)


############### TEST ###############
a = [7, 9, 3, 18, 8]
BubbleSort(a)
print(a)
