def divisor(x):
	
	multi3 = [y * 3 for y in range(1, int((x - 1)/3) + 1)]
	
	multi5 = [z * 5 for z in range(1, int((x - 1)/5) + 1)]
	
	return(sum(set(multi3 + multi5)))