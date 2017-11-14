largest = 0
for x in range(100,1000):
	for y in range(x,1000):
		if str(x*y)[3:6][::-1] == str(x*y)[0:3] and x*y>largest:largest = x*y
print(largest)
input()
