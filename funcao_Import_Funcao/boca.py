import cerebro

receber_login = input(" Digite login: ")
receber_senha = input(" Digite senha: ")

resp1 = cerebro.login(str(receber_login))
resp2 = cerebro.senha(str(receber_senha))

print(resp1, resp2)