
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < min_price: min_price = price
            if price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
    
if __name__ == "__main__":
    test_data = [7,1,5,3,6,4]
    print(Solution().maxProfit(test_data))
