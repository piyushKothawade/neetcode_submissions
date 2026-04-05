class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = list()
        # keep pushing to the stack until you see an operator
        for ch in tokens:
            if not ch in "+-*/":
                st.append(ch)
            else:
                # an operator, retrieve the last 2 elements
                [a, b] = st[-2:]

                # pop the last 2 elements
                st = st[:-2]

                a = int(a)
                b = int(b)

                if ch == '+':
                    st.append(a+b)
                elif ch == '-':
                    st.append(a-b)
                elif ch == '*':
                    st.append(a*b)
                else:
                    st.append(int(a/b))
        return int(st[0])