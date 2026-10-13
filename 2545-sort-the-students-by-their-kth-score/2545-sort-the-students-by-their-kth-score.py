class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:        
        sorted_score=sorted(score,key=lambda x:x[k],reverse=True)
        return sorted_score    
        