from random import randint
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap
        c = defaultdict(int)
        for n in nums:
            c[n] += 1

        # heap
        # c = [(-v, k) for k, v in c.items()]
        # heapq.heapify(c)
        # return [heapq.heappop(c)[1] for _ in range(k)]

        # Quickselect
        less = [(-v, k) for k, v in c.items()]
        more = []
        eq = []

        # print(f"c={c}")
        i = 0
        while not (len(less) < k and len(less) + len(eq) >= k) and i < 10:
            i += 1
            # print(f"i={i}\nless={less}\neq={eq}\nmore={more}\n---")

            # choose pivot
            if len(less) < k:
                pivot = more[randint(0, len(more) - 1)]
                less = less + eq + [x for x in more if x[0] < pivot[0]]
                eq = [x for x in more if x[0] == pivot[0]]
                more = [x for x in more if x[0] > pivot[0]]

            else:
                pivot = less[randint(0, len(less) - 1)]
                more = [x for x in less if x[0] > pivot[0]]
                eq = [x for x in less if x[0] == pivot[0]]
                less = [x for x in less if x[0] < pivot[0]]

            # print(f"pivot={pivot}\n")


        # print("====")
        # print(f"final: less={less}, eq={eq}, more={more}")

        ans = less + eq
        ans = [x[1] for x in ans]
        return ans