# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Beats 99.21% of users with Python3

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase =''.join([char for char in s if char.isalnum()]).lower()
        return lowercase == lowercase[::-1]
