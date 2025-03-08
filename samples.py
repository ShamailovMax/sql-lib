from sql_funcs import SQLLibFunctions as SQLib

query = SQLib() \
    .select(['_types', 'lists', 'colbs']) \
    .from_table('tbl') \
    .where("id='291910'") \
    .build()

query_2 = SQLib() \
    .select(['*']) \
    .from_table('tbl_2') \
    .group_by(['uid']) \
    .build()

query_3 = SQLib() \
    .select(['*']) \
    .from_table('tbl_3') \
    .order_by(['uid'], sort_order='desc') \
    .build()