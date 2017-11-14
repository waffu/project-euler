grid, l = {}, []
with open("data.txt", "r",) as f:
	for i, line in enumerate(f):
		for j, item in enumerate(line.split(" ")):
			grid[j,i]= int(item)
for y in range(20):
	for x in range(16):
		l.append(grid[x,y] * grid[x+1,y] * grid[x+2,y] * grid[x+3,y])
		if y < 17:
			l.append(grid[x,y] * grid[x,y+1] * grid[x,y+2] * grid[x,y+3])
		if y < 17:
			l.append(grid[x,y] * grid[x+1,y+1] * grid[x+2,y+2] * grid[x+3,y+3])
		if y > 3:
			l.append(grid[x,y] * grid[x+1,y-1] * grid[x+2,y-2] * grid[x+3,y-3])
print(max(l))
input()





