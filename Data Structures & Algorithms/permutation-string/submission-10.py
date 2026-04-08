class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        def charIdx(ch):
            return ord(ch)-ord('a')

        if m < n:
            return False

        match = [0]*26
        for ch in s1:
            match[charIdx(ch)] += 1

        l=0
        substr = [0]*26
        for i in range(l,n):
            substr[charIdx(s2[i])] += 1
        if substr == match:
            return True
        while l+n < m:
            substr[charIdx(s2[l+n])] += 1
            substr[charIdx(s2[l])] -= 1
            l+=1
            if substr == match:
                return True
            print(substr)
        return False