class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n = len(s); m = len(t)
        dict1 = {}; dict2 = {}
        if n != m:
            return False
        
        for i in range(n):
            dict1[s[i]] = dict1.get(s[i], 0) + 1
            dict2[t[i]] = dict2.get(t[i], 0) + 1
        
        if dict1 == dict2:
            return True
        else:
            return False
        