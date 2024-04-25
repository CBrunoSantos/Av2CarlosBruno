# test_transaction.py

import unittest
from transaction import cash_transaction, bank_transfer, credit_transaction

class TestTransaction(unittest.TestCase):
    def test_cash_transaction(self):
        # Simula uma transação em dinheiro
        transaction_steps = cash_transaction()
        expected_steps = [
            "Receive cash amount: 100",
            "Print payment receipt",
            "Receipt for payment of $100.",
            "Complete transaction"
        ]
        self.assertEqual([step() for step in transaction_steps], expected_steps)

    def test_bank_transfer(self):
        # Simula uma transferência bancária
        transaction_steps = bank_transfer()
        expected_steps = [
            "Provide bank deposit details",
            "Confirm payment approval from bank",
            "Close transaction"
        ]
        self.assertEqual([step() for step in transaction_steps], expected_steps)

    def test_credit_transaction(self):
        # Simula uma transação de crédito
        transaction_steps = credit_transaction()
        expected_steps = [
            "Request credit account details - Name: Test Account Account Number: 1234",
            "Request payment from bank - Value: 200",
            "Confirm payment approval from bank",
            "Close transaction"
        ]
        self.assertEqual([step() for step in transaction_steps], expected_steps)

def test_stress():
    for _ in range(1000):
        transaction_steps = cash_transaction()
        for step in transaction_steps:
            step()

if __name__ == "__main__":
    unittest.main()
