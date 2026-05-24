class Solution:
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            l = len(s)
            s.add(n)
            if len(s) == l:
                return True
        
        return False
