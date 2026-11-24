class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            j, k = i + 1, len(nums) - 1
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            while j < k:
                target = nums[i]
                left = nums[j]
                right = nums[k]
                

                if left + right == -target:
                    res.append([target, left, right])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k-=1

                elif left + right < -target:
                    j += 1
                else:
                    k -= 1

        return res

# O(n^2) time because nested loop

