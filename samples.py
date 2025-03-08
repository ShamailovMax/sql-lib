from sql_funcs import SQLLibFunctions as SQLib

query = SQLib() \
    .select(['_types', 'lists', 'colbs']) \
    .from_table('tbl') \
    .where("id='291910'") \
    .build()