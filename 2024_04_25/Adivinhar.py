x = 33
res = 0
c = 0

print('Dica: Jesus!!!')
while res != x:
        res = int(input('Digite um número:'))
        if res != x:
                print('Você errou. Tente de novo!!!')
        c += 1

print('Parabéns!!! Você demorou', c, 'tentativas')