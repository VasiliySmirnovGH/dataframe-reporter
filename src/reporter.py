import pandas as pd

class DataFrameReporter:
    def __init__(self, float_format='0.05f', percent_format='0.02%', include_all=False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all

    def show_report(self, df, title=None):
        if title != None:
            print(title)
        print(f'Количество столбцов: {df.shape[1]}')
        print(f'Количество строк: {df.shape[0]}')
        print(f'Количество дубликатов: {df.duplicated().sum()}')
        print(f'Доля дубликатов: {format(df.duplicated().sum()/df.shape[0], self.percent_format)}')


reporter = DataFrameReporter()

import pandas as pd

data = pd.read_csv('payments.csv')

reporter.show_report(data)
