class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n==0:
            return 0
        contains=set([s[0]])
        maxLen = 1
        start = 0
        end = 1

        while end < n:
            while end < n and s[end] not in contains:
                contains.add(s[end])
                end+=1
            maxLen=max(maxLen,end-start)
            contains.remove(s[start])
            start+=1
        return maxLen