import unittest
from core.sql_funcs import SQLLibFunctions

# select method test
class TestSelectMethod(unittest.TestCase):
    # created setUp method not to repeat my code
    def setUp(self):
        self.sql_builder = SQLLibFunctions()
        
    def test_select_single_field(self):
        result = self.sql_builder.select(['name'])
        self.assertEqual(result.query, 'select name \n')
        self.assertIsInstance(result, SQLLibFunctions)
        
    def test_select_multiple_fields(self):
        result = self.sql_builder.select(['name', 'age', 'email'])
        self.assertEqual(result.query, 'select name, age, email \n')
        self.assertIsInstance(result, SQLLibFunctions)
        
    
if __name__ == "__main__":
    unittest.main()
