# date and time (latihan)

import datetime as dt

hari_ini = dt.datetime.today()
print(hari_ini)
print(f"hari ini adalah hari  = {hari_ini:%A}")

tanggal = dt.date(2004,6,30)
print(tanggal)
print(f"hari ini adalah hari  = {tanggal:%A}")

now = dt.datetime.now()
print(now)