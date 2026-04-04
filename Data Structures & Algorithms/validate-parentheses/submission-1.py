class Solution:
    def isValid(self, s: str) -> bool:
        N = len(s)
        st = list()
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                st.append(ch)
            else:
                # look at the top
                topCh = st[-1] if len(st) > 0 else -1
                if topCh == -1:
                    return False
                imdStr = str()
                imdStr = topCh + ch
                if imdStr == "()" or imdStr == "[]" or imdStr == "{}":
                    st.pop()
                else:
                    return False
        if len(st) == 0:
            return True
        return False
        