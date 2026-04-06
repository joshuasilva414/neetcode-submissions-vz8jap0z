class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        def helper(ls):
            dp = [-1]*(n-1)
            dp[-1] = ls[-1]
            for i in range(len(ls)-2,-1,-1):
                prevMax = 0
                if i+2 < len(ls):
                    prevMax = dp[i+2]
                dp[i] = max(dp[i+1], prevMax+ls[i])
            return dp[0]
        return max(helper(nums[:-1]), helper(nums[1:]))