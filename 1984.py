class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        a=1000000
        if k==1:
            return 0
        else:
            for i in range(len(nums)-k+1):
                diff = nums[i+k-1] - nums[i]
                if diff<a:
                    a=diff
            return a
