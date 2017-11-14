print(max([x*y for x in range(100,1000) for y in range(x,1000) if str(x*y)[::-1] == str(x*y)]))
input()
