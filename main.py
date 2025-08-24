limite_saque = 3
saque = 0
valor_deposito = 0
saldo =0
extrato_bancario = []


def deposito(saldo):

  valor_deposito = float(input("Digite o valor a depositar: "))
  saldo +=  valor_deposito

  extrato_bancario.append({"tipo": "✅ Depósito", "valor": valor_deposito})

  print("Deposito REALIZADO!!")

  print(f"\nSeu saldo atual é de R${saldo:.2f}")
  return saldo


def sacar(saldo, limite_saque):

    if limite_saque > 0:


        valor_saque = float(input("digite o valor a sacar: "))

        extrato_bancario.append({"tipo": "➖ Saque", "valor": valor_saque})

        if valor_saque >= 501:
            print("\nValor não permitido")

        elif valor_saque <= saldo :
           saldo  = saldo - valor_saque

           print("Saque realizado!\n")
           print(f"Saldo atual: R$: {saldo:.2f}")

           limite_saque -= 1
           
        else:
            print("Saldo Insuficiente!")

    else:
        print("Saques Insulficientes") 

    return saldo, limite_saque


def extrato():

    print("========== EXTRATO BANCÁRIO ==========")

    if not extrato_bancario :
       print("Nenhuma operação realizada")

    for operacao in extrato_bancario:
        print(f"{operacao['tipo']}: R$ {operacao['valor']:.2f}\n")

    print(f"SALDO : R$ {saldo:.2f}")
    

print("=-"*20)
print("\tBANCO TIO PATINHAS 🏦🦆")
print("=-"*20)


print("1 - Sacar 💳 \n2 - Deposito 💵 \n3 - Extrato 📝\n4 - SAIR ❌")


while True:
    op = int(input("\nDigite a opção: "))

    match op:
        case 1:
            saldo, limite_saque = sacar(saldo, limite_saque)

        case 2:
            saldo = deposito(saldo)

        case 3:
          
          extrato()


        case 4:
          print('Até mais...👋')
          break

        case _:
          print('Opção invalida 🤔')