import random

days_list = []

for days in range(0, 500):
	year = str(random.randint(2012, 2017))
	month_pre = random.randint(1, 12)
	if month_pre < 10:
		month = str(0) + str(month_pre)
	else:
		month = str(month_pre)
	if month == '09' or month == '04' or month == '06' or month == '11':
		day_pre = random.randint(1, 30)
		if day_pre < 10:
			day = str(0) + str(day_pre)
		else:
			day = str(day_pre)
	elif month == '02':
		if int(year)%4 == 0:
			day_pre = random.randint(1,29)
			if day_pre < 10:
				day = str(0) + str(day_pre)
			else:
				day = str(day_pre)
		else:
			day_pre = random.randint(1,28)
			if day_pre < 10:
				day = str(0) + str(day_pre)
			else:
				day = str(day_pre)
	else:
		day_pre = random.randint(1, 31)
		if day_pre < 10:
			day = str(0) + str(day_pre)
		else:
			day = str(day_pre)
	date = year
	date += month
	date += day
	days_list.append(date)

print(*days_list, sep=' ')
