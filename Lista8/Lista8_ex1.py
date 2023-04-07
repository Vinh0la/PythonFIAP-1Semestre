#input
n = int(input("Digite um número inteiro: "))
soma = 0
cont = 1

#proces
while (cont <= n):
    soma += cont
    cont += 1

#output
print(f"A soma dos valores de 1 até {n} é: {soma}")
