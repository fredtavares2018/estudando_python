# para começar uma função comece com "def" e depois o nome da função

def olaMundo():
  print('Olá Mundo!')

# é preciso chamar a função para saber o que ela faz
olaMundo()

# resposta do terminal
# Olá Mundo!

# 02. agora passando um parâmetro ----------------------------------------
def olaParametro(x):
  print('Parâmetro recebido = ',x)

# é preciso chamar a função para saber o que ela faz
olaParametro(4)

# resposta do terminal
# Parâmetro recebido =  4

# 03. agora podemos fazer coisas mais interessamtes -------------------------
# verificando se o aluno está aprovado ou não
# essa função recebe os parâmetros(nota_um, nota_dois) e depois calcula
def calcular_medias(nota_um, nota_dois):
    n1 = float(nota_um)     #float são numero decimais
    n2 = float(nota_dois)   #float são numero decimais
    media = (n1 + n2 )/2
    if media < 7:           #compara se o numero recebido é MENOR que 7
        resultado = 'Reprovado com '      
    else:
        resultado = 'Aprovado com '
        
    print(resultado, media)

calcular_medias(7, 8.5)



# 04. agora podemos saber se um determinado número é PAR ou ÍMPAR -------------------------
def paridade(numero):
  if numero % 2 == 0: #faz a divisão e pega o resto, se resto for igual a ZERO é par
    print ("O número digitado",numero, "é par")
  else:
    print ("O número digitado",numero, "é impar")

paridade(5)