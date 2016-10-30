from itertools import permutations
	

def fact(num):
	if num <= 1:
		return 1
	return num * fact(num - 1) 

def main():
	# ls = list(permutations(range(10)))
	# rep = (list(ls[999999]))
	# print("".join([str(i) for i in rep]))

	position = 999999
	factoList = [fact(i) for i in range(10)]
	listComp = [i for i in range(10)]
	positionList = []
	comb = []

	for i in range(len(listComp)):
		positionList.append(position // factoList[-(i + 1)])
		position -= (position // factoList[-(i + 1)]) * factoList[-(i + 1)]

	for i in positionList:
		comb.append(listComp[i])
		del listComp[i]

	print("".join([str(i) for i in comb]))

if __name__ == '__main__':
	main()