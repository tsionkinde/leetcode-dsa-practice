class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        current_floor=0
        time=0
        for i in range(len(requests)):           
            time+=abs(requests[i]-current_floor)
            current_floor=requests[i]
        return time    
            

        
        