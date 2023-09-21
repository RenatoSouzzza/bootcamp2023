# le saldo e valor do saque e se o saldo é suficiente 
# informa o valor do saque e saldo novo saldo. Se não
# informa que o saldo é insuficiente
 
# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

#Criar as condições necessárias para impressão da saída, vide tabela de exemplos.
if (valor_saque <= saldo_total):
    print(f'Saque realizado com sucesso. Novo Saldo: {saldo_total-valor_saque}')
else:
    print('Saldo insuficiente. Saque não realizado!')
