class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            hm[i] = hm.get(i, nums[i])
            for x in hm:
                if hm[x] + nums[i] == target and i != x:
                    return [x, i] 

        return "error"

## problem --
## array of integers nums and an integer target
## return i and j where nums[i] + nums[j] == target AND i != j
## assume every input has one pair of i and j that satisfy the condition
## return answer with the smaller index first

## brute force --
"""""
for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target: 
                    return [i, j]
"""""

## solution --
"""""
create empty hashmap
for each index of nums:
    set key of hashmap[index] to index, if it doesnt exist set value to 0, then add nums[i]
    for each value of hashmap:
        if value == target, return index i and index j -- does NOT work because how would you get index

save i to key, set value to nums[i]
keep going through nums
check if nums[j] + any value of hashmap == target --> requires iterating through hashmap
if true + if i != j return [i, j]
"""""


