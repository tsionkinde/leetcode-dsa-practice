class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        l=0
        r=len(nums)-1
        nums.sort()
        for i in range(len(nums)):
            for j in range(len(nums)-1,-1,-1):
                if nums[i]==-nums[j]:
                    return nums[j]

            
        return -1                
        