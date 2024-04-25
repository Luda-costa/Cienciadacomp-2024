alt = int(input('Digite a altura do losangulo:'))

tamanho = alt //2

c=0

#Caso digite numero impar
if alt%2 == 0:
       exit()

# primeira metada do losangulo
for num in range(alt+1):
   if num%2 != 0 :
       print('.' * (tamanho - c)  + '#' * num)
       c += 1

# segunda metade
c = 0
for num in reversed(range(alt)):
   if num%2 != 0 :
       print('.' * (c+1) + '#' * num)
       c += 1