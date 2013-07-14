import datetime


day = datetime.date(1901,1,1)
count =0 
dt = datetime.timedelta(days=1)

while day.year < 2001:
   # check if sunday & on first of the month
   if day.weekday() == 6 and day.day == 1:
      count += 1
   day = day + dt;


print count
