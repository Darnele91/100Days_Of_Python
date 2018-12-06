import datetime
import calendar

now = datetime.datetime.now()
print(now.strftime("%d/%b/%y %H:%M"))

next_week = now + datetime.timedelta(days=7)
print(next_week)

first_weekday,number_days=calendar.monthrange(2018,2)
print(first_weekday,number_days)

print(calendar.month(2018,2))
