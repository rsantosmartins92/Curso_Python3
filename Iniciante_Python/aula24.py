# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  R a f a e l
# -6-5-4-3-2-1

nome = 'Rafael'
print(nome[4])
print(nome[0])
print('el'in nome)
print('Rad' in nome)

print(10 * '-')

print('el' not in nome)
print('ru' not in nome)

print(10 * '-')

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')



