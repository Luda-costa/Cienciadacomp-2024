ano = int(input("Digite o ano a ser analisado:"))

if ano % 4==0:
  print("É bissexto!!!")
else:
  prox = ano + (4 - ano % 4)
  print("Não é bissexto!!! O ano será bissexto em", prox)