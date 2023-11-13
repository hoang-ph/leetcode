class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for i in range(len(s)):
            # add char count from s, subtract char count from t
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
        
        # if every element in count == 0, s and t are anagram
        for value in count.values():
            if value != 0:
                return False
        return True 
        