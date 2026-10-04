import pandas as pd
from src.reporter import DataFrameReporter


def main():
    df = pd.read_csv("data/payments.csv")
    reporter = DataFrameReporter(df)
    reporter.show_report()

if __name__ == "__main__":
    main()
