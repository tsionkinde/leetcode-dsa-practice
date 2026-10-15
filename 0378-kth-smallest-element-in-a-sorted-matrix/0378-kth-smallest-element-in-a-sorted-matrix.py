import numpy as np
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        res=[]
        new_arr=np.array(matrix)
        for val in new_arr.flat:
            res.append(val)
        res.sort()
        return int(res[k-1])   


      

        