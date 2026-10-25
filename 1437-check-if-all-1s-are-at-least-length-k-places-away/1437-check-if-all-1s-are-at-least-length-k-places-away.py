class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        indices=[]
        for i,val in enumerate (nums):
            if val==1:
                indices.append(i)
        for index in range(1,len(indices)):
            if indices[index]-indices[index-1]<=k:
                return False
        return True        


         
        