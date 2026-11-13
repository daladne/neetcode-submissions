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

# O(n) time - nested for loop but each sequence is only counted from starting number so the inner loop visits each unique member at most once
# also building set is O(n) so it is 3n work = O(n)

# O(n) space 