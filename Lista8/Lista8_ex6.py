senha = str(input("Cadastre sua senha pela primeira vez: "))
cadastro = str(input("Digite sua senha: "))

while (cadastro != senha):
    print("Senha incorreta !")
    cadastro = str(input("Digite novamente: "))

print("BEM VINDO")