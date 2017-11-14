def primes(n):
	l = [k for k in range(n)]
	for i in range(2,6,1):
		if i!=2 and i%2==0:
			pass
		else:
			for j in range(i*i, n, i):
				if j in l:
					l.remove(j)
	return l



print(primes(100000))
input()