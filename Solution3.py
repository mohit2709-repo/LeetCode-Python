class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        set_char = set()
        n = len(s)

        for right in range(n):
            while s[right] in set_char:
                set_char.remove(s[left])
                left += 1

            window = (right - left) + 1
            longest = max(longest, window)
            set_char.add(s[right])

        return longest



