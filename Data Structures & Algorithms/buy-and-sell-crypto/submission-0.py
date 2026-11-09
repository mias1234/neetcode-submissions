class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = 0
        curr = 1
        max_prof = 0

        while curr < len(prices):
            if prices[prev] > prices[curr]:
                prev, curr = curr, curr + 1
            
            else:
                max_prof = max(max_prof, prices[curr] - prices[prev])
                curr += 1
        
        return max_prof