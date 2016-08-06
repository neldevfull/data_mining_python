# coding: utf-8

import sys
from decimal import Decimal
from datetime import datetime, timedelta


class FinancialExecution:
    def total(self, date_ini, date_end):
        total = Decimal('0')
        start_date = datetime.strptime(date_ini, '%d/%m/%Y')
        end_date   = datetime.strptime(date_end, '%d/%m/%Y')

        with open('infra/saida/data/data/ExecucaoFinanceira.csv', 'r') as data:
            for line in data:
                try:
                    info = line.split(';')
                    d_date = datetime.strptime(info[7], '%d/%m/%Y') # date

                    if (d_date >= start_date and
                        d_date <= end_date):
                        str_value = info[5] # value
                        total += Decimal(str_value)
                except Exception as e:
                    print('Error {} on line {}'.format(e, line))

        print('Total expenditure beteween the dates {} {} is: {}'
            .format(date_ini, date_end, total))

    def signature_interval(self):
        totals = {2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0, 2015: 0}

        for year in totals.keys():
            year_start = datetime(year, 1, 1)
            year_end   = year_start + timedelta(days=365)

            with open('infra/saida/data/data/ExecucaoFinanceira.csv', 'r') as data:
                for line in data:
                    try:
                        info = line.split(';')
                        start_date = datetime.strptime(info[8], '%d/%m/%Y')
                        end_date = datetime.strptime(info[9], '%d/%m/%Y')

                        if start_date > year_start and end_date < year_end:
                            totals[year] += 1
                    except Exception as e:
                        print('Error {} on line {}'.format(e, line))

        for year, signed in totals.items():
            print('{} financial executions in {}'.format(signed, year))
