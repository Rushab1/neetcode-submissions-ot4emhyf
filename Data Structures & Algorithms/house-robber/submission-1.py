class Solution:
    def rob(self, nums: List[int]) -> int:
        # only depends on previous house was robbed or not.
        # ri = max robbery in house [0:i], if i is definitely robbed. 
        # ti = max robbery in house [0:i] (regardless of whether i is robebd or not)
        # ri = t(i-2) + nums[i]
        # ti = max(ri, ri-1)
        n = len(nums)

        if n < 2:
            return max(nums)
        r = [nums[0], nums[1]]
        t = [nums[0], max(r)]

        for i in range(2, n):
            _r = t[0] + nums[i]
            _t = max(_r, r[1])

            r = [r[1], _r]
            t = [t[1], _t]

        return t[1]