class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups={}
        for num in range(1,n+1):
            digit_sum=0
            for digit in str(num):
                digit_sum+=int(digit)
            if digit_sum not in groups:
                groups[digit_sum]=[]
            groups[digit_sum].append(num)       
        max_size=max(len(group)  for group in groups.values())
        
        count=0        
        for group in groups.values():
            if len(group)==max_size:
                count+=1
        return count                





        