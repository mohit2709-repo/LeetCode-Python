class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n ==2 :
            return 2

        total = [0] * (n+1)
        total[1] = 1
        total[2] = 2

        for i in range (3, n+1):
            total[i] = total[i-1] + total[i-2]

        return total[i]