# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Aaron Merchant

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
