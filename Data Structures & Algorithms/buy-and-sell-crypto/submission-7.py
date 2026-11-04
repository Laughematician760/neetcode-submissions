class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_list = []
        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                profit_list += [prices[j] - prices[i]]
        return max(max(profit_list, default = 0), 0)





        