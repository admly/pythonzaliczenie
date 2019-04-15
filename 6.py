from datetime import datetime


def calculate_days_between(date_start, date_end):
    date_format = "%m.%d.%Y"
    a = datetime.strptime(date_start, date_format)
    b = datetime.strptime(date_end, date_format)
    delta = b - a
    if delta.days > 0:
        print(delta.days)
    else:
        print("wrong dates")


calculate_days_between('8.18.2019', '8.31.2019')
