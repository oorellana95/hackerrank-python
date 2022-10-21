# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd


def print_hi(name):
    data = {'fields': ['cik', 'name', 'ticker', 'exchange'],
            'data': [[320193, 'Apple Inc.', 'AAPL', 'Nasdaq'],
                     [789019, 'MICROSOFT CORP', 'MSFT', 'Nasdaq'],
                     [1067983, 'BERKSHIRE HATHAWAY INC', 'BRK-B', 'NYSE'],
                     [731766, 'UNITEDHEALTH GROUP INC', 'UNH', 'NYSE']]}

    df = pd.DataFrame(data=data.get('data'), columns=data.get('fields'))
    dict = df.to_dict(orient='records')

    print(dict)  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
