#def multiList(x, y):
#	return [z * y for z in range(1, int((x - 1) / y) + 1)] 

def main():
#	print(sum(set(multiList(1000, 3) + multiList(1000, 5))))
	print(sum([i for i in range(1000) if (not i % 3) or (not i % 5)]))
if __name__ == "__main__":
    main()
