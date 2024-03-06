"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou impar. 
Caso o usuário não digite um número inteiro, informe que não é um número inteiro
"""

try:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
except :
    print("Você não digitou um número inteiro.")
    

#traço
print(50 * '-')


"""
Faça um programa que pergunte a hora ao usuárioe, baseando-se no horário descrito, exiba 
a saudação apropriada.
Ex.: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
try:
    hora = int(input("Digite a hora (0-23): "))
    if hora < 0 or hora > 23:
        print("Hora inválida. Digite um número entre 0 e 23.")
    elif hora < 12:
        print("Bom dia!")
    elif hora < 18:
        print("Boa tarde!")
    else:
        print("Boa noite!")
except ValueError:
    print("Você não digitou um número inteiro.")


   

   #traço
print(50 * '-')



"""
Faça um programa que peça o primeio nome do usúario. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto", 
se tiver entre 5 e 6 letras, escreva "Seu nome é normal", maior que 6 escreva "Seu nome é muito grande".
"""



nome = (input('Digite seu primeiro nome:'))
tamanho_nome = len(nome)

if tamanho_nome > 1:
        
    if tamanho_nome <= 4:
        print('Seu nome é curto')
        
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
       

    else:
         print('Seu nome é muito grande')
else:
        print('Digite mais de uma letra')

