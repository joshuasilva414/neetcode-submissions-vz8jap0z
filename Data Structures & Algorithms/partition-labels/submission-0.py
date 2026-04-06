class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n=len(s)
        def chToIdx(ch) -> int:
            return ord(ch)-ord('a')

        first: List[int] = [-1] * 26
        last: List[int] = [-1] * 26
        for i in range(n):
            if first[chToIdx(s[i])]==-1:
                first[chToIdx(s[i])]=i
            last[chToIdx(s[i])]=i
        
        res = []
        l=0
        r=last[chToIdx(s[0])]
        i=l

        while True:
            while i < r and r <= n-1:
                r = max(r, last[chToIdx(s[i])])
                i+=1
            res.append(r-l+1)
            print(res)
            i+=1
            l=i
            if i>=n:
                break
            r=last[chToIdx(s[i])]
            if r > n-1:
                break
        return res