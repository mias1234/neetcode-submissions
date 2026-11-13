class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        n = len(s)
        
        left = 0; right = 0
        max_length = 0

        while right < n:
            freq[s[right]] = freq.get(s[right], 0) + 1

            replace = (right - left + 1) - max(freq.values())

            if replace <= k:
                max_length = max(max_length, right - left + 1)
            
            elif replace > k:
                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]
                
                left += 1

            right += 1
        return max_length

            
            

