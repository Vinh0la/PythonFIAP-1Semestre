#input
tx_abat = int(input("Digite a taxa de abatimento em porcentagem: "))
num_prest = int(input("Digite o número de prestações: "))
val_1prest = float(input("Digite o valor da primeira prestação: "))
qnt_prest = 0


#proces
while (qnt_prest < num_prest):
    porcentagem = (val_1prest * tx_abat) / 100
    val_1prest -= porcentagem
    qnt_prest += 1
    print(f"R${val_1prest:.2f}")
