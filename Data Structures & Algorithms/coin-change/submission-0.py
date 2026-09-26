from bisect import bisect_right


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {}
        memo[0] = 0

        def minCoins(target) -> int:
            if target < 0:
                return amount + 1
            if target in memo:
                return memo[target]

            minimum = amount + 1
            for i in range(bisect_right(coins, target)):
                change = minCoins(target - coins[i])
                minimum = min(minimum, change + 1)
            memo[target] = minimum
            return minimum

        ans = minCoins(amount)
        return ans if ans < amount + 1 else -1
