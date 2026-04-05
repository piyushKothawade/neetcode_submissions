class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # START from the backwards
        N = len(temperatures)
        st = list()
        res = [0]*N

        # store the prospects for the NGE in the stack
        # Compare each element (i.e. the current element) with the prospects until 
        # you get one
        for i in range(N-1, -1, -1):
            if i == N-1:
                res[i] = 0
            else:
                while len(st) and st[-1][0] <= temperatures[i]:
                    st.pop();
                if len(st):
                    res[i] = st[-1][1] - i
                else:
                    res[i] = 0
            st.append((temperatures[i], i))  
        return res