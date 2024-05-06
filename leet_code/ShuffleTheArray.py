# problem
# https://leetcode.com/problems/shuffle-the-array/description/

class Solution(object):
    def shuffle(self, nums, n):
        lista_ordenada = []
        for posicao in range(n):
            lista_ordenada.append(nums[posicao])
            lista_ordenada.append(nums[posicao + n])
        return lista_ordenada