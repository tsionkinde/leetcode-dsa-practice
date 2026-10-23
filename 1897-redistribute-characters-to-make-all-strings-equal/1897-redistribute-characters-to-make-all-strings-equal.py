from collections import Counter

class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        count = Counter()

        for word in words:
            count.update(word)

        for char in count:
            if count[char] % len(words) != 0:
                return False

        return True