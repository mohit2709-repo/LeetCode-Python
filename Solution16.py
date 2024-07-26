class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])


        for i in range(len(nums)-2):
            start = i + 1
            end = len(nums)-1

            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if abs(total - target) < abs(res - target):
                    res = total
                if total < target:
                    start += 1
                else:
                    end -= 1

        return res



