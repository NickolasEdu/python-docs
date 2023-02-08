print("\n******************* Calculadora em Python *******************")

print('Escolha uma das operações a seguir:\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão')

operation = int(input("Insira um número: "))

def chooseOperator(arg):
    
    if operation > 4:
        print('Número selecionado não tem relação com nenhuma operação, por favor tente um valor válido')
    elif operation == 3:
        print('Operação de Multiplicação selecionada')
    elif operation == 4:
        print('Operação de Divisão selecionada')
    elif operation == 2:
        print('Operação de Subtração selecionada')
    elif operation == 1:
        print('Operação de soma selecionada')
    else:
        print('Número selecionado não tem relação com nenhuma operação, por favor tente um valor válido')
    
chooseOperator(operation)

##

first_op = int(input('Primeiro número da operação:'))
sec_op = int(input('Segundo número da operação:'))

# Função que vai chamar uma função que chama as funções determindas
def operating(num1, num2):
    
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        return num1 * num2
    elif operation == 4:
        return num1 / num2
    else:
        print('Uma operação inválida foi selecionada')
        
result = operating(first_op, sec_op)
print(result)