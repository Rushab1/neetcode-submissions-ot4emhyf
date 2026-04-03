class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)

        if n1 + n2 != n3:
            return False

        if n1 == 0 or n2 == 0:
            return s1 + s2 == s3

        dp = {0: True}
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i == 0 or j == 0:
                    dp[j] = ((s1[:i] + s2[:j]) == s3[:i + j])
                    continue

                val = False
                val = val or (dp[j] and s1[i - 1] == s3[i + j - 1])
                val = val or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])

                dp[j] = val

        return dp[n2]
