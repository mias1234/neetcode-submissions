class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0; right = 0
        result = []
        heap = []
        while right < len(nums):
            heapq.heappush_max(heap, (nums[right], right))

            if right - left + 1 >= k:
                while heap[0][1] <= right - k:
                    heapq.heappop_max(heap)
                result.append(heap[0][0])

                left +1
            

            right += 1
        return result

                