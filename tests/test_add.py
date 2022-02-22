from Demo.demo.add import add
from unittest import TestCase

class TestAdd(TestCase):
    def test_addition(self):
        result = add(2, 3)
        self.assertEqual(result, 5)
    
    def test_addition_of_strings(self):
        result = add('2', '3')
        self.assertEqual(result, 5)