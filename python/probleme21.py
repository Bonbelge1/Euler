def divisors(number):
	lower =  [i for i in range(1, int(number ** (1/2) + 1)) if number % i == 0]
	higher = [number // i for i in reversed(lower)]
	return set(lower + higher)

def main():
	[divisors]

	divisors(220))

if __name__ == '__main__':
	main()
