class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[-1]
        def solve(i, temp):
            if i >= len(temp):
                return 0
            
            if dp[i] != -1:
                return dp[i]
                
            # rob the current house
            rob = temp[i] + solve(i+2, temp)

            # don't rob
            dontRob = solve(i+1, temp)

            dp[i] = max(rob, dontRob)
            return dp[i]

        # create 2 house lists
        temp1, temp2 = nums[:-1], nums[1:]

        dp = [-1]*N
        ans1 = solve(0, temp1)

        dp[:] = [-1]*N
        ans2 = solve(0, temp2)

        return max(ans1, ans2)

        