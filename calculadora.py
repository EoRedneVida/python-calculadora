def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida."

def main():
    print("Bem-vindo à calculadora!")
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
        return

    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Digite o número da operação desejada: ")

    if operacao == '1':
        resultado = soma(num1, num2)
    elif operacao == '2':
        resultado = subtracao(num1, num2)
    elif operacao == '3':
        resultado = multiplicacao(num1, num2)
    elif operacao == '4':
        resultado = divisao(num1, num2)
    else:
        print("Operação inválida. Digite um número válido!")
        return

    print(f"O resultado da operação é: {resultado}")

if __name__ == "__main__":
    main()