# coding: utf-8

import sys
from decimal import Decimal
from datetime import datetime


class FinancialExecution:
    def __init__(self, date_ini, date_end):
        self._total   = Decimal('0')
        self.date_ini = date_ini
        self.date_end = date_end

        self.start_date = datetime.strptime(self.date_ini, '%d/%m/%Y')
        self.end_date   = datetime.strptime(self.date_end, '%d/%m/%Y')

    def total(self):
        with open('infra/saida/data/data/ExecucaoFinanceira.csv', 'r') as data:
            for line in data:
                try:
                    info = line.split(';')
                    d_date = datetime.strptime(info[7], '%d/%m/%Y') # date

                    if (d_date >= self.start_date and
                        d_date <= self.end_date):
                        str_value = info[5] # value
                        self._total += Decimal(str_value)
                except Exception as e:
                    print('Error {} on line {}'.format(e, line))

    def str_total(self):
        print('Total expenditure beteween the dates {} {} is: {}'
            .format(self.date_ini, self.date_end, self._total))
