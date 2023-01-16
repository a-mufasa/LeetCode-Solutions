class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        else:
            start = prices[0]
            mp = 0
            for p in prices[1::]:
                temp = p - start
                if temp > mp:
                    mp = temp
                if start > p:
                    start = p
            return mp