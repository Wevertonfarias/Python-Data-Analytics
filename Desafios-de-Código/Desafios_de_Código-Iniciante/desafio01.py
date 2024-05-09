# Desafio: A Aventura do Explorador
'''
Desafio

Você é um intrépido explorador em uma jornada por uma terra desconhecida 
repleta de desafios emocionantes. Ao se deparar com uma floresta misteriosa, 
você percebe que a única maneira de atravessá-la é desvendando seus caminhos 
por meio de um código em Python. Prepare-se para a "Aventura do Explorador"!

Entrada
Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo, 
representando a quantidade de passos que o explorador deve dar na floresta. .

Saída
O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta. 
Utilize um laço de repetição para simular os passos do explorador. 
A cada passo, imprima uma mensagem informando a distância percorrida até o momento.

Exemplos
Alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Se o input for:	
2

O output deve ser:
Explorador: 1 passo
Explorador: 2 passos

Se o input for:
3

O output deve ser:
Explorador: 1 passo
Explorador: 2 passos
Explorador: 3 passos
'''

quantidade_passos = int(input())
if quantidade_passos > 0:
    for i in range(1,quantidade_passos+1):
        if i == 1: ## Singular do texto de saida
            print(f'Explorador: {i} passo')
        else: ## Plural do texto de saida
            print(f'Explorador: {i} passos')
else:
    print("Nenhum passo dado na floresta.")