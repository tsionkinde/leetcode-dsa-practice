class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        SumAlice=sum(aliceSizes)
        SumBob=sum(bobSizes)
        for x in aliceSizes:
            y=x + (SumBob - SumAlice)//2
            if y in bobSizes:
                return [x,y]


       
        
        
     


        