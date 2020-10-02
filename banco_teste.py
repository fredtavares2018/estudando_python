# pip install pysqlite3 

import sqlite3

# cria o banco
meu_banco = sqlite3.connect('bd_clientes.db')

# habilita com esse método
cursor = meu_banco.cursor()

# comentar a linha abaixo após a primeira execução
#cursor.execute("CREATE TABLE usuarios (nome text, telefone text)")

nome = input("Digite seu nome: ")
telefone = input("Digite seu telefone: ")

cursor.execute("INSERT INTO usuarios VALUES(?, ?)", (nome,telefone))

# nos mostra tudo que foi cadastrado
cursor.execute("SELECT * FROM usuarios ")

meu_banco.commit()

recebendo = cursor.fetchall()

print(recebendo, recebendo[0][1])

