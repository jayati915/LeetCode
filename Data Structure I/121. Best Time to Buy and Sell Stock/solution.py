class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buyPrice = 0
        sellPrice = 0
        profitMax = 0
        length = len(prices)
        i = 0
        slicedArray = []
        while i < length-1:
            profit = profit + prices[i+1] - prices[i]
            if profit < 0:
                profit = 0
            elif profit > profitMax: 
                profitMax = profit 
           
            i+=1

        return profitMax

                    

                    
