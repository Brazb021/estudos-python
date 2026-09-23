import json

conta = {
    "titular": "Breno",
    "saldo": 1000,
    "cpf": "123.123.123-00"
}

with open("banco.json", "w") as ficheiro:   #with é para sempre mexer apenas quando estiver aberto e não precisar fechar
    json.dump(conta, ficheiro, indent=4)    #banco.json é o nome do arquivo // W vem de "write"
                                            #as ficheiro: nomeando o banco.json // json.dump: pega o dicionario (conta)

    print("Dados guardados com sucesso no ficheiro!")