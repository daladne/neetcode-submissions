class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        seq = 0
        res = 1

        if nums == []:
            return 0
        for num in num_set:
            seq = 0
            if num + 1 in num_set: # if next element in sequence exists
                 if num - 1 not in num_set: # if num is start of sequence
                    for i in range(len(num_set)):
                        if num + seq in num_set:
                            seq += 1
                        else:
                            break

            if seq > res:
                res = seq

        return res

# if new seq add new list
# else 