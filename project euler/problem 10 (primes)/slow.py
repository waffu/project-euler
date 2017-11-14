p = []
np = []
for i in range(2,10000):
	if i not in np:
		p.append(i)
	for j in range(i*i,10000,i):
		if j not in np:
			np.append(j)
print(p)
input()
