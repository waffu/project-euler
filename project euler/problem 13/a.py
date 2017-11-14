t, f = [], open("numbers.txt", "r")
for line in f:
	t.append(int(line))
print(str(sum(t))[:10])
input()