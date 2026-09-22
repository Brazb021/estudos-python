conta = {
    "titular": "Breno",
    "saldo": 1000,
    "cpf": "123.123.123-00"
}

def realizar_saque(conta, valor_saque):
    if valor_saque <= conta["saldo"]:
        conta["saldo"] -= valor_saque
        return f"O saque foi realizado no valor de: {valor_saque}! O novo saldo é de: {conta["saldo"]}!"
    else:
        return "Saldo insuficiente!"

opcao = ""

while opcao != "3":
    print("\n--- MENU ---")
    print("1 - Sacar")
    print("2 - Ver Saldo")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")


    if opcao == "1":
        valor_saque = int(input("Quanto quer sacar? "))
        print(realizar_saque(conta, valor_saque))
    elif opcao == "2":
        print(f"O valor do seu saldo é de {conta["saldo"]}!")
    elif opcao == "3":
        print("Saindo do sistema! Até logo!")
    else: 
        print("Opção inválida!")