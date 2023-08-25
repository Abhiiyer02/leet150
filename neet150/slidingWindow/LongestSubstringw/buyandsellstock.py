class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        prof=0
        n=len(prices)
        while l<n and r<n:
            diff=prices[r]-prices[l]
            if diff <=0 :
                l = r
                r=l+1
            else:
                prev=prof
                print(prices[l],prices[r])
                prof=max(prof,diff)
                if prev<=prof:
                    r+=1
                else:
                    l+=1
                    r+=1
        return prof