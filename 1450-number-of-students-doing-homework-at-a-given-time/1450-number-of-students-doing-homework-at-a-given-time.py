class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        count=0
        for i in range(len(startTime)):
            if queryTime in range(startTime[i],endTime[i]+1):
                count+=1
        return count        
        