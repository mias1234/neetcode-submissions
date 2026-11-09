class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        nums = list(num_set)
        print(num_set)
        n = len(list(num_set))
        max_seq = 0
        for i in range(n):
            prev = nums[i] - 1
            if prev not in num_set:
                count = 1
                next1 = nums[i] + 1
                while next1 in num_set:
                    count += 1
                    next1 += 1

                max_seq = max(max_seq, count)
        
        return max_seq

        