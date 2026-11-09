class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        nums = sorted(nums)
        result = []
        #print(nums)
        for i in range(n):
            if nums[i] == nums[i - 1] and i > 0:
                continue

            elif nums[i] > 0:
                break
            
            else:
                target = nums[i]
                left = i + 1
                right = n - 1

                while left < right:
                    tar = nums[left] + nums[right]
                    if tar > -target:
                        right -= 1
                    elif tar < -target:
                        left += 1
                    elif tar == -target:
                        result.append([nums[left], nums[i], nums[right]])
                        left += 1; right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return result 



        