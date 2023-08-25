from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        left = 0
        right = 0
        d=defaultdict(int)
        longest = 0
        maxc=0
        while(right<length):
            
            d[s[right]]+=1
            maxc = max(d[s[right]],maxc)
            right+=1
            
            vals = d.values()
            if d and longest - maxc >=k:
                print(sum(vals),max(vals))
                d[s[left]] -=1
                left+=1            
            else:
                longest+=1
            print(d,left,right,longest)
        return longest



s="AABABBA"
k=1
S=Solution()
print(S.characterReplacement(s,k))    