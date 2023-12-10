import unittest

from rendite import _earnings, return_on_investment

class TestRendite(unittest.TestCase):
    def test_earnings(self):
        self.assertEqual(_earnings(100, 200), 100)
        self.assertEqual(_earnings(100, 100), 0)
        self.assertEqual(_earnings(100, 50), -50)

    def test_return_on_investment(self):
        self.assertEqual(return_on_investment(100, 200, 1000), 10)
        self.assertEqual(return_on_investment(100, 200, 100), 100)
        self.assertEqual(return_on_investment(100, 200, 200), 50)
        self.assertEqual(return_on_investment(200, 140, 300), -20)
        
if __name__ == '__main__':
    unittest.main()