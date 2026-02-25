class Solution:
    def mySqrt(self, x: int) -> int:
    
        """
        answer is beetwen 0 and x, 
        which int is the biggest sqrt which is no more than x
        """
        left = 0
        right = x
        while left <= right:
            mid=(left+right) // 2
            if mid*mid>x:
               right=mid-1
            else:
                left=mid+1
        return right