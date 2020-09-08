# funções com while que se fosse traduzir seria "enquanto"
# while é ,mais um, laço de repetição

#forma mais simples

incrementador = 0
while (incrementador < 5):  # vai fazer "enquanto" o incrementador for MENOR que 5
       print(incrementador)
       incrementador   = incrementador + 1 # estamos incrementando 1, ou seja , somando 1 toda vez que repetir
       
#saida no terminal
# 0
# 1
# 2
# 3
# 4


# 02. agora vamos imprimir os números pares no intervalo de 0 até 20------------------------------

x = 0
while x <= 20:
    x += 1    # estamos incrementando 1, ou seja , somando 1 toda vez que repetir
    if x%2 == 0:
        print(x, "é par")
        
    
    
        
# 03. agora você pode definir o intervalo entre os números------------------------------

def soPares(y):
    i = 0
    while i <= y:
        i += 1    # estamos incrementando 1, ou seja , somando 1 toda vez que repetir
        if i%2 == 0:
            print(i, "é par")
            
soPares(26) # aqui você informa até onde vai seu intervalo 
