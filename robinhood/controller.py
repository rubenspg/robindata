import robin_stocks.robinhood as rh
import models.transaction as t
from datetime import datetime
import csv

class Controller(object):
    def __get_date_to_sort__(self,e):
        return datetime.timestamp(e.date)

    def get_all_transactions(self):
        all_transactions = []

        with open('data/test_data.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                if row[0] == 'symbol':
                    continue
                all_transactions.append(
                    t.Transaction(
                        str(row[0]),
                        # 2021-04-01T13:43:00.607000Z
                        datetime.strptime(row[1], '%Y-%m-%dT%H:%M:%S.%fZ'),
                        str(row[2]),
                        str(row[3]),
                        float(row[4]),
                        float(row[5]),
                        float(row[6])
                    )
                )
        sort = sorted(all_transactions, key=self.__get_date_to_sort__)
        return sort
