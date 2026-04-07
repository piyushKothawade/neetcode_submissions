class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            # keep the current index as the height of the largestRectangle
            height = heights[i]
            l, r = i, i
            while l - 1 >= 0 and heights[l - 1] >= height:
                l -= 1
            while r + 1 < len(heights) and heights[r + 1] >= height:
                r += 1
            res = max(res, height * (r - l + 1))
        return res