# coding: utf-8

import unittest


class TestExample(unittest.TestCase):
    def setUp(self):
        # Add cleanup action
        self.addCleanup(self.my_cleanup, ('cleanup run...'))
        self.out_file = open()

    def my_cleanup(self, msg):
        print(msg)

    def test_add_column(self):
        pass

    def tearDown(self):
        print('Never run!')


if __name__ == '__main__':
    unittest.main()