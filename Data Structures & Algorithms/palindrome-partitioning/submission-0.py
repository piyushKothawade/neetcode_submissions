class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        startIndices = [0]
        res = []
        startIndex = 0
        def isPalindrome(s: str) -> bool:
            return s == s[::-1]

        def solve (i, startIndex, startIndices):
            # print(i)
            if i == N:
                # CHECK the last substring
                lastIndex = startIndices[-1]
                if lastIndex == N:
                    # this is a successful sequence
                    endIndices = startIndices[1:-1] + [N]
                    ans = [s[start:end] for start, end in zip(startIndices, endIndices)]
                    res.append(ans)
                return


            # should I split here?
            # must be a palindrome till now
            str = s[startIndices[-1]:i+1]
            temp = startIndex
            lenSI = len(startIndices)
            if isPalindrome(str):
                # I can split!
                startIndex = i+1
                startIndices.append(startIndex)
                solve(i+1, startIndex, startIndices)
            # I don't want to, I can't!
            # reset the value of startIndex
            startIndex = temp
            # only pop if the string could have got splitted before
            if not lenSI == len(startIndices):
                startIndices.pop()
            solve(i+1, startIndex, startIndices)

            return
        solve(0, startIndex, startIndices)
        return res

        