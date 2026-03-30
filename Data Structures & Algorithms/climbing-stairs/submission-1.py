class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        def solve(i):
            if i == 0:
                return 1

            if not (dp[i] == -1):
                return dp[i]
            # Climb 1 stair
            climb1 = solve(i-1)

            # Climb 2 stairs
            climb2 = 0
            if i >= 2:
                climb2 = solve(i-2)
            dp[i] = climb1 + climb2
            return dp[i]
        return solve(n)
        