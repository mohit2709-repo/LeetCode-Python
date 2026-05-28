class Solution:
    def containsduplicate(self, nums: List[int]) -> bool:
        prevMap = {}
        duplicates = []

        for num in nums:
            if num in prevMap:
                return True
            duplicates.append(num)
        return False

        



