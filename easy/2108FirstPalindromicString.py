# 2108. Find First Palindromic String in the Array
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array
# Aaron Merchant

class Solution:
    def firstPalindrome(self, words):
        for i in words:
            if i==i[::-1]:
                return i
        return ''
