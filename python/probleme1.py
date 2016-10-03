def multiList(x, y):
	return [z * y for z in range(1, int((x - 1) / y) + 1)] 

def main():
	print(sum(set(multiList(1000, 3) + multiList(1000, 5))))

if __name__ == "__main__":
    main()