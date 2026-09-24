class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}
        
        for i in range(len(s)):
            char_s = s[i]  
            char_t = t[i]     
            if char_s in mapS:
                if mapS[char_s] != char_t:
                    return False
            
            if char_t in mapT:
                if mapT[char_t] != char_s:
                    return False
                    
            mapS[char_s] = char_t
            mapT[char_t] = char_s
            
        return True