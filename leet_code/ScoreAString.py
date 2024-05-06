# problem
# https://leetcode.com/problems/score-of-a-string/description/

class Solution(object):
    def scoreOfString(self, s):
        
        reserva = ord(s[0])
        soma = 0
        subtracao = 0

        for letra in s:
            subtracao = ord(letra) - reserva
            if subtracao < 0:
               subtracao *= -1
            soma += subtracao
            reserva = ord(letra)
        return soma