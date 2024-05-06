# problem
# https://leetcode.com/problems/find-words-containing-character/description/

class Solution(object):
    def findWordsContaining(self, words, x):
        lista = []
        posicao = -1
        for word in words:
            posicao += 1
            if x in word:
                lista.append(posicao)
        return lista