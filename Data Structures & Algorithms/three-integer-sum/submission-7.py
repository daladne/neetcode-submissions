class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, n in enumerate(nums):
            j, k = i + 1, len(nums) - 1
            if i > 0 and n == nums[i - 1]:
                pass
            else:
                while j < k:
                    left = nums[j]
                    right = nums[k]

                    if left + right == -n:
                        res.append([n, left, right])
                        j += 1
                        k -= 1

                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                    elif (left + right) < -n:
                        j += 1
                    else:
                        k -= 1
    
        return res
