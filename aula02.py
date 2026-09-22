def realizar_saque(saldo, valor_saque):
    if valor_saque <= saldo:
        saldo_final = saldo - valor_saque
        return f"Saque de R${valor_saque} realizado! Novo saldo é de {saldo_final}!"
    else:
        return "Saldo insuficiente!"

saldo = int(input("Digite seu saldo: "))
valor_saque = int(input("Digite o quanto quer sacar: "))

resposta = realizar_saque(saldo, valor_saque)
print(resposta)