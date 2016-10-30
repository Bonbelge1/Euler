def divisors(num):
	lows = [i for i in range(2, int(num ** (1/2)) + 1) if num % i == 0]
	highs = [int(num / i) for i in lows]
	return set(lows + highs)
	
def ab(num):
	if num < sum(divisors(num)):
		return True
	else:
		return False
		
def main():
	ls = [i for i in range(28123) if ab(i)]
	
	addiLs = set([(ls[i] + ls[j]) for i in range(len(ls)) for j in range(i, len(ls))])
	print(sum([i for i in range(28123) if i not in addiLs]))

if __name__ == "__main__":
	main()