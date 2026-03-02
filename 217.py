class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=sorted(nums)
        k=False
        for i in range (1,len(nums)):
            if a[i] == a[i-1]:
                k = True
                break            
        return k
