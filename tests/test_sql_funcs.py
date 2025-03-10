# Новый корректный импорт
from core.sql_funcs import SQLLibFunctions

# Пример использования
qq = SQLLibFunctions()
qq.select(['*']).build()