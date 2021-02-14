import datetime

today = datetime.date.today()
print(today)

next_birthday = datetime.date.fromisoformat('2022-01-06')
print(next_birthday)
print(type(next_birthday))

days_remains= next_birthday - today
print(days_remains.days)
print(type(days_remains))

next_20_days = today + datetime.timedelta(days=20)
print(next_20_days)

print(__name__)

