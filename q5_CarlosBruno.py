from flask import Flask, request, jsonify
from functools import partial
import bcrypt  # Biblioteca para criptografia de senha
import mysql.connector

app = Flask(__name__)

# Configuração da conexão com o banco de dados
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Br041100!',
            database="tabelacinco"
        )
        print("Conexão ao banco de dados bem-sucedida.")
        return connection
    except mysql.connector.Error as error:
        print(f"Erro ao conectar ao banco de dados: {error}")
        return None

# Função para criar uma transação em dinheiro
def dinheiro(amount):
    return [
        partial(print, "Valor recebido:", amount),
        partial(print, "Receita do pagamento: ${}.".format(amount)),
        partial(print, "Transação completa")
    ]

# Função para criar uma transferência bancária
def transferenciaBancaria():
    return [
        partial(print, "Forneça detalhes de depósito bancário"),
        [
            partial(print, "Confirmando aprovação de pagamento do banco"),
            partial(print, "Fechando transação")
        ]
    ]

# Função para criar uma transação de crédito
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
def create_transaction(transaction_type, amount=None, account_name=None, account_number=None, payment_value=None):
    if transaction_type == 'dinheiro':
        if amount is None:
            amount = int(request.form['amount'])
        return dinheiro(amount)
    elif transaction_type == 'transferenciaBancaria':
        return transferenciaBancaria()
    elif transaction_type == 'credito':
        if account_name is None:
            account_name = request.form['account_name']
            account_number = request.form['account_number']
            payment_value = int(request.form['payment_value'])
        return credito(account_name, account_number, payment_value)
    else:
        raise ValueError("Tipo de transação inválido")

# Rota para criar uma transação
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
