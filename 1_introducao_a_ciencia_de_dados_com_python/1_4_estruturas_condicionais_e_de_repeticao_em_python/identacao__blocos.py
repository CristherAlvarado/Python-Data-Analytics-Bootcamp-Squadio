saldo = 500

def sacar(valor):
    if saldo >= valor:
        print("Valor Sacado!")
        print("Retire seu dinheiro no lugar indicado.")

    print("Obrigado por ser nosso cliente")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(900)