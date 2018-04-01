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


def quad(n,a,b):
	return n*n+a*n+b

def main():
	aList = [i for i in range(-999,1000)]
	bList = [i for i in range(-1000,1001)]
	WWList = []

	for aValue in aList:
		for bValue in bList:
			
			increment = 0
			while isPrime(quad(increment, aValue, bValue)):
				increment += 1

			if increment:
				WWList.append((increment-1, aValue, bValue))

	WinWinChickenDinner = max(WWList)
	print(WinWinChickenDinner)
	print(WinWinChickenDinner[1] * WinWinChickenDinner[2])
	
			


		




if __name__ == '__main__':
	main()