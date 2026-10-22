class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        res=set()
        indices=[]
        for index,val in enumerate(nums):
            if val==key:
                indices.append(index)
        for i in range(len(nums)):        
            for j in indices:
                if abs(i-j)<=k :
                    res.add(i)
        
        return sorted(list(res))           

        

       

                 


        