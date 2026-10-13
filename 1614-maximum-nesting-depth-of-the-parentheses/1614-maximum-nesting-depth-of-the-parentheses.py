class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        maxDepth=0
        for i in s:
            if i=="(":
                count+=1
                if maxDepth < count:
                    maxDepth=count
            elif i==")":
                count-=1
        return maxDepth                

         



            


        