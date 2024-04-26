from flask import Flask, request, jsonify
from functools import partial
import bcrypt
import mysql.connector

app = Flask(__name__)

connect_to_database = lambda: (
    (lambda connection: (
        print("Conexão ao banco de dados bem-sucedida.") or connection
    ))(mysql.connector.connect(
        host='localhost',
        user='root',
        password='Br041100!',
        database="tabelacinco"
    )) or None
)

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

create_transaction = lambda transaction_type, amount=None, account_name=None, account_number=None, payment_value=None: (
    dinheiro(amount) if transaction_type == 'dinheiro' else
    transferenciaBancaria() if transaction_type == 'transferenciaBancaria' else
    credito(account_name, account_number, payment_value) if transaction_type == 'credito' else
    None
)

@app.route('/create_transaction', methods=['POST'])
def handle_create_transaction():
    transaction_type = request.form['transaction_type']
    transaction_steps = create_transaction(transaction_type)
    response = {'steps': []}
    for step in transaction_steps:
        if isinstance(step, list):
            for sub_step in step:
                response['steps'].append(sub_step())
        else:
            response['steps'].append(step())
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
