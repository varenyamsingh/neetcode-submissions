class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Start they'll indicate/match
        # i = 0 → s[i] = n
        # j = 0 → t[j] = n
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
        