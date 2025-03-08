# functions and keywords
from typing import List
import logging

# logging configs
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()] # console output
)

# main parent class with basic funcs and constructions
class SQLLibFunctions:
    def __init__(self):
        self.query = ''
        self.logger = logging.getLogger('SQLLibFunctions')
    
    def select(self, fields: List[str]) -> 'SQLLibFunctions':
        self.query += f'select {", ".join(fields)} \n'
        return self

    def from_table(self, table: str) -> 'SQLLibFunctions':
        self.query += f'from {table} \n'
        return self

    def where(self, condition: str) -> 'SQLLibFunctions':
        self.query += f'where {condition} \n'
        return self

    def group_by(self, fields: List[str]) -> 'SQLLibFunctions':
        self.query += f'group by {", ".join(fields)} \n'
        return self

    def order_by(self, fields: List[str], sort_order: str = 'asc') -> 'SQLLibFunctions':
        self.query += f'order by {", ".join(fields)} {sort_order} \n'
        return self

    def having(self, condition: str) -> 'SQLLibFunctions':
        self.query += f'having {condition} \n'
        return self
    
    def limit(self, limit: int) -> 'SQLLibFunctions':
        self.query += f'limit {limit} \n'
        return self
    
    def offset(self, offset: int) -> 'SQLLibFunctions':
        self.query += f'offset {offset} \n'
        return self

    def over(partition_by: str) -> 'SQLLibFunctions':
        pass

    def build(self) -> str:
        self.logger.info(f'Generated SQL query: \n{self.query}')
        return self.query
