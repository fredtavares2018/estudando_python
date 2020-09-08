
# Um conjunto montamos com seus valores entre chaves {} :
# Obs: nenhum elemento em um conjunto possui um índice

conj = {'Hoje','Amanhã','Ontem'}
print(type(conj))

# resposta 
# <class 'set'> conjunto

# Uma das formas de mostrar os elementos de um conjunto separadamente é transformá-lo em lista
# faça: list(conj)



# Uma lista montamos com seus valores entre colchetes [] :
# Obs: uma lista possui índices

numeros_primos = [2, 3, 5, 7, 11]
print(type(numeros_primos))
print(numeros_primos[0])

# resposta 
# <class 'list'>  lista
# numeros_primos[0] = 2



# Uma tupla montamos com seus valores entre parênteses () :
# Obs: uma tupla possui índices

decimais = (4.23, -8.44, 3.9)
print(type(decimais))
print(decimais[1])

# resposta 
# <class 'tuple'>  tupla
# decimais[1] = -8.44


# Uma ideia de dicionário seria um "json"
meus_carros = {1 : 'Caminhonete', 2 : 'Uno', 3 : 'Fusca', 4 : 'Jeep'}
print(type(meus_carros))
print(meus_carros[3])

# resposta 
# <class 'dict'>  dicionario
# meus_carros[3] = Fusca