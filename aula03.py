conta = {
    "titular": "Breno",
    "saldo": 1000,
    "cpf": "123.123.123-00"
}

def realizar_saque(conta, valor_saque): #pega a conta direto para mexer nela
    if valor_saque <= conta["saldo"]:   #verifica se o valor do saque é menor do que o saldo DIRETO da conta
        conta["saldo"] -= valor_saque   #Diminui o saldo da conta 
        return f"Saque realizado! Novo saldo de {conta['titular']}: R$ {conta['saldo']}"
    else:
        return "Saldo insuficiente"

valor_saque = int(input("Quanto quer sacar? "))
resultado = realizar_saque(conta, valor_saque)
print(resultado)

print(conta)