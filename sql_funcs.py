# functions and keywords
from typing import List, Union, Tuple
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

    def from_table(self, table: Union[str, 'SQLLibFunctions'], alias: str = None) -> 'SQLLibFunctions':
        # self.query += f'from {table} \n'
        if isinstance(table, SQLLibFunctions):
            # if subquery
            subquery = table.build()
            self.query += f'from ({subquery})'
        else:
            # if table name
            self.query += f'from {table}'

        if alias:
            self.query += f' as {alias}'
        
        self.query += ' \n'
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

    def join_tables(self, table: Union[str, 'SQLLibFunctions'], condition: str, join_type: str = 'inner', alias: str = None) -> 'SQLLibFunctions':
        # self.query += f'{join_type} join {table} on {condition} \n'
        if isinstance(table, SQLLibFunctions):
            # if subquery
            subquery = table.build()
            self.query += f'{join_type} join ({subquery})'
        else:
            # if table name
            self.query += f'{join_type} join {table}'

        if alias:
            self.query += f' as {alias}'

        self.query += f' on {condition} \n'
        return self

    def subquery(self, subquery: 'SQLLibFunctions', alias: str) -> 'SQLLibFunctions':
        self.query += f'({subquery.build()}) as {alias} \n'
        return f'({subquery})'

    def case(self, *conditions: Tuple[str, str], else_value: str = None) -> 'SQLLibFunctions':
        case_query = 'case\n'
        for condition, result in conditions:
            case_query += f'when {condition} then {result}\n'
        if else_value:
            case_query += f'else {else_value}\n'
        case_query += 'end'
        return case_query

    # window funcs support
    def over(self, partition_by: str = None, order_by: str = None) -> 'SQLLibFunctions':
        over_clause = 'over ('
        if partition_by:
            over_clause += f'partition by {partition_by} '
        if order_by:
            over_clause += f'order by {order_by}'
        over_clause += ')'
        return over_clause

    def build(self) -> str:
        self.logger.info(f'Generated SQL query: \n{self.query}')
        return self.query.strip()
