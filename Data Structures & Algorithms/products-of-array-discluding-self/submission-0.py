class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ret = [nums[0]]
        for n in nums[1:]:
            ret.append(ret[-1] * n)
        
        curr = 1
        for i in range(len(nums)-1, 0 , -1):
            ret[i] = ret[i-1] * curr
            curr *= nums[i]

        ret[0] = curr
        return ret