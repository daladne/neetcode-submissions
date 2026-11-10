class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        zeros = 0

        for n in nums:
            if n == 0:
                zeros += 1
            else:
                product *= n

        for n in nums:
            if zeros > 1:
                output.append(0)
            elif zeros == 1:
                if n == 0:
                    output.append(product)
                else:
                    output.append(0)
            else:
                output.append(product // n)
        
        return output

# O(n + n) = O(n) time

#O(1) auxiliary space or O(n) total space

# uses division