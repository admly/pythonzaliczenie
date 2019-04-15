import calendar
import locale

locale = locale.setlocale(locale.LC_ALL, 'pl_PL')
monthsToInts = {'styczen': 1, 'luty': 2, 'marzec': 3, 'kwiecien': 4,
                'maj': 5,'czerwiec': 6, 'lipiec': 7, 'sierpien': 8,
                'wrzesien': 9, 'pazdziernik': 10, 'listopad': 11,
                'grudzien': 12}

y = int(input("Rok: "))
m = monthsToInts.get((input("Miesiac: ")))

print(calendar.month(y, m))
