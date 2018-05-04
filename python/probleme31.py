#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
def main():
	amount = 200
	coins = (200 ,100, 50, 20, 10, 5, 2, 1)
	print(recursion(amount, coins, 0))

def recursion(value, listCoins, index):
	possibilities = 0
	canBeDivided = [i for i in range(0, int(value/listCoins[index])+1)]
	if (not bool(canBeDivided)) or (listCoins[index] == 1):
		return 1
	else:
		for j in canBeDivided:
			possibilities += recursion(value-j*listCoins[index], listCoins, index+1)
	return possibilities

if __name__ == '__main__':
	main()