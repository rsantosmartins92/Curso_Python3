# Uma introdução ás f-strings (formatação de strings)

nome = 'Rafael Martins'
altura = 1.80
peso = 100
imc = peso / (altura * altura)

"f-strings"
texto = f'{nome} tem {altura:.2f} de altura e pesa {peso} quilos e seu IMC é {imc:.3f}'

print(texto)

print(nome, 'tem', altura, 'de altura', 'pesa', peso, 'quilos e seu IMC é',imc) 