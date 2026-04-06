class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        def helper(ls):
            prevOpt, opt = 0, 0
            for x in ls:
                prevOpt, opt = opt, max(prevOpt + x, opt)
            return opt
        return max(helper(nums[:-1]), helper(nums[1:]))