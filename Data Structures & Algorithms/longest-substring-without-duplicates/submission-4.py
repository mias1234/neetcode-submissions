class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        prev = 0
        hash_set = set()
        max_len = 0

        for curr in range(len(s)):
            while s[curr] in hash_set:
                hash_set.remove(s[prev])
                prev += 1
            hash_set.add(s[curr])
            max_len = max(max_len, curr - prev + 1)

        return max_len