class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        dp = dict()

        coins.sort()
        coins = coins[::-1]
        
        def solve(i, target):
            if target == 0:
                return 0
            if i == N:
                return 10**9
            
            if (i, target) in dp:
                return dp[(i, target)]
            
            # use the current denomination
            # can only use if the target is >= coins[i]
            ans1 = 1e9
            if coins[i] <= target:
                ans1 = 1 + solve(i, target - coins[i])
            
            # proceed to the next denomination
            ans2 = solve(i+1, target)
            dp[(i, target)] = min(ans1, ans2)
            return dp[(i, target)]

        res = solve(0, amount)
        return res if res < 10**9 else -1