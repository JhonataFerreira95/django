# Implemente a solução aqui. 
# Definam e implementem todas as funções que julgarem necessárias.


import random

print('Bem vindo(a) a casa lotérica mais famosa do Brasil, somos a Fortune Monkey, entregamos infelicidades e frustrações desde 2024.')
print(' ')
print('Acerte ao menos 6 números para ganhar respectivamente os valores: 10.000 R$, 50.000 R$, 100.000 R$, 150.000 R$ ou 350.000 R$')
print(' ')

lista_sorteados = set()

while len(lista_sorteados) != 10:
    numeros_sorteados = random.randint(1,60)
    lista_sorteados.add(numeros_sorteados)


lista_valores_usuario = set()
while len(lista_valores_usuario) != 10:
    numeros_usuario = input('Digite 10 números únicos de 1 à 60, caso digitar um número repetido não será registrado: ')
    if numeros_usuario.isdigit() and int(numeros_usuario) <= 60:
        lista_valores_usuario.add(int(numeros_usuario))
    else:
        print('Letras não serão registradas, apenas números abaixo ou igual a 60.')

numeros_certos = 0
for i in lista_sorteados:
    for j in lista_valores_usuario:
        if i == j:
            numeros_certos += 1
print(f'Números escolhidos pelo usuário: {sorted(lista_valores_usuario)}')
print(' ')



print(f'Você acertou {numeros_certos} números.')

if numeros_certos >= 6:
    premios = {6: 10000, 7: 50000, 8: 100000, 9: 150000, 10: 350000}
    print(f'Que pena! Você ganhou {premios.get(numeros_certos, 0)} R$')
else:
    print('Felizmente você não acertou o suficiente para ganhar um prêmio e perdeu tudo.')
