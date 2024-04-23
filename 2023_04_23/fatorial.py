num = int(input('Digite um numero:'))
result = 1
for number in range(num+1):
        if number != 0:
                result = result * number
print(result)