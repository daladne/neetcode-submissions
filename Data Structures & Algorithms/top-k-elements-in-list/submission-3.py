class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # creates size(nums) + 1 amount of empty arrays

        for num in nums:
            count[num] = 1 + count.get(num, 0)  # count[num] = 1 + the current value of count[num] (if it exists)
        
        for num, cnt in count.items(): # for every number, count in [key, value] of count
            freq[cnt].append(num) # append num to freq[cnt]
        
        res = []
        for i in range(len(freq) - 1, 0, -1): # iterate through freq backwards and stop before reaching 0 - range(start, stop, step)
            for num in freq[i]: # iterate through list of numbers in freq[i]
                res.append(num) # append num to result list
                if len(res) == k: 
                    return res # return res if length of res == k
        