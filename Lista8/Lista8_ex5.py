#input
n1 = int(input("Digite um número para iniciar a sequência: "))
n2 = int(input("Digite outro número para finalizar a sequência: "))
cont = n1 + 1
pares = 0
impares = 0

#proces and output
while (cont < n2):
    if (cont % 2 == 0):
        pares += 1
    else:
        impares += 1
    print(f"{cont}")
    cont+=1






print(f"Existem {pares} números pares entre {n1} e {n2}")
print(f"Existem {impares} números impares entre {n1} e {n2}")

