class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        st = list()
        for i in range(len(position)):
            pair.append([position[i], speed[i]])
        pair.sort()

        st.append(pair[-1])
        # RELATIVE positions won't change
        for i in range(len(position)-2, -1, -1):
            # compare the current car to the previous car carFleet
            time1 = (target - st[-1][0]) / st[-1][1]
            time2 = (target - pair[i][0]) / pair[i][1]

            if time2 <= time1:
                # these would intersect
                continue
            else:
                st.append(pair[i])
        return len(st)