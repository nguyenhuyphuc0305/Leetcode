def search(nums, target):
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

    def findShift(nums):
        low = 0
        high = len(nums) - 1
        while high - low != 1:
            mid = (low + high) // 2
            if (nums[mid] > nums[low]) and (nums[mid] > nums[high]):
                low = mid
            elif (nums[mid] < nums[low]) and (nums[mid] < nums[high]):
                high = mid
            elif (nums[mid] > nums[low]) and (nums[mid] < nums[high]):
                return low

        if nums[high] > nums[low]:
            return low
        else:
            return low + 1

    if len(nums) == 0:
        return -1
    elif len(nums) == 1:
        if target == nums[0]:
            return 0
        else:
            return -1

    shiftPoint = findShift(nums)
    newArray = nums[shiftPoint:] + nums[:shiftPoint]

    res = binSearch(newArray, 0, len(newArray) - 1, target)

    if res == -1:
        return -1
    elif (res + shiftPoint) >= len(nums):
        return (res + shiftPoint - len(nums))
    else:
        return (res + shiftPoint)


############### TEST ###############
a = [7, 8, 1, 2, 3, 4]
print(search(a, 3))
