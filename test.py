# coding: utf-8

import unittest
from column import Column


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


if __name__ == '__main__':
    unittest.main()