meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
signos = ('python','fortran','rust','go','java','javascript','c','php','haskel','perl','swift','kotlin')
mes=int(input('Digite o numero do mes em que nasceu:'))

if mes > 12 or mes < 1:
        print('Voce nao é um programador')
else:
        print('Você nasceu em', meses[mes-1], ', por isso seu signo é',signos[mes-1])