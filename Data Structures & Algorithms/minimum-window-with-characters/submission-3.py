class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqt = {}
        n = len(s); m = len(t)
        length = float('inf')

        if n < m:
            return ''

        for char in t:
            freqt[char] = freqt.get(char, 0) + 1

        need_types = len(freqt)
        left = 0; right = 0
        have = 0
        count = {}
        minl = 0; minr = 0

        while right < n:
            count[s[right]] = count.get(s[right], 0) + 1

            if s[right] in freqt:
                print(s[right])
                if freqt[s[right]] == count[s[right]]:
                    have += 1
            
            while have == need_types:
                if right - left + 1 < length:
                    length = right - left + 1
                    minl = left
                    minr = right
                
                count[s[left]] -= 1
                if s[left] in freqt:
                    if count[s[left]] < freqt[s[left]]:
                        have -= 1

                if count[s[left]] == 0:
                    del count[s[left]]

                left += 1

            right += 1
        return '' if length == float('inf') else s[minl:minr + 1]

            

            





        