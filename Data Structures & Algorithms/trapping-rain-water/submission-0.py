
        #1. if the difference in heights betwen i and j is negative move both of them by an increment of 1. 
# 2. if the difference is positive we should move the j value by 1 and continue and then see, if it results in a negative height, then add the current amoutn of area, to the curr_area which is 0 intiall , and then move both i and j incremented by 1. 
#3. if the height [i] - height[j] is 0 at any point then set i index to where j is currently and then add that current area to the curr_area. 
# You would although have to run this from both sides to make this work and check. 
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res