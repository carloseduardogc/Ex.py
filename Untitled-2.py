def soma(a, b):
   return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b) :
    return a * b

def divisao(a, b) :
    if b != 0 :
        return a / b
    else:
        return "não é possível dividir por 0"

print("selecione a operacao")
print("1. soma")
print("2. subtracao")
print("3. multiplicacao")
print("4. divisao")

opcao= input("qual sua escolha :")

num1 = int(input("primeiro digito:"))
num2 = int(input("segundo digito:"))

if opcao == '1':
    print('resultado:', soma(num1, num2))
elif opcao == '2':
    print('resultado:', subtracao(num1, num2))
elif opcao == '3':
    print('resultado:', multiplicacao(num1, num2))
elif opcao == '4':
    print('resultado:', divisao(num1, num2))
else:
    print("opcao nao e valida")


