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

                    i += 1
                    while nums[i] == nums[i-1] and i < j:
                        i += 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                twoSum(i, 0 - nums[i])
        return res
                