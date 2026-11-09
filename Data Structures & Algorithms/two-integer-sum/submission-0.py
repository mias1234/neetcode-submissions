class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in pair:
                return [pair[nums[i]], i]
            
            else:
                comp = target - nums[i]
                pair[comp] = i
        