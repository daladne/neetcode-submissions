class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        if len(s) == 1:
            return True

        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            
            while not s[j].isalnum() and i < j:
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


# O(n) because each character is seen at most once
# O(1) space

# in the case of i and j both finding non-alphanumeric character, 
# both inner loops stop when i == j so if no valid characters remain, the character is compared to itself which will return True
