class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        freq = dict(sorted(freq.items(), key=lambda item: item[1]))

        result = []
        keys = list(freq.keys())
        for i in range(k):
            result.append(keys[-(i+1)])

        return result
        