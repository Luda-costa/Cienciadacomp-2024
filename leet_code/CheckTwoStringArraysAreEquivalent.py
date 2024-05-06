# problem
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        palavra1 = ''.join(word1)
        palavra2 = ''.join(word2)
        if palavra1 == palavra2:
            return True
        return False