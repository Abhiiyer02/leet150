class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        for i in nums:
            myDict[i]  = myDict.get(i,0)+1
        
        freq = [[] for i in range(len(nums)+1)]
        for num,count in myDict.items():
            freq[count].append(num)
            
        res= []
        for i in range(len(freq)-1 , 0 , -1): #upper bound, #lower bound , decrement  
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res