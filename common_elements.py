def common(arr1, arr2):
    s = set(arr2)
    for k in range(len(arr1)):
        if arr1[k] in s:
            print(arr1[k])


############### TEST ###############
arr1 = [4, 3, 5, 1, 2, 2, 2]
arr2 = [5, 8, 2, 4, 6]
common(arr1, arr2)
