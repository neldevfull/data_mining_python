# coding: utf-8

import unittest
from column import Column
from data_table import DataTable


class TestColumn(unittest.TestCase):
    def test_validate_bigint(self):
        self.assertTrue(Column.validate('bigint', 100))
        self.assertTrue(not Column.validate('bigint', 10.1))
        self.assertTrue(not Column.validate('bigint', 'Text'))

    def test_validate_numeric(self):
        self.assertTrue(Column.validate('numeric', 10.1))
        self.assertTrue(Column.validate('numeric', 100))
        self.assertTrue(not Column.validate('numeric', 'Text'))

    def test_validate_varchar(self):
        self.assertTrue(Column.validate('varchar', 'Text'))
        self.assertTrue(not Column.validate('varchar', 10.1))
        self.assertTrue(not Column.validate('varchar', 100))


class TestDataTable(unittest.TestCase):
    def setUp(self):
        self.table = DataTable('TestTable')

    def test_add_column(self):
        self.assertEqual(0, len(self.table._columns))

        self.table.add_column('id', 'bigint')
        self.assertEqual(1, len(self.table._columns))

        self.table.add_column('value', 'numeric')
        self.assertEqual(2, len(self.table._columns))

        self.table.add_column('desc', 'varchar')
        self.assertEqual(3, len(self.table._columns))

    def test_add_column_invalid_type(self):
        self.assertRaises(
            Exception,
            self.table.add_column,
            ('col', 'date')
        )

    def test_add_column_invalid_type_fail(self):
        error = False

        try:
            self.table.add_column('col', 'date')
        except:
            error = True

        if not error:
            self.fail('method not raise exeception, but it should')


if __name__ == '__main__':
    unittest.main()