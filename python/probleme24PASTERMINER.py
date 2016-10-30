def fact(num):
	if num <= 1:
		return 1
	return num * fact(num - 1) 
	
	
def main():
	lsFact = [(fact(i), int(fact(i)/i)) for i in range(1,11)]
	ls = [i for i in range(10)]