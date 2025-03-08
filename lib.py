# functions and keywords
from typing import List

def select(fields: List[str]) -> str:
    return f'select {fields}'

def from_() -> str:
    pass

def where() -> str:
    pass

def group_by() -> str:
    pass

def order_by() -> str:
    pass

def having() -> str:
    pass

def over(partition_by: str) -> str:
    pass

# sample
print(select(['*']))