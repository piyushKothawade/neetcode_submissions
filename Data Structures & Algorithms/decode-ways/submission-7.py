class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case: If the string starts with '0', it can't be decoded
        if not s or s[0] == '0':
            return 0
            
        dp = {}

        def solve(i):
            # Base case: We successfully reached the end of the string
            if i == len(s):
                return 1
            
            # Base case: A string starting with '0' is invalid
            if s[i] == '0':
                return 0

            # Return memoized result if we've been here before
            if i in dp:
                return dp[i]

            # Choice 1: Decode 1 character (We already know it's not '0')
            ans = solve(i + 1)

            # Choice 2: Decode 2 characters (Check if it's between 10 and 26)
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                ans += solve(i + 2)

            dp[i] = ans
            return dp[i]

        return solve(0)