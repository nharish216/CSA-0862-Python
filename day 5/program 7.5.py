
class Solution:
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(c))
s =input("enter : ")
k = int(input("enter: "))
x =Solution()
print(x.longestSubstring( s, k))
