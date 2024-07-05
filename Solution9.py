class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        reverse_str = num_str[::-1]
        
        if x <0:
            return False
        
        if reverse_str == num_str:
            return True
        else:
            return False