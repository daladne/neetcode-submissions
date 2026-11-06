class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
    
        for s in strs:
            count = [0] * 26

            for l in s:
                count[ord(l) - ord('a')] += 1
            
            key = tuple(count)
            
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        
        lst = []

        for v in d.values():
            lst.append(v)
        
        return lst
        