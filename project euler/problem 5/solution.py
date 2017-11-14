c = 0
x = False
while x == False:
	c += 20
	for i in range(1,21):
		if c%i==0:
			if i==20:
				x = True
		else:
			break

print(c)
input()