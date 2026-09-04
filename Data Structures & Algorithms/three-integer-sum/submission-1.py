class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break # if the index is greater than 0 then we are fine 

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1 # just should consider the right side of i. 
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
        # i get why we only consider the right of i, we are essentially trying every pair to teh right of i right, and then we obviosuly going through teh same two pointer approach to figure out the vlaues to sum, 

        