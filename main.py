menu = {
    "espresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
        },
        "custo": 1.5,
    },
    "latte": {
        "ingredientes": {
            "agua": 200,
            "leite": 150,
            "cafe": 24,
        },
        "custo": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "agua": 250,
            "leite": 100,
            "cafe": 24,
        },
        "custo": 3.0,
    }
}


def reabastercer():
    estoque["agua"] = 500
    estoque["leite"] = 300
    estoque["cafe"] = 100


def mostrar_estoque():
    print(f"""
    Agua: {estoque["agua"]}
    Leite: {estoque["leite"]}
    Café: {estoque["cafe"]}
    """)


def verifica_estoque(bebida):
    for item in bebida:
        if bebida[item] > estoque[item]:
            print(f"Desculpe Impossivel fazer essa bebida. Falta igrediente. Comunique o responsavel ")
            return False
        return True


def verifica_pagamento(preco, moeda1, moeda050, moeda025):
    global troco
    valor_total = (moeda1 * 1) + (moeda050 * 0.5) + (moeda025 * 0.25)
    troco = valor_total - preco
    if valor_total < preco:
        print("A quantia depositada não corresponde ao preço da bebida.")
        print("Colete seu dinheiro e se desejar escolha outra bebida. ")
        return False
    else:
        return True


def atualiza_estoque(bebida):
    for item in bebida:
        estoque[item] -= bebida[item]


estoque = {"agua": 0, "leite": 0, "cafe": 0}
reabastercer()
caixa = 0
maquina = True

while maquina:
    print('''O que voce Deseja?
    1 - Espresso
    2 - Latte
    3 - Cappuccino
    ''')
    escolha = input("Digite a opção desejada: ").lower()
    if escolha == "off":
        print("Até Logo.")
        break
    elif escolha == "1":
        escolha = menu["espresso"]
    elif escolha == "2":
        escolha = menu["latte"]
    elif escolha == "3":
        escolha = menu["cappuccino"]
    elif escolha == "report":
        mostrar_estoque()
        continue
    elif escolha == "refill":
        reabastercer()
        continue
    elif escolha == "caixa":
        print(f"O valor no cofre é de R${caixa: 2} ")
        continue
    else:
        print("Essa opção não existe")
        continue

    if verifica_estoque(escolha["ingredientes"]):
        print("Por Favor insira as Moedas")
        moeda1 = int(input("Quantas de 1 real: "))
        moeda05 = int(input("Quantas de 0,50 centavos: "))
        moeda025 = int(input("Quantas de 0,25 centavos: "))
        preco = escolha["custo"]
    else:
        continue

    pagamento = verifica_pagamento(preco, moeda1, moeda05, moeda025)
    if pagamento:
        caixa += escolha["custo"]
        atualiza_estoque(escolha["ingredientes"])
        print(f"Seu troco é de R${troco: 2}.")
    else:
        continue

    print("Aqui esta sua bebida. Aproveite e curta o momento")


# TODO: 1. Apresentar as opções das bebidas.
# TODO: 2. Esperar o pedido do cliente.
# TODO: 3. Verificar se ha recurso suficiente.
# TODO: 4. Solicitar o dinheiro.
# TODO: 5. Contabilizar o dinhehro.
# TODO: 6. Liberar a Bebida.
# TODO: 8. Atualizar recursos e caixa.
# TODO: 9. Voltar ao passo 1.
