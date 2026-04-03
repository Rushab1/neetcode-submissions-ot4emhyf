class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max = -math.inf
        curr_max = -math.inf

        for num in nums:
            curr_max = max(curr_max + num, num)
            _max = max(_max, curr_max)
        return _max
