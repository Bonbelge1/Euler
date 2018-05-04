maxSum = 9**5*6
finalList = []

for number in range(10, maxSum):
	if (number == sum([int(letter)**5 for letter in str(number)])):
		finalList.append(number)

print(finalList, sum(finalList))