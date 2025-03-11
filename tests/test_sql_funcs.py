import unittest
from core.sql_funcs import SQLLibFunctions

# select method test
class TestSQLlibFunctions(unittest.TestCase):
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
        
    def test_from_table(self):
        result = self.sql_builder.from_table('cars')
        self.assertEqual(result.query, 'from cars \n')
        self.assertIsInstance(result, SQLLibFunctions)
        
    def test_from_table_with_subquery(self):
        subquery = SQLLibFunctions().select(['order']).from_table('services')
        result = self.sql_builder.from_table(subquery)
        self.assertEqual(result.query, 'from (select order \nfrom services) \n')
        self.assertIsInstance(result, SQLLibFunctions)
        
    def test_where(self):
        result = self.sql_builder.where('age >= 21')
        self.assertEqual(result.query, 'where age >= 21 \n')
        self.assertIsInstance(result, SQLLibFunctions)
        
    
if __name__ == "__main__":
    unittest.main()
