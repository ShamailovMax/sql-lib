# functions and keywords
from typing import List


class SQLLibFunctions:
    def __init__(self):
        self.query = ''
    
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

    def build(self):
        return self.query
