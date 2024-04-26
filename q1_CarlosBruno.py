from functools import partial

dinheiro = lambda amount: [
    partial(print, "Valor recebido:", amount),
    partial(print, f"Receita do pagamento: ${amount}."),
    partial(print, "Transação completa")
]

transferenciaBancaria = lambda: [
    partial(print, "Forneça detalhes de depósito bancário"),
    [
        partial(print, "Confirmando aprovação de pagamento do banco"),
        partial(print, "Fechando transação")
    ]
]

credito = lambda account_name, account_number, payment_value: [
    partial(print, "Solicitar dados da conta de crédito - Nome:", account_name, "Número de conta:", account_number),
    [
        partial(print, "Solicitar pagamento ao banco - Valor:", payment_value),
        partial(print, "Confirme a aprovação do pagamento do banco"),
        partial(print, "Fechar transação")
    ]
]

create_transaction = lambda transaction_type: (
    dinheiro(int(input("Digite o valor do pagamento: "))) if transaction_type == 'dinheiro' else
    transferenciaBancaria() if transaction_type == 'transferenciaBancaria' else
    credito(input("Digite o nome da conta: "), input("Digite o número da conta: "), int(input("Digite o valor do pagamento: "))) if transaction_type == 'credito' else
    None
)

transaction_type = input("Digite o tipo de transação (dinheiro, transferenciaBancaria, credito): ")
transaction_steps = create_transaction(transaction_type)
for step in transaction_steps:
    if isinstance(step, list):
        for sub_step in step:
            sub_step()
    else:
        step()
