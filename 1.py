class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict={}
        for index, i in enumerate(nums):
            x=target-i
            if x in dict:
                return [dict[x],index]
            dict[i]=index
