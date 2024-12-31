import unittest
from greet.simple_function import greet_name

class TestSimpleFunction(unittest.TestCase):
    def test_greet_name(self):
        self.assertEqual(greet_name("Alice"), "Hello, Alice ! Welcome to the library !!!")

if __name__ == "__main__":
    unittest.main()
