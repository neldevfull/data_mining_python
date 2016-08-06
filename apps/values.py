# coding: utf-8

import sys
from decimal import Decimal
from datetime import date


class FinancialExecution:
    def __init__(self, date_ini, date_end):
        self.date_ini = date_ini
        self.date_end = date_end

        dateini = date_ini.split('/')
        dateend = date_end.split('/')

        self._total = Decimal('0')
        self.start_date = date(int(dateini[2]), int(dateini[1]), int(dateini[0]))
        self.end_date   = date(int(dateend[2]), int(dateend[1]), int(dateend[0]))

    def _mount_date(self, str_date):
            year  = int(str_date.split('/')[2])
            month = int(str_date.split('/')[1])
            day   = int(str_date.split('/')[0])

            return date(year, month, day)

    def total(self):
        with open('infra/saida/data/data/ExecucaoFinanceira.csv', 'r') as data:
            for line in data:
                try:
                    info = line.split(';')
                    d_date = self._mount_date(info[7]) # date

                    if (d_date >= self.start_date and
                        d_date <= self.end_date):
                        str_value = info[5] # value
                        self._total += Decimal(str_value)
                except Exception as e:
                    print('Error {} on line {}'.format(e, line))

    def str_total(self):
        print('Total expenditure beteween the dates {} {} is: {}'
            .format(self.date_ini, self.date_end, self._total))
