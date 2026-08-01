class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        res = 0
        sign = x // abs(x)
        x = abs(x)
        _max = -((-2)**31 + 1)
        _min = -(-2) ** 31
        limit = _max if sign == 1 else _min
        adj = 1 if sign < 0 else 0

        while x > 0:
            rem = x % 10
            x = x // 10

            # max // 10 == (-min) // 10
            if _max // 10 >= res and (_max - res * 10 >= rem - adj):
                res = res * 10 + rem
            else:
                return 0
        return sign * res
