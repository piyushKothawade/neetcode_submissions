class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [-1]*N

        def solve(i):
            if i >= N:
                return 0
            
            if dp[i] != -1:
                return dp[i]
                
            # rob the current house
            rob = nums[i] + solve(i+2)

            # don't rob
            dontRob = solve(i+1)

            dp[i] = max(rob, dontRob)
            return dp[i]
        return solve(0)