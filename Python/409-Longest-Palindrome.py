class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        else:
            freq = {}
            length = 0
            odd_bit = 0

            for c in s:
                freq[c] = freq.get(c, 0) + 1
            
            for v in freq.values():
                if v % 2 == 0:
                    length += v
                else:
                    length += v-1
                    odd_bit = 1

            return length + odd_bit
            