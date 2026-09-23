import json

with open("banco.json", "r") as ficheiro:   # o modo "r" (Read / Leitura)
    conta = json.load(ficheiro)         # Carregar o conteúdo do ficheiro JSON para a variável conta

print("Dados lidos no ficheiro com sucesso")
print(f"Titular: {conta['titular']}")
print(f"Saldo atual: {conta['saldo']}")