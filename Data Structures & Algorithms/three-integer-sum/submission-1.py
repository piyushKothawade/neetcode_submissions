class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def twoSum(k, target):
            # the two numbers should add up to target
            i, j = k + 1, len(nums) - 1
            while (i < j):
                if nums[i] + nums[j] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    while i < len(nums) - 1 and nums[i] == nums[i+1]:
                        i += 1
                    while j > 0 and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                print('Hi')
                twoSum(i, 0 - nums[i])
        return res
                