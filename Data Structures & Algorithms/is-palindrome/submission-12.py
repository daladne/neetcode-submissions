class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ0123456789")
        i = 0
        j = len(s) - 1

        if len(s) == 1:
            return True

        while i <= j:
            while s[i] not in alpha and i < len(s) - 1:
                i += 1
            
            while s[j] not in alpha and j > 0:
                j -= 1

            if s[i] in alpha and s[j] in alpha and s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

