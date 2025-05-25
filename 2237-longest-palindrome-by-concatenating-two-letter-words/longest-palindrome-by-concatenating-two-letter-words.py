from collections import Counter

class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        counter = Counter(words)
        length = 0
        
        for word in list(counter.keys()):
            rev = word[::-1]
            if word != rev:
                if rev in counter:
                    pairs = min(counter[word], counter[rev])
                    length += 4 * pairs
                    counter[word] -= pairs
                    counter[rev] -= pairs
            else:
                pairs = counter[word] // 2
                length += 4 * pairs
                counter[word] -= pairs * 2
        
        # Check if we can place one palindromic word in the center
        for word in counter:
            if word[0] == word[1] and counter[word] > 0:
                length += 2
                break

        return length
