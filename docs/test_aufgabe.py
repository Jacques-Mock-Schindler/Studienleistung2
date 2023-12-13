import unittest
from unittest.mock import patch
from io import StringIO
from typing import get_type_hints

from aufgabe import _earnings, return_on_investment
# from rendite import _earnings, return_on_investment

class TestRendite(unittest.TestCase):
    def test_earnings(self):
        self.assertEqual(_earnings(100, 200), 100)
        self.assertEqual(_earnings(100, 100), 0)
        self.assertEqual(_earnings(100, 50), -50)
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_statement(self, mock_stdout):
        return_on_investment(100, 200, 1000)
        self.assertEqual(mock_stdout.getvalue(), 'The RoI is 10.00%.\n')

    def test_return_on_investment(self):
        self.assertEqual(return_on_investment(100, 200, 1000), 10)
        self.assertEqual(return_on_investment(100, 200, 100), 100)
        self.assertEqual(return_on_investment(100, 200, 200), 50)
        self.assertEqual(return_on_investment(200, 140, 300), -20)
        
    def test_type_hints_eranings(self):
        erwartete_hints = {'expenses': float, 'income': float, 'return': float}
        tatsaechliche_hints = get_type_hints(_earnings)
        self.assertEqual(erwartete_hints, tatsaechliche_hints)
        
    def test_type_hints_return_on_investment(self):
        erwartete_hints = {'expenses': float, 'income': float, 'investment': float, 'return': float}
        tatsaechliche_hints = get_type_hints(return_on_investment)
        self.assertEqual(erwartete_hints, tatsaechliche_hints)
        
if __name__ == '__main__':
    unittest.main()