class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        left = 0; right = n - 1
        max_con = 0
        while left < right:
            con = min(heights[left], heights[right]) * (right - left)
            max_con = max(max_con, con)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_con 