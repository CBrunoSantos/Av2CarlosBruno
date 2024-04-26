from functools import partial

# Função para transação em dinheiro
dinheiro = lambda amount: [
    partial(print, "Valor recebido:", amount),
    partial(print, f"Receita do pagamento: ${amount}."),
    partial(print, "Transação completa")
]

# Função para transferência bancária
transferenciaBancaria = lambda: [
    partial(print, "Forneça detalhes de depósito bancário"),
    [
        partial(print, "Confirmando aprovação de pagamento do banco"),
        partial(print, "Fechando transação")
    ]
]

# Função para transação de crédito
credito = lambda account_name, account_number, payment_value: [
    partial(print, "Solicitar dados da conta de crédito - Nome:", account_name, "Número de conta:", account_number),
    [
        partial(print, "Solicitar pagamento ao banco - Valor:", payment_value),
        partial(print, "Confirme a aprovação do pagamento do banco"),
        partial(print, "Fechar transação")
    ]
]

# Função principal para criar a transação com base no tipo
create_transaction = lambda transaction_type: (
    dinheiro(int(input("Digite o valor do pagamento: "))) if transaction_type == 'dinheiro' else
    transferenciaBancaria() if transaction_type == 'transferenciaBancaria' else
    credito(input("Digite o nome da conta: "), input("Digite o número da conta: "), int(input("Digite o valor do pagamento: "))) if transaction_type == 'credito' else
    None
)

# Exemplo de uso:
transaction_type = input("Digite o tipo de transação (dinheiro, transferenciaBancaria, credito): ")
transaction_steps = create_transaction(transaction_type)
for step in transaction_steps:
    if isinstance(step, list):
        for sub_step in step:
            sub_step()
    else:
        step()
