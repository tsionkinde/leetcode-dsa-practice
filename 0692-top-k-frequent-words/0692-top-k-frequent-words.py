from collections import Counter
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count=Counter(words)
        sorted_keys=sorted(count)
        sorted_keys.sort(key=lambda word: count[word], reverse=True)
        return sorted_keys[:k]

              


        