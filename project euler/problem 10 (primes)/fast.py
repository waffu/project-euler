p = []
f = [True for _ in range(1000)]
for i in range(2,1000):
	for j in range(2, i):
		if i%j==0:
			f[i]=False
for i, flag in enumerate(f):
	if flag == True:
		p.append(i)

print(p)

input()
