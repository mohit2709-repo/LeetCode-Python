class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        spointer = tpointer = 0

        while spointer < len(s) and tpointer < len(t):
            if s[spointer] == t[tpointer]:
                spointer += 1
            tpointer += 1

        return spointer == len(s)