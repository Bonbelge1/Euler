fiboList = [1, 1]

while fiboList[-1] + fiboList[-2] < 4000000:

	fiboList.append(fiboList[-1] + fiboList[-2])



print(sum([i for i in fiboList if i % 2 == 1]))