from collections import Counter
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count=Counter(words)
        sorted_keys=sorted(count,key=lambda word:(-count[word],word))
        return sorted_keys[:k]

              


        