class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {};

        for l in s:
            if l in d:
                d[l] += 1;
            else:
                d[l] = 1;
        
        for l in t:
            if l in d:
                d[l] -= 1;
                
                if d[l] == 0:
                    del d[l];
            else:
                return False;
        
        if not d: return True;
        else: return False


