class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        window= len(s1)
        
        d1 ={}
        l1 = list(s1)
        for i in l1:
            d1[i] = l1.count(i)
        
        l=0
        r=window
        for i in range(len(s2)-len(s1)):
                for j in range(i,len(s1)+1):
                    l2= list(s2[l:r])
                    d2={}
                    for j in l2:
                        d2[i] = l2.count(j)
                    if d1== d2:
                        return True
                    
                
        return False

 
        
if  __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    ob = Solution()
    print(ob.checkInclusion(s1,s2))

