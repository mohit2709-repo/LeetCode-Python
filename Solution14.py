class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first),len(last))):
            if (first[i] != last[i]):
                return answer
            else:
                answer += first[i]
        return answer