# declaramos duas listas vazias
nomes=[]
notas=[]
# contamos quantos elementos tem em cada lista
quantidade = len(nomes)
quantidadeNotas = len(notas)
while quantidade < 2:
    nome = input("Digite um nome ")
    # adicionamos(append) nome na lista nomes
    nomes.append(str(nome))
    quantidade = quantidade + 1
    # condicional if, verificando se já tem DOIS nomes cadastrados
    if quantidade == 2:
        while quantidadeNotas < 2:
            nota = input("Digite a nota de " + nomes[quantidadeNotas]+ " ")
            # adicionamos(append) nota na lista botas
            notas.append(str(nota))
            quantidadeNotas = quantidadeNotas + 1

# mandamos listar o nome ao lado da nota       
listar = 0
while listar < 2:
    print(nomes[listar], notas[listar])
    listar = listar + 1