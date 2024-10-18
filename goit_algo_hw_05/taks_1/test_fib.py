import unittest
from main import caching_fibonacci
class TestCachingFibonacci(unittest.TestCase):
    
    def setUp(self):
        '''restart initial values'''
        self.fib = caching_fibonacci()
    
    def test_fib_0(self):
        self.assertEqual(self.fib(0), 0) 
    
    def test_fib_1(self):
        self.assertEqual(self.fib(1), 1)
    
    def test_fib_5(self):
        self.assertEqual(self.fib(5), 5)
    
    def test_fib_10(self):
        self.assertEqual(self.fib(10), 55)
    
    def test_fib_15(self):
        self.assertEqual(self.fib(15), 610)

    def test_negative_value(self):
        self.assertEqual(self.fib(-5), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
