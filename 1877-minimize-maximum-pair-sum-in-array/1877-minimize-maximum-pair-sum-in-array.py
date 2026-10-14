class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_pairSum=0
        r=len(nums)-1
        result=[]
        for l in range(len(nums)):
            result.append((nums[l],nums[r]))
            r-=1
        for num in result:
            if min_pairSum<sum(num):
                min_pairSum=sum(num)
        return  min_pairSum       
              
    


        