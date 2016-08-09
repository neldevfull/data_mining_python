# coding: utf-8

import sys
from decimal import Decimal
from datetime import datetime, timedelta


class Base:
    def dec(self, element, index):
        try:
            return Decimal(element[index])
        except:
            return Decimal('0')

class Value(Base):
    def __init__(self):
        self._total = Decimal('0')
        self.schema = ('NumDocumento', 'ValContrato')
        self.result = None

    def value(self):
        with open('infra/saida/data/data/ExecucaoFinanceira.csv', 'r') as data_file:
            splited_data = [line.split(';') for line in data_file]
            data = [(element[2], self.dec(element, 12)) for element in
                splited_data if len(element) > 2]
            self.result = [{key:value for key, value in zip(self.schema, element)}
                for element in data]

    def str_value(self):
        for info_dict in self.result:
            print("{}".format(info_dict))

class QueryFile(Base):
    """To run class
    query = QueryFile('infra/saida/data/data/ExecucaoFinanceira.csv')
    total = sum(query.dec(element, 5) for element in query)
    print('Total: {}'.format(total))
    """
    def __init__(self, filename):
        self._file = open(filename, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        data = self._file.readline()
        if not data:
            self._file.close()
            raise StopIteration
        return data.split(';')


class FinancialExecution:
    def get_id_and_value(self, info, lower):
        value = Decimal(info[5])

        if value > lower:
            return info[2], value
        return None, Decimal(0)

    def companies_received(self):
        all_companies = set()
        intervals = [
            (Decimal('1000000000'), set()),
            (Decimal('500000000'), set()),
            (Decimal('100000000'), set()),
            (Decimal('10000000'), set()),
            (Decimal('1000000'), set()),
            (Decimal('1000'), set())
        ]

        for lower, companies in intervals:
            data = open('infra/saida/data/data/ExecucaoFinanceira.csv', 'r')
            for line in data:
                info = line.strip().split(';')
                company_id, contract_value = self.get_id_and_value(info, lower)

                if company_id and not company_id in all_companies:
                    companies.add(company_id)
                    all_companies.add(company_id)

        data.close()

        for lower, companies in intervals:
            print("{} companies received more than {}".format(len(companies), lower))
        print("{} companies total".format(len(all_companies)))

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
