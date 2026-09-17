class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0

        for i in range(len(s) - 1):
            ans += abs(s[i].encode()[0] - s[i + 1].encode()[0])

        return ans