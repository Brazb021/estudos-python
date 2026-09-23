import json

try:
    with open("banco.json", "r") as ficheiro:
        conta = json.load(ficheiro)
except FileNotFoundError:
    print("Ficheiro 'banco.json' não encontrado. Criando um novo")
    conta = {"titular": "Breno", "saldo": 1000}

def realizar_saque(conta, valor_saque):
    if valor_saque <= conta['saldo']:
        conta["saldo"] -= valor_saque
        return f"O valor do saque foi de: {valor_saque}, e o novo saldo é de: {conta['saldo']}!"
    else:
        return "Saldo insuficiente!"

def realizar_deposito(conta, valor_deposito):
    conta["saldo"] += valor_deposito
    return f"O valor do depósito foi de: {valor_deposito}, e o novo saldo é de: {conta['saldo']}!"

opcao = ""

while opcao != "4":
    print("\n--- MENU ---")
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Ver Saldo")
    print("4 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        try:
            valor_saque = float(input("Digite o quanto quer sacar: "))
            print(realizar_saque(conta, valor_saque))
        except ValueError:
            print("Erro: Digite apenas números")

    elif opcao == "2":
        try:
            valor_deposito = float(input("Digite quanto quer depositar: "))
            print(realizar_deposito(conta, valor_deposito))
        except ValueError:
            print("Erro: Digite apenas números! ")

    elif opcao == "3":
        print(f"O saldo da sua conta é de: {conta['saldo']}")

    elif opcao == "4":
        with open("banco.json", "w") as ficheiro:
            json.dump(conta, ficheiro, indent=4)
        print("Saindo da conta! Até logo!")

    else:
        print("Opção inválida!")