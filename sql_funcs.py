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

    def where(self, condition: str) -> str:
        self.query += f'where {condition} \n'
        return self

    def group_by() -> str:
        pass

    def order_by() -> str:
        pass

    def having() -> str:
        pass

    def over(partition_by: str) -> str:
        pass

    def build(self) -> str:
        self.logger.info(f'Generated SQL query: \n{self.query}')
        return self.query
