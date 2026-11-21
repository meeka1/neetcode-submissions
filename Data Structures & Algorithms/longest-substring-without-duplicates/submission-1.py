class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        window = set()
        max_length = 0

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
                max_length = max(max_length, R-L+1)

            window.add(s[R])

        return max_length