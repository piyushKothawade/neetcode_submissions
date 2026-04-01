class Solution:
    def countSubstrings(self, s: str) -> int:
        # consider every character of 's' as the center of 
        # even-lengthed and odd=lengthed substrings and count
        res = 0

        for i in range(len(s)):
            # odd lengthed substrings
            j, k = i, i
            while (j >= 0 and k < len(s) and s[j] == s[k]):
                res += 1
                j -= 1
                k += 1
            # even lengthed substrings
            if not (i == len(s) - 1):
                j, k = i, i + 1
                while (j >= 0 and k < len(s) and s[j] == s[k]):
                    res += 1
                    j -= 1
                    k += 1
        return res
