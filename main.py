import pandas as pd
from src.reporter import DataFrameReporter


def main():
    df = pd.read_csv("data/payments.csv")

    reporter_1 = DataFrameReporter(
        float_format="0.02f",
        percent_format="0.03%",
    )
    reporter_2 = DataFrameReporter(
        float_format="0.03f",
        percent_format="0.01%",
        include_all=True,
    )

    reporter_1.show_report(df, "Отчёт в формате 1:")
    print()
    reporter_2.show_report(df, "Отчёт в формате 2:")


if __name__ == "__main__":
    main()
