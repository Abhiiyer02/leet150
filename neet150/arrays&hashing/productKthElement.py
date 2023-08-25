class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = 1
        post = 1
        ans =[]
        ans.index()
        for i in nums: 
            pre *= i
            ans.append(pre)
        #print(ans)
        post=1
        for i in range(len(ans) -1 , -1 ,-1):
            if i!=0:
                pre = ans[i-1]
            else: 
                pre =1
            #print(ans , pre, post)
            ans[i] = pre*post
            post*=nums[i]

            
        return ans
    


    