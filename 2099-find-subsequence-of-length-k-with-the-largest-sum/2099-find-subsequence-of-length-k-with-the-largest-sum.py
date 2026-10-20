class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        pairs = list(enumerate(nums))#it displays the elements with their index
        pairs.sort(key=lambda x: x[1], reverse=True)#sorting based on value which means by the element in nums and largest comes first

        selected = pairs[:k] #we can select the first k maximum pairs  
        selected.sort()# sort by their original index

        res = []
        for i, num in selected:
            res.append(num)

        return res     
        