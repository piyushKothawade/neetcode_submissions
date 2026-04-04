class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        setNums = set(nums)
        res = 1
        for i in range(len(nums)):
            if nums[i] - 1 in setNums:
                continue
            else:
                curr = 0
                # it's the first number in the sequence
                currNum = nums[i]
                while(nums[i] in setNums):
                    curr += 1
                    nums[i] += 1
                res = max(res, curr)
        return res
                
        # for i in range(1, len(sortedSet)):
        #     if sortedSet[i] == sortedSet[i-1] + 1:
        #         curr += 1
        #     else:
        #         res = max(res, curr)
        #         curr = 1
        # res = max(res, curr)
        return res
