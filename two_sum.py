def twoSum(nums, target):
    numDict = {}
    for i in range(len(nums)):
        if nums[i] not in numDict:
            numDict[nums[i]] = [i]
        else:
            numDict[nums[i]].append(i)

    for i in range(len(nums)):
        if nums[i] == target - nums[i]:
            try:
                return [numDict[nums[i]][0], numDict[nums[i]][1]]
            except:
                return []
        elif (target - nums[i]) in numDict:
            return [i, numDict[target-nums[i]][0]]
        else:
            return []


a = [3, 3]

print(twoSum(a, 6))
