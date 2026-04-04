class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        sortedSet = sorted(set(nums))
        res = 1
        curr = 1
        for i in range(1, len(sortedSet)):
            if sortedSet[i] == sortedSet[i-1] + 1:
                curr += 1
            else:
                res = max(res, curr)
                curr = 1
        res = max(res, curr)
        return res
