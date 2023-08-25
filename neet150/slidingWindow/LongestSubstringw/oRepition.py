class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=0
        substr=""
        long=0
        aux=0
        for i in s:
            if (i in substr):
                ind = substr.index(i)
               # print(ind)
                substr = substr[ind+1:]+i
                #print(substr)
                sub=len(substr)
                
            else:
                substr=substr+i
                sub+=1
            if(sub>long):
                long=sub
        return long