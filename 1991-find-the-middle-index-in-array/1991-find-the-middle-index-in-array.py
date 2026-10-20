class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i+1])==sum(nums[i:]):
                return i
            else:
                continue 
        return  -1         


        