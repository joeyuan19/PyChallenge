import datetime
import calendar

year = 1996

day = datetime.datetime(year,1,26,0,0,0,0)

for i in range(1000):
    if year < 0:
        break
    day = datetime.datetime(year,1,26,0,0,0,0)
    if day.weekday() == 0 and calendar.isleap(year):
        print year
    year += -10


