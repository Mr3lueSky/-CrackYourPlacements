class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        array = [0] * len(nums)
        for num in nums:
            array[num] += 1
        return(array.index(max(array)))
