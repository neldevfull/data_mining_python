# coding: utf-8

from decimal import Decimal


class FinancialExecution:
    def total(self):
        total = Decimal('0')

        with open('infra/saida/data/data/ExecucaoFinanceira.csv', 'r') as data:
            for line in data:
                try:
                    info = line.split(';')
                    str_value = info[5] # value is fifth
                    total += Decimal(str_value)
                except Exception as e:
                    print('Error {} on line {}'.format(e, line))

        print('Total spent: {}'.format(total))