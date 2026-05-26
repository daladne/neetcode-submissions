class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c = {}

        for l in s:
            c[l] = c.get(l, 0) + 1
        
        for l in t:
            if l not in c:
                return False
            
            c[l] -= 1

            if c[l] < 0:
                return False

        return True
        

## if length of s != length of t, false
## create empty hashmap c
## for letters in s: find letter -> if it doesn't exist, add to hashmap -> add 1 -> change value of letter in hashmap to that value
## for letters in t: if letter is not in c, false -> if letter is in c, subtract value by 1 -> if value is less than 0, false

## O(n + m) time and O(1) space