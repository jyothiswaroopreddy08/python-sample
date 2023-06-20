import unittest
from app import add_numbers

class TestApp(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEquals(result, 5)
        
if __name__ == '__main__':
    unittest.main()
