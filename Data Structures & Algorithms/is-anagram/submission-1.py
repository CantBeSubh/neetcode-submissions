class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
            
        hash_map = dict()
        for ch in s:
            if ch in hash_map:
                hash_map[ch] +=1
            else:
                hash_map[ch] = 1
        
        for ch in t:
            if ch not in hash_map:
                return False
            elif hash_map[ch] == 0:
                return False
            else:
                hash_map[ch] -= 1
        
        return True