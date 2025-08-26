class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Left = 0
        max = 0

        for Right in range(len(prices)):
            if prices[Right] < prices[Left]:
                Left = Right
            
            if  prices[Right] - prices[Left] > max :
                max =  prices[Right] - prices[Left]
            print(max)
        return max
