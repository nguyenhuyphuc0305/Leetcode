# Problem: Get all pair in an array that has sum equal to n
# Approach: Create a set (hash table) to store all elements of the array. That way we can take the one we need out in constant time
# Time complexity: n * 1 = O(n)  ; linear * constant (search an element in set)


def sumPair(arr, sum):
    s = set()
    for i in range(len(arr)):
        temp = sum - arr[i]
        if temp in s:
            print(arr[i], temp)
        s.add(arr[i])

############### TEST ###############
# testArr = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 9]
# sumPair(testArr, 6)
