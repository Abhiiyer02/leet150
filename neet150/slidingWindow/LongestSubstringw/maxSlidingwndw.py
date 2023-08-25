
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ln = len(nums)
        mw = []
        dq=[]
        l=0
        r=0
        while(r<ln):
            print("before: ",l,r,dq,mw)
            while len(dq) and nums[dq[-1]]<nums[r]:
                dq.pop(-1)
            dq.append(r)
            if l>dq[0]:
                dq.pop(0)
            if r-l==k-1:
                mw.append(nums[dq[0]])
                l+=1
            print("after: ",l,r,dq,mw)
            r+=1
        return mw
            
nums = [1,3,-1,-3,5,3,6,7]
k=3
S= Solution()
print(S.maxSlidingWindow(nums,k))