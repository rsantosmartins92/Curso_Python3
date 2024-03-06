# Operadores lógicos 
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão a expressão inteira será avaliada naquele valor
# São considerados false (que vocẽ ja viu) 0 0.0 '' false
# Também existe o tipo none que é usado para representar um não valor

entrada = input('[E]ntrar [S]air:')
senha_digitada = input('Senha:')

senha_permitida = '123456'

if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
    print('Entrar')

else: print('sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)