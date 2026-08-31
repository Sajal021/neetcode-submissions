class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_prof = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         curr_prof = prices[j] - prices[i]
        #         max_prof = max(curr_prof, max_prof)
        # return max_prof
        max = 0
        min = float('inf')
        prof = 0
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
                max  = 0
            else:
                max =  prices[i]
            if prof < (max-min):
                prof = max-min
            
        return prof