def listPrimeNumbers(maxRange):
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
	for i in listPrimeNumbers(int(number ** (1/2))):
		if number % i == 0: 
			return False
	return True
	
def nextPrime(primeList):
	sortedList = sorted(set(primeList))
	iterable = sortedList[-1] + 2
	boolean = True
	while boolean:
		for i in sortedList:
			if iterable % i == 0:
				
		
def main():
	#nb = 600851475143
	#print([i for i in list(reversed(listPrimeNumbers(int(nb ** (1/2))))) if 600851475143 % i == 0])
	#print(isPrime(9))


if __name__ == "__main__":
    main()