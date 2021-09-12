def readable_timedelta(num):
    weeks = 0
    days = 0
    weeks = num//7
    days = num%7
    # return ("{} week(s) and {} day(s)".format(weeks,days))
    return (f"{weeks} week(s) and {days} day(s)")

a = int(input("Please enter number of days"))
print(readable_timedelta(a))