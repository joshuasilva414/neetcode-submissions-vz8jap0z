class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        n = len(coins)
        memo = {}
        def dfs(target, i) -> int:
            if (target,i) in memo:
                return memo[(target,i)]
            if i == n:
                return 0
            if target == 0:
                return 1
            if target < 0:
                return 0
            memo[(target,i)] = dfs(target-coins[i], i) + dfs(target, i+1)
            return memo[(target,i)]
        return dfs(amount, 0)