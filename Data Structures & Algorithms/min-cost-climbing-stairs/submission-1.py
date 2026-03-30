class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [-1]*N
        def solve(i):
            if i == N:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            # take 1 step
            oneStep = cost[i] + solve(i+1)

            twoSteps = 10**6
            # take 2 steps
            if not (i == N-1):
                twoSteps = cost[i] + solve(i+2)
            dp[i] = min(oneStep, twoSteps)
            return dp[i]
        choice1 = solve(0)
        choice2 = solve(1)
        return min(choice1, choice2)