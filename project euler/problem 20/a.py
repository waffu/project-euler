def f(x):
	y, t = 1, 0
	for n in range(x,0,-1):y*=n
	for num in str(y):t+=int(num)
	return t