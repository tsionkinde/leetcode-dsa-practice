class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1        
        summ=0
        while l<r:
            conc=str(nums[l])+str(nums[r])
            summ+=int(conc)
            l+=1
            r-=1           
            
        if l==r: 
            summ+=nums[l]    
           
        
        return summ            

            


        