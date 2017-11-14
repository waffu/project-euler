num = 1000
count = 0
total = 0

for count in range(num):
	if count % 3==0 or count % 5 == 0:
		total += count

print(total)
input()