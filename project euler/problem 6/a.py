a_sum, b_sum = 0,0
for i in range(101):
	a,b = i*i, i
	a_sum += a
	b_sum += b
b_sum = b_sum*b_sum
difference = b_sum-a_sum

print(difference)
input()