# para começar uma função comece com "def" e depois o nome da função

def olaMundo():
  print('Olá Mundo!')

# é preciso chamar a função para saber o que ela faz
olaMundo()

# resposta do terminal
# Olá Mundo!

# agora passando um parâmetro 
def olaParametro(x):
  print('Parâmetro recebido = ',x)

# é preciso chamar a função para saber o que ela faz
olaParametro(4)

# resposta do terminal
# Parâmetro recebido =  4

#agora podemos fazer coisas mais interessamtes
def calcular_medias(nota_um, nota_dois):
    n1 = float(nota_um)
    n2 = float(nota_dois)
    media = (n1 + n2 )/2
    if media < 7:
        resultado = 'Reprovado com '      
    else:
        resultado = 'Aprovado com '
        
    print(resultado, media)

calcular_medias(7, 8.5)
