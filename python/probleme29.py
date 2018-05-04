def main():
	a = [x for x in range(2,100+1)]
	b = a
	list = [i**j for i in a for j in b]
	print(len(set(list)))

if __name__ == '__main__':
	main()