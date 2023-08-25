class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = list(set(nums))
        s.sort()
        print(s)
        nums.sort()
        if nums==s:
            return False
        return True
    
s=Solution()
nums = [1,5,-2,-4,0]
nums.sort()
print(nums)
print(s.containsDuplicate(nums))



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
