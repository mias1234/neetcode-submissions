class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        left = [1]; right = [1]

        for i in range(n):
            left.append(nums[i] * left[-1])
            right.append(nums[-(i+1)] * right[-1])

        result = []

        for i in range(n):
            result.append(left[i] * right[-(i+2)])
        
        return result

        