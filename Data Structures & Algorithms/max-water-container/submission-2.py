class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
        # okay im happy with this approach its what i thought of as well, but i was just confused on how to move teh pointers, yh sure i mean i guess just move based on heights, even if current area less it doesnt matter, since we have curr_max