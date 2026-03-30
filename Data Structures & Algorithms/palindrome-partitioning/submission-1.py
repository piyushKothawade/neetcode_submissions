class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        startIndices = [0]
        res = []
        def isPali(s: str) -> bool:
            return s == s[::-1]

        def solve(i):
            if i == N:
                # where was my last Cut?
                if startIndices[-1] == N:
                    endIndices = startIndices[1:]
                    ans = [s[start:end] for start, end in zip(startIndices[:-1], endIndices)]
                    res.append(ans)
                return
            startInd = startIndices[-1]
            substr = s[startInd:i+1]
            if isPali(substr):
                startIndices.append(i+1)
                solve(i+1)
                startIndices.pop()
            solve(i+1)
        solve(0)
        return res

        