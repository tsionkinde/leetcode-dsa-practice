class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        pairs = list(enumerate(nums))
        pairs.sort(key=lambda x: x[1], reverse=True)

        selected = pairs[:k]
        selected.sort()

        res = []
        for i, num in selected:
            res.append(num)

        return res     
        