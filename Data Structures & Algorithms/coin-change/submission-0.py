class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = defaultdict(lambda: math.inf, {a: 1 for a in coins})

        for i in range(min(coins), amount+1):
            if dp[i] is math.inf:
                continue

            for c in coins:
                dp[c + i] = min(dp[i] + 1, dp[c + i])

        return (dp[amount]) if dp[amount] is not math.inf else -1
            