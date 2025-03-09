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

# join example
query_4 = SQLib() \
    .select(['*']) \
    .from_table('users') \
    .join_tables('orders', 'users.id = orders.user_id', 'LEFT') \
    .build()

# subquery example
subquery = SQLib().select(['user_id']).from_table('orders').where('amount > 100')
query_5 = SQLib() \
    .select(['*']) \
    .from_table(subquery, 'high_value_orders') \
    .build()

# case-when condition example
query_6 = SQLib() \
    .select([
        'name',
        SQLib().case(
            ('age < 18', "'Minor'"),
            ('age BETWEEN 18 AND 65', "'Adult'"),
            else_value="'Senior'"
        ) + ' AS age_group'
    ]) \
    .from_table('users') \
    .build()