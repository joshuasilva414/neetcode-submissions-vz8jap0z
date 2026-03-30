class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(m+1) for _ in range(n+1)]
        dp[0][1] = 1
        for c in range(1,m+1):
            for r in range(1,n+1):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        print(dp)
        return dp[n][m]