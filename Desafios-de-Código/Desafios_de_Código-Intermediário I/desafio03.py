'''Desafio
Você está trabalhando para uma empresa que utiliza extensivamente os serviços da AWS, e após algumas análises a equipe de segurança identificou que algumas senhas dos usuários no IAM são fracas e podem representar um risco à segurança dos dados da empresa.
Para resolver esse problema, foi solicitado que você desenvolva um programa capaz de analisar as senhas dos usuários e fornecer uma validação de força com base em critérios predefinidos.

Requisitos de segurança para a senha:

A senha deve ter no mínimo 8 caracteres.
A senha deve conter pelo menos uma letra maiúscula (A-Z).
A senha deve conter pelo menos uma letra minúscula (a-z).
A senha deve conter pelo menos um número (0-9).
A senha deve conter pelo menos um caractere especial, como !, @, #, $, %, etc.

Entrada
A entrada será uma única string representando a senha que precisa ser validada.

Saída
Seu programa deve retornar uma mensagem indicando se a senha fornecida pelo usuário atende aos requisitos de segurança ou não,
juntamente com um feedback explicativo sobre os critérios considerados.

Entrada:
0101
030609saturno*
010203Jupiter

Saída:
Sua senha e muito curta. Recomenda-se no minimo 8 caracteres.
Sua senha atende aos requisitos de seguranca. Parabens!
Sua senha nao atende aos requisitos de seguranca.
'''
def busca_validacao(a, b):
    flag = False
    for i in a:
        if i in b:
            flag = True
            break
    return flag        
                
def verificar_forca_senha(senha):
    
    answer = 'Sua senha e muito curta. Recomenda-se no minimo 8 caracteres.'
    # Verificando o comprimento da senha
    if len(senha) >= 8:
        # TODO: Verifique se a senha contém letras maiúsculas e minúsculas
        tem_letra_maiuscula = busca_validacao('ABCDEFGHIJLMNOPQRSTUVXYZ', senha) 
        tem_letra_minuscula = busca_validacao('ABCDEFGHIJLMNOPQRSTUVXYZ'.lower(), senha)
        
        # Verificando se a senha contém sequências comuns
        if busca_validacao(['123456', 'abcdef'], senha): 
            answer = "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."
            pass
        # Verificando se a senha contém palavras comuns
        if busca_validacao(['password', '123456', 'qwerty'], senha):
            answer = "Sua senha e muito comum. Tente uma senha mais complexa."
            pass
        # TODO: Verificar o comprimento mínimo e critérios de validação
        tem_numero = busca_validacao('0123456789', senha)
        
        tem_caractere_especial = busca_validacao('_~!@#$%^&*(){}[]-+/?></|=', senha)
       
        flag = tem_letra_maiuscula and tem_letra_minuscula and tem_numero and tem_caractere_especial
       
        answer = 'Sua senha atende aos requisitos de seguranca. Parabens!' if flag else 'Sua senha nao atende aos requisitos de seguranca.'
    
    return answer

# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)