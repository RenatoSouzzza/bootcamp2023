# Demonstrativo - Programa que le o salário do funcionário 
# e calcula o valor a ser recebido considerando o desconto de impostos
# de acordo com a alíquota e com o acréscimo de benefícios

def calculo_imposto(salario):
    aliquota = 0.00
    if salario == 0 and salario <= 1100:
        aliquota = 0.05
    elif salario > 1100.01 and salario <= 2500:
        aliquota = 0.10
    else:
        aliquota = 0.15
    return aliquota * salario

salario = float(input('Informe o salário: R$ '))
beneficios = float(input('Informe o valor dos benefícios R$: '))
impostos = calculo_imposto(salario)
liquido = (salario - impostos) + beneficios

print(f'O valor a ser recebido pelo funcionário é R$ {liquido:.2f}')

