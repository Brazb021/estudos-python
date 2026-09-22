nome = input("Digite seu nome: ")
saldo = int(input("Digite seu saldo: "))
idade = int(input("Digite sua idade: "))
valor_saque = int(input("Digite quanto quer sacar: "))


print(f"Bem-vindo ao banco, {nome}")
print(f"Sua idade é: {idade}")
print(f"Seu saldo atual é: {saldo}")
print(f"Você quer sacar: {valor_saque}")


if valor_saque <= saldo:
    saldo_final = saldo - valor_saque
    print(f"Saldo realizado! O novo valor da sua conta é de: {saldo_final}!")
else:
    print("Saldo insuficiente!")