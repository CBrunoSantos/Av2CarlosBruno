from functools import partial

# Definindo funções Lambda para cada etapa do processo

# Função para transação em dinheiro
def dinheiro(amount):
    return [
        partial(print, "Valor recebido:", amount),
        partial(print, "Receita do pagamento: ${}.".format(amount)),
        partial(print, "Transação completa")
    ]

# Função para transferência bancária
def transferenciaBancaria():
    return [
        partial(print, "Forneça detalhes de depósito bancário"),
        [
            partial(print, "Confirmando aprovação de pagamento do banco"),
            partial(print, "Fechando transação")
        ]
    ]

# Função para transação de crédito
def credito(account_name, account_number, payment_value):
    return [
        partial(print, "Solicitar dados da conta de crédito - Nome:", account_name, "Número de conta:", account_number),
        [
            partial(print, "Solicitar pagamento ao banco - Valor:", payment_value),
            partial(print, "Confirme a aprovação do pagamento do banco"),
            partial(print, "Fechar transação")
        ]
    ]

# Função principal para criar a transação com base no tipo
def create_transaction(transaction_type):
    if transaction_type == 'dinheiro':
        amount = int(input("Digite o valor do pagamento: "))
        return dinheiro(amount)
    elif transaction_type == 'transferenciaBancaria':
        return transferenciaBancaria()
    elif transaction_type == 'credito':
        account_name = input("Digite o nome da conta: ")
        account_number = input("Digite o número da conta: ")
        payment_value = int(input("Digite o valor do pagamento: "))
        return credito(account_name, account_number, payment_value)
    else:
        raise ValueError("Tipo de transação inválido")

# Exemplo de uso:
transaction_type = input("Digite o tipo de transação (dinheiro, transferenciaBancaria, credito): ")
transaction_steps = create_transaction(transaction_type)
for step in transaction_steps:
    if isinstance(step, list):
        for sub_step in step:
            sub_step()
    else:
        step()
