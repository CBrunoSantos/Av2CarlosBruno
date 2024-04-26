import unittest
from io import StringIO
from unittest.mock import patch
from q1_CarlosBruno import dinheiro, transferenciaBancaria, credito, create_transaction

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.stdout = StringIO()
        self.patcher = patch('sys.stdout', new=self.stdout)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def assertFunctionListEqual(self, a, e):
        """Método auxiliar para verificar se duas listas de funções são equivalentes."""
        self.assertEqual(len(a), len(e))
        for step, expected in zip(a, e):
            if isinstance(step, list) and isinstance(expected, list):
                self.assertFunctionListEqual(step, expected)
            else:
                self.assertEqual(step(), expected())

    def test_dinheiro_transaction(self):
        amount = 20
        transaction_steps = dinheiro(amount)
        
        expected_steps = [
            lambda: print("Valor recebido:", amount),
            lambda: print(f"Receita do pagamento: ${amount}."),
            lambda: print("Transação completa")
        ]
        
        self.assertFunctionListEqual(transaction_steps, expected_steps)

    def test_bank_transfer_transaction(self):
        transaction_steps = transferenciaBancaria()

        expected_steps = [
            lambda: print("Forneça detalhes de depósito bancário"),
            [
                lambda: print("Confirmando aprovação de pagamento do banco"),
                lambda: print("Fechando transação")
            ]
        ]

        self.assertFunctionListEqual(transaction_steps, expected_steps)

    def test_credit_transaction(self):
        account_name = "Test Account"
        account_number = "1234"
        payment_value = 200

        transaction_steps = credito(account_name, account_number, payment_value)

        expected_steps = [
            lambda: print(f"Solicitar dados da conta de crédito - Nome: {account_name} Número de conta: {account_number}"),
            [
                lambda: print(f"Solicitar pagamento ao banco - Valor: {payment_value}"),
                lambda: print("Confirme a aprovação do pagamento do banco"),
                lambda: print("Fechar transação")
            ]
        ]

        self.assertFunctionListEqual(transaction_steps, expected_steps)

    def test_stress(self):
        num_transactions = 1
        for _ in range(num_transactions):
            transaction_type = "dinheiro"
            transaction_steps = create_transaction(transaction_type)
            for step in transaction_steps:
                if isinstance(step, list):
                    for sub_step in step:
                        sub_step()
                else:
                    step()

if __name__ == "__main__":
    unittest.main()
