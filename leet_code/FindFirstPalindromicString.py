# problem
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            if word[::-1] == word:
                return word
        return ""