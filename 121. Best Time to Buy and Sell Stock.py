class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_buy = prices[0]
        for idx,price in enumerate(prices):
            profit = max(profit, price-min_buy )
            min_buy = min(min_buy,price)
        return profit

sl = Solution()

print(sl.maxProfit([2,1,4]))




        # Timelimit exceeded!!!!!
        # profit = 0
        # for idx, price in enumerate(prices):
        #     potential_profits = []
        #     for i in range(idx+1, len(prices)):
        #         potential_profits.append(prices[i]-price)
        #     profit = max(profit, max(potential_profits) if potential_profits != [] else 0)

        # return profit