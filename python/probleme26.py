def repLen(num):
	rest = 10
	restList = [10]
	aws = []
	while rest != 0:
		rest = rest % num * bool(rest % num) * 10
		if rest in restList:
			return len(restList) - restList.index(rest)
		else:
			restList.append(rest)
	return 0
	
def main():
	ls = [repLen(i) for i in range(1,1001)]
	print(1 + ls.index(max(ls)))
	
if __name__ == "__main__":
    main()