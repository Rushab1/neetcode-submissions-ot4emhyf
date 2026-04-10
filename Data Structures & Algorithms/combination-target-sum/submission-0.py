class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        n = len(candidates)
        dp = defaultdict(set, {
            c: set([tuple([c])]) for c in candidates
        })

        for i in range(candidates[0], target + 1):
            for j in range(n):
                c = candidates[j]
 
                if i + c > target:  # micro optimization
                    continue

                for x in dp[i]:
                    if c >= x[-1]:
                        dp[i + c].add((*x, c))
        return [list(x) for x in dp[target]]
