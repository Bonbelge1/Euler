def main():
	
	fibo = [1, 1]
	i = 1
	while len(str(fibo[i])) < 1000:
		fibo.append(fibo[i] + fibo[i - 1])
		i += 1

	print(i + 1)

if __name__ == '__main__':
	main()