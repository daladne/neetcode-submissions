class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) >= len(t):
            lst = list(t)
            small = s
        else:
            lst = list(s)
            small = t

        for l in small:
            if l not in lst:
                return False

            lst.remove(l)
        return True

## make a list of t
## for every letter in s:
## if letter is not in list then it is NOT anagram
## remove letter from list
## if every letter was in list, then word IS anagram

## O(n + m) time and O(n) space

## make a hashmap of every letter
## if a letter in s, add by 1
## if a letter in l, add by 1
## if numbers match at end word IS anagram
## if numbers do not match word is NOT anagram

## O(n + m) time and O(n) space