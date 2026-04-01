class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        seen=[False]*n
        frontier = [0]
        hops=0
        while frontier:
            explore = []
            for i in frontier:
                if i == n-1:
                    return 0
                if i + nums[i] >= n-1:
                    return hops+1
                for j in range(1,nums[i]+1):
                    if not seen[i+j]:
                        seen[i+j]=True
                        explore.append(i+j)
            frontier=explore
            hops+=1
        return hops