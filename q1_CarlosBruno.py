# Definindo funções Lambda para cada etapa do processo

# Modificando a função cash_transaction
def dinheiro():
    amount = int(input("Digite o valor do pagamento: "))
    return [
        lambda: print("Valor recebido:", amount),
        lambda: print("Receita do pagamento"),
        lambda: "Receita do pagamento é ${}.".format(amount),
        lambda: print("Transação completa")
    ]


# Função para transferência bancária
transferenciaBancaria = lambda: (
    lambda: print("Provide bank deposit details"),
    lambda: (
        lambda: print("Confirmando aprovação de pagamento do banco"),
        lambda: print("Fechando transação")
    )
)

# Função para transação de crédito
def credito():
    account_name = input("Digite o nome da conta: ")
    account_number = input("Digite o número da conta: ")
    return [
        lambda: print("Request credit account details - Name:", account_name, "Account Number:", account_number),
        lambda: (
            lambda payment_value: [
                lambda: print("Request payment from bank - Value:", payment_value),
                lambda: (
                    lambda: print("Confirm payment approval from bank"),
                    lambda: print("Close transaction")
                )
            ]
        )(amount = int(input("Digite o valor do pagamento: ")))
    ]

# Função principal para criar a transação com base no tipo
def create_transaction(transaction_type):
    return {
        'dinheiro': dinheiro,
        'transferenciaBancaria': transferenciaBancaria,
        'credito': credito
    }[transaction_type]()

# Exemplo de uso:
transaction_type = input("Digite o tipo de transação (dinheiro, transferenciaBancaria, credito): ")
transaction_steps = create_transaction(transaction_type)
for step in transaction_steps:
    step()
    
