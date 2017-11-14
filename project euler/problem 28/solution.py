# difference between each diagonal number
# increases by 8 every increment after second value
# therefore I will keep four lists of differences
# and one list for storing the numbers to be summed

rightup = [1,8]
rightdown = [1,2]
leftup = [1,6]
leftdown = [1,4]

l = []

for n in range(500):

	l.append(sum(rightup))
	rightup.append(rightup[-1]+8)

	l.append(sum(rightdown))
	rightdown.append(rightdown[-1]+8)

	l.append(sum(leftup))
	leftup.append(leftup[-1]+8)

	l.append(sum(leftdown))
	leftdown.append(leftdown[-1]+8)

print(sum(l)+1)
