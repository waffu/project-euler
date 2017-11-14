
def f(x):
	t, y = 0, 2 ** x
	for n in str(y):
		t += int(n)
	return t