import datetime as dt
import pytz
x = dt.datetime.today()

print(x)
print(x.month)
print(x.isoweekday())

tdelta = dt.timedelta(7)
print(x + tdelta)

day_birthday = dt.datetime(2021,12,3, 7,36,42,tzinfo = pytz.utc)

print(day_birthday)

# till_birthday = day_birthday - x
# # kind of time delta
# print(till_birthday)
# print(till_birthday.days)


# Note: today has no choice of timezone but now has an option to add a timezone (Difference)


# dt_now = dt.datetime.now()

dt_utcnow =dt.datetime.utcnow()

