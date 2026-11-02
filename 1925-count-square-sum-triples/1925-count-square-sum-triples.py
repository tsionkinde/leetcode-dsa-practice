import math
class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                sum_of_squares=i*i + j*j
                c=int(math.sqrt(sum_of_squares))
                if c<=n and c*c==sum_of_squares:
                    count+=1
        return count            

        