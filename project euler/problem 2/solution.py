num1 = 1
num2 = 2
total = 0
fibo = []
fibo.append(num1)
fibo.append(num2)

# make sequence, trimmed the range value through printing and lowering range value on repeat xD
for i in range(30):
	nextnum = fibo[i] + fibo[i + 1]
	fibo.append(nextnum)

for i in range(len(fibo)):
	if fibo[i] % 2 == 0:
		total += fibo[i]

print(total)
input()
