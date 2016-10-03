dayList = []
weekList = []
count = 0
monthList = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for years in range(1901, 1902):
	monthList[1] = 28 + 1 * bool((not years % 4 and years % 100) or not years % 400)
	for months in range(len(monthList)):
			for days in range(monthList[months]):
				dayList.append(days + 1)

for weeks in range(len(dayList)):
	weekList.append(((weeks + 1) % 7) + 1)

for index in range(len(dayList)):
	count = count + 1 * bool(dayList[index] == 1 and weekList[index] == 1)
print(count, len(dayList), len(monthList), len(weekList), len(dayList), weekList, dayList)


#Réponse mauvaise de 1 :(