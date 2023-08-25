class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        s=0
        l=len(cost)
        j=0
        print("len",l)
        while j<l-1:
            
            if(j<l-3):
                print("b1 before",j,cost[j],cost[j+1],cost[j+2],s)
                if cost[j+1]>=cost[j+2]:
                    s+=cost[j+2]
                    if j==0:
                        s+=cost[0]
                    j+=2
                     
                elif cost[j+1]<cost[j+2]:
                    s+=cost[j+1]
                    j+=1
                print("b1 after",j,s)
            elif j==l-2:
                break
            else:
                print("b2 before",j,cost[j],cost[-2],cost[-1],s)
                if cost[-1]>=cost[-2]:
                    s+=cost[-2]
                    j+=1
                    print("b2 after",j,cost[j],cost[-2],cost[-1],s)
                    break
                if cost[-1]<cost[-2]:
                    s+=cost[-1]
                    j+=2
                    print("b2 after",j,cost[j],cost[-2],cost[-1],s)
                    break
        # print("b2 after",j,cost[j],cost[-2],cost[-1],s)
        return s

arr = [0,1,2,2]
s = Solution()
s.minCostClimbingStairs(arr)