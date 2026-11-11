class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1

        for i, n in enumerate(nums):
            output.append(product)
            
            product *= n
        
        # return output

        product = 1

        for i, n in reversed(list(enumerate(nums))):
            output[i] *= product

            product *= n

        return output

# O(2n) = O(n)
# O(n) space because of the reversed list