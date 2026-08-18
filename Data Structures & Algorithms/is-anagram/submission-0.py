class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s, t:
            return sorted(s) == sorted(t)
                