class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        dp = [[None]*(n+1)] * (m+1)
        dp[0][0]=0

        if m+n != len(s3):
            return False

        for r in range(m+1):
            for c in range(n+1):
                best=0
                if r>0:
                    best = dp[r-1][c] + (1 if (s3[dp[r-1][c]] == s1[r-1]) else 0)
                if c > 0:
                    best = max(best, dp[r][c-1] + (1 if (s3[dp[r][c-1]] == s2[c-1]) else 0))
                dp[r][c]=best
        print(dp)
        return dp[-1][-1] == len(s3)