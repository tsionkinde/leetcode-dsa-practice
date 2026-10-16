class Solution:
    def checkRecord(self, s: str) -> bool:    
        countA=0
        countL=0
        for i in s:
            if i=="A":
                countA+=1
            elif i=="L":
                countL+=1
        if "LLL" not in s and countA<2:
            return True
        else:
            return False            


        