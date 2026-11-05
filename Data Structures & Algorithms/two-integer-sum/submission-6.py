class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(nums):
            if target - num in d and d[target - num] != i:
                return [d[target - num], i]

            d[nums[i]] = i

# O(n) time and O(n) space

