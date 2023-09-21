# solicita 3 entradas de ativos numa lista os ordena e imprime os dados
ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)
    ativos.sort()
#Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for elemento in ativos:
    print(elemento)
