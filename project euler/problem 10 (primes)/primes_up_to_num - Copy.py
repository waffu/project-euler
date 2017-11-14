def primes(n):
	l = [k for k in range(n)]
	prime = []
	nonprime = []
	for i in range(2,n):
		if i not in nonprime:
			prime.append(i)
		for p in range(i*i,n,i):
			nonprime.append(p)
	return prime





print(primes(10000))
input()