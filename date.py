# task1
import datetime

now = datetime.date.today()
x = now - datetime.timedelta(days=5)
print(x)

# task2
import datetime

now = datetime.date.today()
x = now - datetime.timedelta(days=1)
a = now + datetime.timedelta(days=1)
print(x)
print(now)
print(a)

# task3
import datetime
now=datetime.datetime.now()
wo_ms=now.replace(microsecond=0)
print(wo_ms)

#task4
import datetime
date1=datetime.date(2024, 2, 23)
date2=datetime.date(2022, 11, 7)
dif=date1-date2
dif_in_s=dif.total_seconds()
print(dif_in_s)
