# class Solution:
#     def group(self,strs):
#         print("asdasd")


# strs = ["eat","ate","pat","apt"]
# s= Solution()
# s.group(strs)
# s = ["asd"]
# print([s])

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
