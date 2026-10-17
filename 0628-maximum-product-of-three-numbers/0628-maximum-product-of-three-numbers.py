import math
class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums = sorted(nums)
        first = math.prod(nums[-3:])
        second = nums[0] * nums[1] * nums[-1]
        return max(first, second)