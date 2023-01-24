def twoSum( nums, target):
    a = {}
    for i in range(len(nums)):
        if (target - nums[i]) in a:
            return [a[target - nums[i]], i]
        else:
            a[nums[i]] = i


arr = [3,2,4]

print(twoSum(arr, 6))



