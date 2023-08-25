class Solution:
    def canJump(self, nums: list[int]) -> bool:
        l = len(nums)
        i=0
        sum = 0
        diff=l
        while(i<l-1):
            print(i,nums[i])
            i += nums[i]
            diff -=i
            if i <= 0 :
                return False
        if diff >0:
            return False
        return True
        
nums = [2,3,1,1,4]
s = Solution()
s.canJump(nums)