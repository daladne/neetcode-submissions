class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            left = numbers[i]
            right = numbers[j]

            if left + right == target:
                return [i + 1, j + 1]
            elif left + right < target:
                i += 1
            else:
                j -= 1

# O(n) time because at most you go through each element once
# O(1) space because of constant number of variables