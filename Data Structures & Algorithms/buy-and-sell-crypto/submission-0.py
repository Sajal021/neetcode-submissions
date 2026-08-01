class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        left=0
        while left<len(prices):
            for right in range(left+1,len(prices)):
                if prices[left]<prices[right]:
                    max_prof=max(max_prof,prices[right]-prices[left])
            left+=1
        return max_prof
            
