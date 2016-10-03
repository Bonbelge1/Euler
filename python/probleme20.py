def factorial(number):
	tot = 1
	for i in range(number):
		tot *= (i + 1)
	return tot

def main():
	print(sum([int(n) for n in str(factorial(100))]))

if __name__ == '__main__':
	main()