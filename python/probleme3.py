def listPrimeNumbers(maxRange):
	if maxRange == 2:
		return [2]
	if maxRange < 2:
		return []
	listPrime = [2]
	for testIfPrime in range(3, maxRange + 1, 2):
		verificator = True
		for foundPrimes in listPrime:
			verificator = verificator and (testIfPrime % foundPrimes)
			if not verificator:
				break
		if verificator:
			listPrime.append(testIfPrime)
	return listPrime


def isPrime(number):
	if number < 2:
		return False
	for i in listPrimeNumbers(int(number ** (1/2))):
		if number % i == 0: 
			return False
	return True


def nextPrimeFromNumber(number):
	if number <= 1:
		return 2
	else:
		return nextPrimeFromList(listPrimeNumbers(number))

	
def nextPrimeFromList(primeList):  
	sortedList = sorted(set(primeList))
	#Verification of primes
	for i in sortedList:
		if not isPrime(i):
			return nextPrimeFromNumber(sortedList[-1])
	if sortedList[-1] == 2:
		iterable = 3
	else:
		iterable = sortedList[-1] + 2
	while True:
		verificator = True
		for foundPrimes in [i for i in sortedList if i <= int(iterable ** (1/2))]:
			verificator = verificator and (iterable % foundPrimes)
			if not verificator:
				break
		if verificator:
			return iterable
		iterable += 2	


def addPrimeFromList(primeList):
	return primeList.append(nextPrimeFromList(primeList))


def main():
	nb = 600851475143
	divider = nextPrimeFromNumber(1)
	while divider <= int(nb**(1/2)):
		division = True
		while division:
			if not nb % divider:
				nb //= divider
				#print(nb)
			else:
				division = False
				divider = nextPrimeFromNumber(divider)
	print(nb)		


if __name__ == "__main__":
    main()