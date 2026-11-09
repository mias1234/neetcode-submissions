class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1); m = len(s2)
        if n > m:
            return False
        
        left = 0; right = n - 1

        run_freq = {}; freq = {}

        for char in s1:
            freq[char] = freq.get(char, 0) + 1

        for i in range(n):
            run_freq[s2[i]] = run_freq.get(s2[i], 0) + 1
        
        while right < m - 1:
            if freq == run_freq:
                return True
            print(run_freq)
            run_freq[s2[left]] -= 1
            if  run_freq[s2[left]] == 0:
                del run_freq[s2[left]]
            left += 1

            right += 1
            run_freq[s2[right]] = run_freq.get(s2[right], 0) + 1

        return freq == run_freq
        