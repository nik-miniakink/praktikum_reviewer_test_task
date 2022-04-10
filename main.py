import datetime as dt


# Добавить везде Docstrings, в соответствии с Docstring Conventions
# Хорошо бы добавить везде аннотация типов
class Record:
    # Дефолтное значение даты по заданию должно быть текущей датой
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        # Слишком сложная конструкция(учти замечание выше)
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        # Название переменной Record не по PEP8
        for Record in self.records:
            # Лучше сделать как в недельной ститистики
            if Record.date == dt.datetime.now().date():
                # Лучше сделать как в недельной ститистики
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            # Можно упростить условие, посмотри в сторону timedelta
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    # Комментарий лучше сделать в виде докстринга
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        # Плохое название переменной
        x = self.limit - self.get_today_stats()
        # Можно улучшить условие для большей читабельности кода
        if x > 0:
            # Бэкслеши для переносов не применяются
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        # Нет необходимости в else
        else:
            # Лучше использовать один формат форматирования строки
            return ('Хватит есть!')


class CashCalculator(Calculator):
    # Комментарии можно и убратб, значение очевидно.
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.
    # По условиям задания в эту функцию передается 1 аргумент - currency,

    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        currency_type = currency
        # Эту строку можно убрать, изменив условия сравнения
        cash_remained = self.limit - self.get_today_stats()
        # Слишком много условий elif, нужно упростить и сделать универсальнее
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            # Неверное значение переменной, в рублях всегда будет 1
            cash_remained == 1.00
            currency_type = 'руб'

        # Лучше вставить пустую строку, для увеличения читабельности
        if cash_remained > 0:
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        # Проверка условия тут не нужна
        elif cash_remained < 0:
            # Используй один метод форматирования строк
            # Бекслеши не применяются для переноса строк
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)
    # Это излишне, функция есть в родительском классе
    def get_week_stats(self):
        super().get_week_stats()
