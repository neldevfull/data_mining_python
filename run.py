from apps import Table


if __name__ == '__main__':
    table  = Table('Customer')
    table.add_column('customer_id', 'bigint')

    print(table.columns)