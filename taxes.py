#!/usr/bin/env python3

import logging

bracketTable = [{
    'low': 0,
    'high': 3000,
    'percents': 0
}, {
    'low': 3000,
    'high': 5000,
    'percents': 10
}, {
    'low': 5000,
    'high': 8000,
    'percents': 20
}, {
    'low': 8000,
    'high': 10000,
    'percents': 30
}, {
    'low': 10000,
    'high': float('inf'),
    'percents': 40
}]

# safety check: verify that the list is sorted
bracketTable.sort(key=lambda k: k['low'])


def calcTax(salary: int) -> float:
    tax = 0
    for row in bracketTable:
        if salary <= row['low']:
            break  # there is no need to proceed higher levels
        result = (min(salary, row['high']) -
                  row['low']) * row['percents'] / 100
        tax += result
        logging.debug('{low:5} - {high:5} {percents:3}% => {result}'.format(
            low=row['low'],
            high=row['high'],
            percents=row['percents'],
            result=result))
    # logging.debug('Total taxes for salary of {s}: {t}'.format(s=salary, t=tax))
    return tax


if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s:%(message)s',
                        level=logging.DEBUG)
    salary = input('Please enter salary: ')
    print('You should pay {t} in tax.'.format(t=calcTax(int(salary))))
