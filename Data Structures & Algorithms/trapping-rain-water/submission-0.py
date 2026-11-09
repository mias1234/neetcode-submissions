class Solution:
    def trap(self, height: List[int]) -> int:
        left  = 0
        right = len(height) - 1
        water = 0
        max_left = height[left]
        max_right = height[right]

        while left < right:
            if max_left <= max_right:
                water += min(max_left, max_right) - height[left]
                left += 1
                max_left = max(max_left, height[left])
            else:
                water += min(max_left, max_right) - height[right]
                right -= 1
                max_right = max(max_right, height[right])
                
    
        return water