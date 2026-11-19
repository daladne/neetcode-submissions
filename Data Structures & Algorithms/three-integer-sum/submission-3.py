class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, n in enumerate(nums):
            j, k = i + 1, len(nums) - 1
            while j < k:
                left = nums[j]
                right = nums[k]
                if left + right == -n:
                    if [n, left, right] not in res:
                        res.append([n, left, right])

                    j +=1
                    k -= 1
                elif (left + right) < -n:
                    j += 1
                else:
                    k -= 1
    
        return res
