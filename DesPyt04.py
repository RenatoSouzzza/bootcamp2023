valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

def calcjur(valor_inicial, taxa_juros, periodo):
    montante = valor_inicial*(1+taxa_juros) **periodo
    return montante
total = calcjur(valor_inicial, taxa_juros, periodo)
print(f"Valor final do investimento: R$ {total:.2f}")