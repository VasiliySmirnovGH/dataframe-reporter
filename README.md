# DataFrame Reporter

Небольшой проект для получения базового отчёта о качестве и структуре данных из CSV-файла. В качестве примера используется набор платежей `data/payments.csv`.

## Возможности

Класс `DataFrameReporter` выводит в терминал:

- количество строк и столбцов;
- количество и долю полных дубликатов;
- описательную статистику с помощью `pandas.DataFrame.describe()`;
- количество и долю пропущенных значений.

Параметры класса позволяют настроить формат отображения чисел и процентов, а также включить статистику по всем типам столбцов.

## Структура проекта

```text
.
├── data/
│   └── payments.csv       # исходные данные
├── src/
│   └── reporter.py        # класс DataFrameReporter
├── main.py                # точка входа
├── requirements.txt       # зависимости
└── README.md
```

## Установка

Создайте и активируйте виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```

Установите зависимости:

```bash
python3 -m pip install -r requirements.txt
```

## Запуск

Из корня проекта выполните:

```bash
python3 main.py
```

Программа загрузит `data/payments.csv` и выведет два отчёта: с базовой статистикой только для числовых столбцов и с расширенной статистикой для всех типов данных.

## Использование класса

```python
import pandas as pd

from src.reporter import DataFrameReporter

df = pd.read_csv("data/payments.csv")
reporter = DataFrameReporter(include_all=True)
reporter.show_report(df, "Отчёт по платежам")
```

## Данные

Файл `data/payments.csv` содержит 170 записей о платежах и 7 столбцов:

`order_id`, `payment_method`, `date`, `total`, `feature_1`, `feature_2`, `category`.
