#Atribuição
saldo = 500

print("Saldo Atual: R$", saldo)
deposito = int(input("Digite o valor de seu deposito: R$"))

#Atribuição com Soma
saldo += deposito

print("Seu novo saldo é de R$", saldo)
saque = int(input("Digite o valor do seu saque:"))

#Atribuição com Subtração
saldo -= saque
print("Você sacou: R$", saque, "Seu novo saldo é de: R$", saldo)

# -- OUTROS OPERADORES DE ATRIBUBIÇÃO --
var_teste = 1
var_teste_2 = 2

#Atribubição com Divisão
var_teste_2 /= 1

#Atribubição com Divisão Inteira
var_teste //= 1

#Atribubição com Multiplicação
var_teste *= 50