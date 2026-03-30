class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        imd = str()

        mapping = dict()
        mapping['2'] = "abc"
        mapping['3'] = "def"
        mapping['4'] = "ghi"
        mapping['5'] = "jkl"
        mapping['6'] = "mno"
        mapping['7'] = "pqrs"
        mapping['8'] = "tuv"
        mapping['9'] = "wxyz"

        def solve(i, imd, res, digits):
            if i == len(digits):
                res.append(imd)
                return
            
            options = mapping[digits[i]]
            for char in options:
                imd += char
                solve(i+1, imd, res, digits)
                imd = imd[:-1]
        solve(0, imd, res, digits)
        return res
        
