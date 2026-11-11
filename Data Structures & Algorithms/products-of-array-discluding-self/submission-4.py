class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1

        for i, n in enumerate(nums):
            output.append(product)
            
            product *= n
        
        # return output

        product = 1

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= product

            product *= nums[i]

        return output

# O(2n) = O(n)
# O(1) auxiliary, O(n) total space