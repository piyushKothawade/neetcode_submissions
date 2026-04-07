class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) - 1
        def isAlphanumeric(s):
            # s is a character
            if s >= 'a'and s <= 'z':
                return True
            if s >= 'A' and s <= 'Z':
                return True
            if s >= '0' and s <= '9':
                return True
            return False
        while i < j:
            # move 'i' to the next alpha-numeric character
            while(i < len(s) and not isAlphanumeric(s[i])):
                i += 1
            if i == len(s): 
                return True
            while(not isAlphanumeric(s[j])):
                j -= 1
            print(i,j)
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True