class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            n = target - nums[i] 

            if n in hm:
                return [hm[n], i]

            hm[nums[i]] = i

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

O(n^2) time and O(n) space
"""""

## my solution --
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

O(n^2) time and O(n^2) space
"""""

""""" real solution
for each index of nums:
    set n = complement of nums[i] (target - nums[i])

    if n is a key of hm:
        return
    
    create hm element with key of nums[i] and value of index


    code checks if complement of nums[index] is a key in hashmap. then creates a hashmap element with key of nums[index] and value of index

    O(n) time and space because iterating through nums is O(n) and iterating through keys of hashmap is O(1).
    space is O(n) because hashmap can grow to match nums

    LEARNED: hashmap is useful for key lookup because it is O(1) time
             value lookup is O(n)
"""""
