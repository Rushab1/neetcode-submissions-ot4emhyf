from random import randint 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(p):
            x, y = p
            return math.sqrt(x ** 2 + y ** 2)

        d = [(dist(p), p) for p in points]

        # Quick select
        ws = d  # workspace
        it_k = k

        while True:
            idx = randint(0, len(ws) - 1)
            pivot = ws[idx]
            less = [w for w in ws if w <= pivot]

            if len(less) == it_k:
                break

            if len(less) > it_k:
                ws = less
                continue

            else:
                it_k -= len(less)
                ws = [w for w in ws if w > pivot]

        ret = [w[1] for w in d if w <= pivot]
        return ret

