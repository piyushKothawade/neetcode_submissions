class Solution:
    def numDecodings(self, s: str) -> int:
        charMap = {str(i - 64): chr(i) for i in range(65, 91)}

        lastIdx = 0 # stores the starting Indices of the different substrings
        dp = dict()
        # put cuts in the original string
        def solve(i, lastIdx):
            if lastIdx - i + 1 >= 3:
                return 0
                
            if i == len(s):
                if lastIdx == len(s):
                    return 1
                return 0
            
            # memo
            if (i, lastIdx) in dp:
                return dp[(i, lastIdx)]

            # I put a cut here
            # need to check if it is in the charMap
            ans1 = 0
            startIdx = lastIdx
            substr = s[startIdx:i+1]
            if substr in charMap:
                # I can make a cut here
                lastIdx = i + 1
                ans1 = solve(i+1, lastIdx)
                lastIdx = startIdx
            
            # don't make a cut here
            ans2 = solve(i+1, lastIdx)
            dp[(i, lastIdx)] = ans1 + ans2
            return dp[(i, lastIdx)]
        return solve(0, lastIdx)